# Suicide, Homicide, Traffic mortality

 Suicide, Homicide, Traffic mortality

## Indicators

Deaths per 100k standard population (Age Standardized Death Rate) for
several age groups.

## Data sources summary

Data before 1990 come form WHO [Violence and Injury Prevention dataset](http://www.who.int/violence_injury_prevention/en/), and
data after 1990 come from IHME [Global Burden of Disease dataset](http://ghdx.healthdata.org/gbd-results-tool).

Please note that there are some differences between WHO's definition
and IHME's definition for suicide/homicide/traffic accidents.  Both of
them use ICD system: the 3 causes of death are defined by a group of
ICD codes. In some cases, they use different codes. Here is how they
compare to each other:

- for suicide and homicide, WHO and GBD use same ICD9 codes. For
  traffic accident, ICD9 column is empty in the GBD doc, so not sure
  if they are the same
- for ICD10:
  + Interpersonal violence (homocide): no difference
  + Self harm (suicide): GBD doesn't include X65 "Intentional
    self-poisoning by and exposure to alcohol"
    http://apps.who.int/classifications/icd10/browse/2010/en#/X65
  + GBD doesn't include V81 (Occupant of railway train or railway
    vehicle injured in transport accident) WHO includes V81.1
    (Occupant of railway train or railway vehicle injured in collision
    with motor vehicle in traffic accident)
  + GBD includes full V82 (Occupant of streetcar injured in transport
    accident) WHO only includes V82.1, V82.8 and V82.9 (Occupant of
    streetcar injured in collision with motor vehicle in traffic
    accident, Occupant of streetcar injured in other specified
    transport accidents, Occupant of streetcar injured in unspecified
    traffic accident)
  + WHO includes traffic related parts (often .0-.3) V83-V99 and Y850
    while GBD only includes V87.2 and V87.3
