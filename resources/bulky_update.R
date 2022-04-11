library(dplyr)
library(rio)
library(readr)
library(data.table)
library(stringr)

##### function to update with one number in selenium folder #####

update_selenium_with_number <- function(f_date,#"2021-09-09"
                                        e_date,#"2021-12-26"
                                        country_update,#"ElSalvador"
                                        value_update #"1221446"
                                        ){
  today <- format(Sys.time(), "%Y-%m-%d")
  first_date <- as.Date(f_date)
  window_update <- seq(first_date, as.Date(e_date), by = "days")

  selenium_sele<- sprintf(
    "https://raw.githubusercontent.com/finddx/FINDCov19TrackerData/master/automated/selenium/%s-tests-selenium.csv", # nolint
    window_update
  )
  merged_selenium_tests <- rio::import_list(selenium_sele, rbind = TRUE) %>%
    dplyr::select(-`_file`)

  update_values <-  merged_selenium_tests %>%
    mutate(tests_cumulative =
             if_else(country == country_update,
                     value_update,
                     tests_cumulative))

  separate_files <- update_values %>%
    dplyr::arrange(country, date) %>%
    dplyr::group_by(date, .add =TRUE) %>%
    dplyr::group_split()


  mapply(
    readr::write_csv,
    separate_files,
    paste0(window_update, "-tests-selenium.csv")
  )
}

##### function to delete the country from manual files #####
delete_country_manual_f <- function(f_date,#"2021-09-09"
                                    e_date,#"2021-12-26"
                                    country_update#"ElSalvador"
                                    ){
  today <- format(Sys.time(), "%Y-%m-%d")
  first_date <- as.Date(f_date)
  window_update <- seq(first_date, as.Date(e_date), by = "days")


  manual_sele<- sprintf(
    "https://raw.githubusercontent.com/finddx/FINDCov19TrackerData/master/manual/processed/%s-processed-manually.csv", # nolint
    window_update
  )
  manual_tests <- rio::import_list(manual_sele, rbind = TRUE) %>%
    dplyr::select(-`_file`)

  delete_country <-  manual_tests %>%
    filter(country != country_update)

  separate_files <- delete_country %>%
    dplyr::arrange(country, date) %>%
    dplyr::group_by(date, .add =TRUE) %>%
    dplyr::group_split()

  mapply(
    readr::write_csv,
    separate_files,
    paste0("manual/processed/" ,window_update, "-processed-manually.csv")
  )

}

##### function to update with one file several values in selenium folder #####
# important: just works to update values after 2021-02-18
update_selenium_with_file <-function(f_date,#"2021-09-09"
                                     e_date,#"2021-12-26"
                                     country_update,#"ElSalvador"
                                     country_update_path){

  today <- format(Sys.time(), "%Y-%m-%d")
  first_date <- as.Date(f_date)
  window_update <- seq(first_date, as.Date(e_date), by = "days")

  selenium_sele<- sprintf(
    "https://raw.githubusercontent.com/finddx/FINDCov19TrackerData/master/automated/selenium/%s-tests-selenium.csv", # nolint
    window_update
  )
  selenium_tests <- rio::import_list(selenium_sele, rbind = TRUE) %>%
    dplyr::select(-`_file`)

  country_update_file <- readr::read_csv(file.path(country_update_path),
                             readr::cols(country=col_character(),
                                         tests_cumulative = col_character()),
                             col_names = TRUE
  ) %>% mutate(date = data.table::as.IDate(date)) %>%
    dplyr::filter(date >= "2021-02-18") %>%
    dplyr::filter(date <= e_date) # nolint

  merged_files <- dplyr::full_join(selenium_tests,
    country_update_file,by=c("country", "date"))

  merged_f <-  merged_files %>%
    mutate(tests_cumulative =
             if_else(country == country_update,
                     tests_cumulative.y,
                     tests_cumulative.x)) %>%
    select(-tests_cumulative.x,-tests_cumulative.y) %>%
    relocate(country,date,tests_cumulative)

  separate_files <- merged_f %>%
    dplyr::arrange(country, date) %>%
    dplyr::group_by(date, .add =TRUE) %>%
    dplyr::group_split()


  mapply(
    readr::write_csv,
    separate_files,
    paste0("automated/selenium/", window_update, "-tests-selenium.csv")
  )
}


