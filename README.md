# FINDCov19TrackerData

<!-- badges: start -->
[![tic](https://github.com/dsbbfinddx/data/workflows/tic/badge.svg?branch=master)](https://github.com/dsbbfinddx/data/actions)
<!-- badges: end -->

Raw and processed data for [dsbbfinddx/FINDCov19TrackerShiny](https://github.com/dsbbfinddx/FINDCov19TrackerShiny)

# Manual test data preparation

Some parts of the test data are collated manually every day by the FIND team, from information found online.

1. Some data is grabbed with [Selenium IDE](https://www.selenium.dev/selenium-ide/), using the playback sequence saved in `scrap_tests_data.side`. 
  Some website may be slow to answer, the sequence can be played back from where it last stopped.
  When everything is finished, save the output log as a text file named `output_selenium_YYYYMMDD.txt`.
2. The rest is fetch directly from the R script `grab_tests_data_29-06-2020.R`, that download and parse locally data such as CSV, XLSX, ZIP, PDF, HTML, etc. 
  Currently 110+ countries are updated automatically this way. 
  This may vary from one day to another if the page/report file still exists at the expected location and the layout wasn't changed too dramatically. 
  A csv file is produced as a result under the name `coronavirus_tests_YYYYMMDD_sources_SO.csv`, in which manual updates are made afterwards (for other type of reports like ArcGIS dashboard, image, etc).
3. The R package {FindCovTracker} takes this data and writes processed versions to `processed/`, which are then taken as input for the final Shiny App.
