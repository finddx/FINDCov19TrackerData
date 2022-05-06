# FIND COVID-19 Test Data Collection

<!-- badges: start -->

![Scrape test data](https://github.com/finddx/FINDCov19TrackerData/workflows/Scrape%20test%20data%20and%20push/badge.svg)

<!-- badges: end -->


Several countries and entities, including the World Bank, publish aggregate estimates on the total number of tests performed.
These reports are published across individual websites and press releases – often in multiple languages and updated with different periodicity.

The FIND team collects test data from information found online. It combines it with case and deaths data from John Hopkins University and displays them in an [interactive tracker dashboard](https://www.finddx.org/covid-19/test-tracker).

This repository contains the intermediate and final data of the data collection process.


## Available Data

- [`processed/coronavirus_test.csv`](https://github.com/finddx/FINDCov19TrackerData/tree/selenium/processed): Test data collected by the FIND team.

- [`processed/data_all.csv`](https://github.com/finddx/FINDCov19TrackerData/blob/master/processed/data_all.csv): Test data combined with case and deaths data from John Hopkins University, including group aggregations. An [interactive tracker dashboard](https://www.finddx.org/covid-19/test-tracker) displays the data.


## Sources

**Test data**: Collated every day by the FIND team from information found online.
A large fraction is automated via Python and R (see below).
A minor fraction is gathered by manual visits to the respective country websites.
_Generally, the official government websites of each country are consulted._

**Case data**: Downloaded daily from the COVID19 [John Hopkins University (JHU) repository](https://github.com/CSSEGISandData/COVID-19).



## Aggregation

When aggregating over periods and/or groups, we apply the following principles in turn:

**1. Aggregation over period**: If data is missing during more than 25% of the most
recent observations, the period is considered incomplete, no aggregated
value is computed.

**2. Aggregation over group**: Groups aggregations use all the countries for which
data is available. If a ratio is computed (e.g., per capita measures,
positivity rate), we only consider observations that have values both for
the nominator and the denominator. E.g., to calculate tests
per capita for a continent, a country is only used if it reports both test and population data.

When we aggregate both over period and group, we do period aggregation first and group aggregation second.

The [codebook](https://github.com/finddx/shinyfind/blob/main/inst/codebook/codebook_extended.csv) provides a detailed description of how these two steps look for each variable.


## Workflow Description

### High-level Overview

The main part of the test data is scraped in an automated fashion by combining Python and R-based solutions.
COVID-19 tests are queried twice daily (early in the morning and late in the evening).
Because countries change their way of reporting from time to time, manual action is needed for some countries.

1. Most countries are scraped via Python using [Selenium](https://pypi.org/project/selenium/) or [json](https://docs.python.org/3/library/json.html) libraries, and place in [`automated/selenium/`](https://github.com/finddx/FINDCov19TrackerData/tree/master/automated/selenium).
2. Countries that report in PDF (or other non-HTML formats) are queried via R functions and placed in [`automated/fetch/`](https://github.com/finddx/FINDCov19TrackerData/tree/master/automated/fetch).
3. Lastly, country information gathered via manual website visits is added and combined into a single information source listing the number of tests from all different sources (located at [`automated/merged/`](https://github.com/finddx/FINDCov19TrackerData/tree/master/automated/merged)).

The R package [{FindCovTracker}](https://finddx.github.io/FINDCov19Tracker/reference/index.html), which powers most of the automated actions run via GitHub Actions, takes this data and writes [`processed/coronavirus_test.csv`](https://github.com/finddx/FINDCov19TrackerData/tree/selenium/processed).

In a final step, the workflow combines the data with case and deaths data from John Hopkins University and writes [`processed/data_all.csv`](https://github.com/finddx/FINDCov19TrackerData/blob/master/processed/data_all.csv) which is being used as the input for the Shiny app.


### Details

This section explains the workflow in greater detail, including links to all R functions from the [{FindCovTracker}](https://finddx.github.io/FINDCov19Tracker/reference/index.html) R package and how conflicts/errors are handled in the individual stages.

#### 1. Test data scraping via Selenium

- Selenium python code located in `selenium/` is run, specifically `python3 selenium/run.py` is executed.
- The result is uploaded as a JSON file to the [`automated/selenium/`](https://github.com/finddx/FINDCov19TrackerData/tree/master/automated/selenium) directory with a prefix of the respective date.
- `new_tests` are calculated from the different to the previous day.
- **What happens on error?**: Countries that do not return a value after the specified timeout in `selenium/test.py` will be reported as `NA`.
  The country will also be listed in the [all-countries-error.csv](https://github.com/finddx/FINDCov19TrackerData/tree/master/issues).

#### 2. Test data scraping via "R fetch functions"

- [`fetch_test_data()`](https://finddx.github.io/FINDCov19Tracker/reference/fetch_test_data.html) processes countries specified in the [respective upstream file](https://github.com/finddx/FINDCov19Tracker/blob/master/R/preprocess.R) with dedicated functions for the given file type (e.g. PDF).
- **What happens on error?**: the functions operate with a "try/catch" approach and return NA if something does not work.
  The country will also be listed in the [countries-error.csv](https://github.com/finddx/FINDCov19TrackerData/tree/master/issues) file of the respective day.

#### 3. Combination of Selenium, "R fetch functions", and manual updates

The third step in the CI workflow combines the results from Selenium, fetch functions, and manual updates when they are available in [`manual/processed/`](https://github.com/finddx/FINDCov19TrackerData/tree/master/manual/processed).
The function [`get_test_data()`](https://finddx.github.io/FINDCov19Tracker/reference/)
writes out a combined data source to [`automated/merged/`](https://github.com/finddx/FINDCov19TrackerData/tree/master/automated/merged).
In addition, the list with countries that errored (`all-countries-error.csv`) is written.

#### 4. Analysis of Workflow Run

The last step performs some analysis on the previous workflow steps.
In particular, [`combine_all_tests()`](https://finddx.github.io/FINDCov19Tracker/reference/combine_all_tests.html)

- writes the file which lists all countries that still need manual processing ([`$DATE-need-processing.csv`](https://github.com/finddx/FINDCov19TrackerData/tree/master/manual/need-processing))
- writes [`coronavirus_tests_new.csv`](https://github.com/finddx/FINDCov19TrackerData/blob/master/automated/coronavirus_tests_new.csv), which lists information from all dates and all countries that have been processed so far.

This step exists twice in the [GHA workflow file](https://github.com/finddx/FINDCov19TrackerData/blob/master/.github/workflows/automate-tests.yml):

- Job: `run-analysis` runs when automated scraping has happened before and therefore includes a `needs` condition.
- Job: `run-analysis-manual` runs only if the commit message contains `manually processed countries`.
  Also, in this scenario, the scraping jobs are not triggered.

The reasoning here is that if the `.csv` file containing the manual information for countries is uploaded, it should only be merged into the final file.
The automated data scraping should not be triggered again since a new run could lead to new failures for some countries.
These new failing countries would then be missing for the day since they were not processed manually beforehand.

#### 5. Combine with other data

COVID-19 Case data is processed in the following way:

- [`FINDCov19Tracker::process_jhu_data()`](https://finddx.github.io/FINDCov19Tracker/reference/process_jhu_data.html): main function which starts all John Hopkins University (JHU) data processing.
  The functions calls [`FINDCov19Tracker::preprocess_jhu_data()`](https://finddx.github.io/FINDCov19Tracker/reference/preprocess_jhu_data.html) and [`FINDCov19Tracker::check_jhu_data()`](https://finddx.github.io/FINDCov19Tracker/reference/check_jhu_data.html) and writes `processed/coronavirus_cases.csv`.

A final step combines case and test data and aggregates data into groups:

[`FINDCov19Tracker::create_shiny_data()`](https://finddx.github.io/FINDCov19Tracker/reference/create_shiny_data.html): makes use of [`coronavirus_cases.csv`](https://github.com/finddx/FINDCov19TrackerData/blob/master/processed/coronavirus_cases.csv) and [`coronavirus_tests.csv`](https://github.com/finddx/FINDCov19TrackerData/blob/master/processed/coronavirus_tests.csv).
The function writes [`processed/data_all.csv`](https://github.com/finddx/FINDCov19TrackerData/blob/master/processed/data_all.csv), which is being used as the input for the Shiny app.