##### function to update with one file several values in manual folder #####
# important: just works to update values after 2021-02-18
update_manual_with_file <-function(f_date,#"2021-09-09"
                                     e_date,#"2021-12-26"
                                     country_update,#"ElSalvador"
                                     country_update_path){

  today <- format(Sys.time(), "%Y-%m-%d")
  first_date <- as.Date(f_date)
  window_update <- seq(first_date, as.Date(e_date), by = "days")

  manual_sele<- sprintf(
    "https://raw.githubusercontent.com/finddx/FINDCov19TrackerData/master/manual/processed/%s-processed-manually.csv", # nolint
    window_update
  )
  manual_tests <- rio::import_list(manual_sele, rbind = TRUE) %>%
    dplyr::select(-`_file`)

  country_update_file <- readr::read_csv(file.path(country_update_path),
                                         readr::cols(country=col_character(),
                                                     tests_cumulative = col_character()),
                                         col_names = TRUE
  ) %>% mutate(date = data.table::as.IDate(date)) %>%
    dplyr::filter(date >= "2021-02-18") %>%
    dplyr::filter(date <= e_date) # nolint

  merged_files <- dplyr::full_join(manual_tests,
                                   country_update_file,by=c("country", "date"))

  merged_f <-  merged_files %>%
    mutate(tests_cumulative =
             if_else(country == country_update,
                     tests_cumulative.y,
                     tests_cumulative.x)) %>%
    mutate(new_tests =
             if_else(country == country_update,
                     as.integer(0),
                     new_tests)) %>%
    mutate(tests_cumulative_corrected =
             if_else(country == country_update,
                     NA_character_,
                     tests_cumulative_corrected)) %>%
    mutate(new_tests_corrected =
             if_else(country == country_update,
                     NA_integer_,
                     new_tests_corrected)) %>%
    select(-tests_cumulative.x,-tests_cumulative.y) %>%
    relocate(country,tests_cumulative,new_tests,
             tests_cumulative_corrected,new_tests_corrected,date,source,status,url)

  separate_files <- merged_f %>%
    dplyr::arrange(country, date) %>%
    dplyr::group_by(date, .add =TRUE) %>%
    dplyr::group_split()


  mapply(
    readr::write_csv,
    separate_files,
    paste0(window_update, "-processed-manually.csv")
  )
}

##### function to update with one file several values in merge folder #####
# to update before 2021-02-18

update_merge_with_file <- function(f_date,#"2021-09-09"
                                   e_date,#"2021-12-26"
                                   country_update,#"ElSalvador"
                                   country_update_path#"resources/update_Iceland.csv"
                                   ) {
  today <- format(Sys.time(), "%Y-%m-%d")
  first_date <- as.Date(f_date)
  window_update <- seq(first_date, as.Date(e_date), by = "days")

  merged_sele<- sprintf(
    "https://raw.githubusercontent.com/finddx/FINDCov19TrackerData/master/automated/merged/%s-automated-tests.csv", # nolint
    window_update
  )
  merged_tests <- rio::import_list(merged_sele, rbind = TRUE) %>%
    dplyr::select(-`_file`)

  country_update_file <- readr::read_csv(country_update_path,
                             readr::cols(country=col_character(),
                                         tests_cumulative =col_integer(),
                                         new_tests =col_integer(),
                                         tests_cumulative_corrected =col_integer(),
                                         new_tests_corrected =col_integer()),
                             col_names = TRUE
  ) %>% mutate(date = data.table::as.IDate(date)) %>%
    dplyr::filter(date <= "2021-02-18")# nolint


  merged_files <- dplyr::full_join(merged_tests,
                               country_update_file,
                               by=c("country", "date"))

  merged_f <-  merged_files %>%
    mutate(tests_cumulative =
             if_else(country == country_update,
                     tests_cumulative.y,
                     tests_cumulative.x)) %>%
    mutate(new_tests =
             if_else(country == country_update,
                     new_tests.y,
                     new_tests.x)) %>%
    mutate(tests_cumulative_corrected =
             if_else(country == country_update,
                     tests_cumulative_corrected.y,
                     tests_cumulative_corrected.x)) %>%
    mutate(new_tests_corrected =
             if_else(country == country_update,
                     new_tests_corrected.y,
                     new_tests_corrected.x)) %>%
    select(-tests_cumulative.x,-tests_cumulative.y,
           -new_tests.x,-new_tests.y,
           -tests_cumulative_corrected.x,-tests_cumulative_corrected.y,
           -new_tests_corrected.x,-new_tests_corrected.y) %>%
    relocate(country,tests_cumulative,new_tests,
             tests_cumulative_corrected, new_tests_corrected,
             date, source)

  separate_files <- merged_f %>%
    dplyr::arrange(country, date) %>%
    dplyr::group_by(date, .add =TRUE) %>%
    dplyr::group_split()


  mapply(
    readr::write_csv,
    separate_files,
    paste0(window_update, "-automated-tests.csv")
  )
}

