# FINDCov19TrackerData

<!-- badges: start -->

[![tic](https://github.com/dsbbfinddx/data/workflows/tic/badge.svg?branch=master)](https://github.com/dsbbfinddx/data/actions)
![Scrape test data](https://github.com/dsbbfinddx/FINDCov19TrackerData/workflows/Scrape%20test%20data%20and%20push/badge.svg)

<!-- badges: end -->

- [FINDCov19TrackerData](#findcov19trackerdata)
- [Test data scraping](#test-data-scraping)
  - [High-Level Workflow Description](#high-level-workflow-description)
  - [Detailed Workflow Description](#detailed-workflow-description)
    - [1. Test data scraping via Selenium](#1-test-data-scraping-via-selenium)
    - [2. Test data scraping via "R fetch functions"](#2-test-data-scraping-via-r-fetch-functions)
    - [3. Combination of Selenium and "R fetch functions"](#3-combination-of-selenium-and-r-fetch-functions)
    - [4. Analysis of Workflow Run](#4-analysis-of-workflow-run)

Raw and processed data for [dsbbfinddx/FINDCov19TrackerShiny](https://github.com/dsbbfinddx/FINDCov19TrackerShiny)

# Test data scraping

## High-Level Workflow Description

The main part of the test data is scraped in an automated fashion by combining Python and R based solutions.
COVID-19 tests are queried twice per day (early in the morning and late in the evening).
Due to the fact that countries change their way of reporting from time to time, manual action is needed on a daily base for some countries.

1. Most countries are scraped via [Selenium](https://www.selenium.dev) by invoking a playback sequence via the Python interface and place in [`automated/selenium/`](https://github.com/dsbbfinddx/FINDCov19TrackerData/tree/master/automated/selenium).
2. Countries which report in PDF (or other non-HTML formats) are queried via R functions and placed in [`automated/fetch/`](https://github.com/dsbbfinddx/FINDCov19TrackerData/tree/master/automated/fetch).
3. Last, country information gathered via manual website visits is added and combined into a single information source listing the number of tests from all different sources (located at [`automated/merged/`](https://github.com/dsbbfinddx/FINDCov19TrackerData/tree/master/automated/merged)).

The R package [{FindCovTracker}](https://dsbbfinddx.github.io/FINDCov19Tracker/reference/index.html), which powers most of the automated actions run via GitHub Actions, takes this data and writes [`processed/coronavirus_test.csv`](https://github.com/dsbbfinddx/FINDCov19TrackerData/tree/selenium/processed) which is then taken as input for the final Shiny App.

## Detailed Workflow Description

The following section explains the workflow in greater detail, including links to all R functions from the [{FindCovTracker}](https://dsbbfinddx.github.io/FINDCov19Tracker/reference/index.html) R package and how conflicts/errors are handled in the individual stages.

### 1. Test data scraping via Selenium

- Selenium python code located in `selenium/` is run, specifically `python3 selenium/run.py` is executed.
- The result is uploaded as a JSON file to the [`automated/selenium/`](https://github.com/dsbbfinddx/FINDCov19TrackerData/tree/master/automated/selenium) directory with a prefix of the respective date.
- `new_tests` are calculated from the different to the previous day.
- **What happens on error?**: Countries which do not return a value after the specified timeout in `selenium/test.py` will be reported as `NA`.
  The country will also be listed in the [countries-error.csv](https://github.com/dsbbfinddx/FINDCov19TrackerData/tree/master/issues) file of the respective day.

### 2. Test data scraping via "R fetch functions"

- [`fetch_test_data()`](https://dsbbfinddx.github.io/FINDCov19Tracker/reference/fetch_test_data.html) processes countries specified in the [respective upstream file](https://github.com/dsbbfinddx/FINDCov19Tracker/blob/master/R/preprocess.R) with dedicated functions for the given file type (e.g. PDF).
- **What happens on error?**: the functions operate with a "try/catch" approach and return NA in case something does not work.
  The country will also be listed in the [countries-error.csv](https://github.com/dsbbfinddx/FINDCov19TrackerData/tree/master/issues) file of the respective day.

### 3. Combination of Selenium, "R fetch functions", and manual updates

The third step in the CI workflow combines the results from Selenium, fetch functions, and manual updates when they are available in [`manual/processed/`](https://github.com/dsbbfinddx/FINDCov19TrackerData/tree/master/manual/processed).
The function [`get_test_data()`](https://dsbbfinddx.github.io/FINDCov19Tracker/reference/).
writes out a combined data source to [`automated/merged/`](https://github.com/dsbbfinddx/FINDCov19TrackerData/tree/master/automated/merged). In addition, the list with countries which errored (`countries-error.csv`) is written.

### 4. Analysis of Workflow Run

The last step performs some analysis on the previous workflow steps.
In particular, [`combine_all_tests()`](https://dsbbfinddx.github.io/FINDCov19Tracker/reference/combine_all_tests.html)

- writes the file which lists all countries that still need manual processing ([`$DATE-need-processing.csv`](https://github.com/dsbbfinddx/FINDCov19TrackerData/tree/master/manual/need-processing))
- writes [`coronavirus_tests_new.csv`](https://github.com/dsbbfinddx/FINDCov19TrackerData/blob/master/automated/coronavirus_tests_new.csv) which lists information from all dates and all countries which have been processed so far

This step exists twice in the [GHA workflow file](https://github.com/dsbbfinddx/FINDCov19TrackerData/blob/master/.github/workflows/automate-tests.yml):

- Job: `run-analysis` is run when automated scraping has happened before and therefore includes a `needs` condition
- Job: `run-analysis-manual` is only run if the commit message contains `manually processed countries`.
  Also in this scenario the automation jobs are not triggered.

The reasoning here is that if the `.csv` file containing the manually information for countries is uploaded, it should only be merged into the final file.
The automated data scraping should not be triggered again since a new run could potentially lead to new failures for some countries.
These new failing countries would then be missing for the day since they were not processed manually beforehand.
