# FINDCov19TrackerData

<!-- badges: start -->

[![tic](https://github.com/dsbbfinddx/data/workflows/tic/badge.svg?branch=master)](https://github.com/dsbbfinddx/data/actions)
![Scrape test data](https://github.com/dsbbfinddx/FINDCov19TrackerData/workflows/Scrape%20test%20data%20and%20push/badge.svg)

<!-- badges: end -->

Raw and processed data for [dsbbfinddx/FINDCov19TrackerShiny](https://github.com/dsbbfinddx/FINDCov19TrackerShiny)

# Test data scraping

The main part of the test data is scraped in an automated fashion by combining Python and R based solutions.
COVID-19 tests are queried twice per day (early in the morning and late in the evening).
Due to the fact that countries change their way of reporting from time to time, manual action is needed on a daily base for some countries.

1. Most countries are scraped via [Selenium](https://www.selenium.dev) by invoking a playback sequence via the Python interface.
2. Countries which report in PDF or other non-HTML reports are queried via R functions developed by the FIND team.
3. Last, country information gathered via manual website visits is added to the list and combined into a single information source listing the number of tests for a total of 179 countries.

The R package {FindCovTracker}, which powers most of the automated actions run via GitHub Actions, takes this data and writes [`processed/coronavirus_test.csv`](https://github.com/dsbbfinddx/FINDCov19TrackerData/tree/selenium/processed) which is then taken as input for the final Shiny App.
