# -*- coding: utf-8 -*-

from ddf_utils.chef.ingredient import ProcedureResult, Ingredient
from ddf_utils.chef.helpers import create_dsk, debuggable
import logging


logger = logging.getLogger("asdr")


def _calculate(cdrs, std_pop, age_group_mapping, age_column, data_keys, indicator_name):
    """age_group_mapping: map age in cdrs -> age in std_pop"""
    index_keys = data_keys.copy()
    index_keys.remove(age_column)
    cdrs_groups = [(cdrs[cdrs[age_column] == x].copy()
                    .drop(age_column, axis=1)
                    .set_index(index_keys)) for x in age_group_mapping.keys()]
    std_pop_groups = [std_pop[std_pop.index.isin(x)].sum().values[0] for x in age_group_mapping.values()]
    total_pop = sum(std_pop_groups)
    weights = [x/total_pop for x in std_pop_groups]
    assert len(weights) == len(cdrs_groups)
    zipped = zip(weights, cdrs_groups)
    w0, cdr0 = next(zipped)
    rate = w0 * cdr0
    for w, cdr in zipped:
        r1, r2 = rate.align(w * cdr)
        rate = r1.fillna(0) + r2.fillna(0)
    return rate


@debuggable
def asdr(chef, ingredients, result, standard_population, age_group_mapping, age_column, indicator_name):

    assert len(ingredients) == 1, "`ingredients` parameter only accept exactly one ingredient"

    ingredient = ingredients[0]
    std_pop = chef.dag.get_node(standard_population).evaluate()

    data = ingredient.compute()
    data_keys = ingredient.key_to_list()

    pop_data = std_pop.compute()[std_pop.key].set_index(std_pop.key)
    cdrs = list(data.values())[0]

    # if indicator_name == 'death_rate_0_14':
    #     import ipdb; ipdb.set_trace()

    # double checking
    for k, vs in age_group_mapping.items():
        if k not in cdrs[age_column].values:
            logger.warning(f"no data for {k} in cdr")
        for v in vs:
            if v not in pop_data.index.values:
                logger.warning(f"no data for {v} in standard population")

    rate = _calculate(cdrs, pop_data,
                      age_group_mapping, age_column, data_keys, indicator_name)

    data_keys.remove(age_column)

    rate.columns = [indicator_name]
    new_data = {indicator_name: rate.dropna().reset_index()}

    return ProcedureResult(chef, result, ','.join(data_keys), new_data)
