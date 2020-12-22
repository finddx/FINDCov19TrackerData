# TODO: Add comment
#
# Author: CH
###############################################################################

################################################################################################################################################################################################################################
# Clean the environment
################################################################################################################################################################################################################################
rm(list = ls())

################################################################################################################################################################################################################################
# Load libraries
################################################################################################################################################################################################################################
library(rvest)
library(httr)
library(rdrop2)
library(stringr)
library(jsonlite)
library(rjstat)
library(readxl)
library(dplyr)
library(pdftools)
library(readr)
# library(devtools)
# library(mailR)

################################################################################################################################################################################################################################
# load functions
################################################################################################################################################################################################################################

get_status <- function(url){
  return(data.frame(url = url, response_code = html_session(url) %>% status_code()))
}

fetch_data <- function(r) {
  type <- info[[r,"type"]]
  if (!is.na(type)) {
    country <- info[[r,"country"]]
    message(country)
    if (type %in% c("csv","xlsx")) {
      data <- fetch_from_csv_xlsx(type, info[[r,"data_url"]], info[[r,"date_format"]], info[[r,"xpath_cumul"]], info[[r,"xpath_new"]], info[[r,"backlog"]])
    } else if (type == "html") {
      data <- fetch_from_html(info[[r,"source"]], info[[r,"xpath_cumul"]], info[[r,"xpath_new"]])
    } else if (type == "json") {
      data <- fetch_from_json(info[[r,"data_url"]], info[[r,"xpath_cumul"]], info[[r,"xpath_new"]])
    } else if (type == "jsonstat") {
      data <- fetch_from_jsonstat(info[[r,"data_url"]], info[[r,"xpath_cumul"]], info[[r,"xpath_new"]])
    } else if (type == "pdf") {
      data <- fetch_from_pdf(country, info[[r,"data_url"]], info[[r,"date_format"]], info[[r,"xpath_cumul"]])
    } else if (type == "pdf_list") {
      data <- fetch_from_pdf_list(info[[r,"source"]], info[[r,"data_url"]], info[[r,"xpath_cumul"]])
    } else if (type == "html2") {
      data <- fetch_from_html2(info[[r,"data_url"]], info[[r,"date_format"]], info[[r,"xpath_cumul"]])
    } else if (type == "html_list") {
      data <- fetch_from_html_list(info[[r,"source"]], info[[r,"data_url"]], info[[r,"xpath_cumul"]])
    } else if (type == "zip") {
      data <- fetch_from_zip(info[[r,"data_url"]], info[[r,"xpath_cumul"]])
    } else if (type == "Selenium") {
      data <- fetch_from_selenium(info[[r,"country"]], info[[r,"xpath_cumul"]])
    }
    return(data)
  }
  return(NA)
}

fetch_from_csv_xlsx <- function(type, url, date_format, cumul, new, backlog) {
  message(url)
  tests_cumulative <- NA
  new_tests <- NA
  backlog <- ifelse(is.na(backlog),0,as.numeric(backlog))

  if (type == "xlsx") {

    tmpfile <- tempfile("country_data", fileext = ".xlsx")

    if (!is.na(date_format)) {
      today_char <- as.character(Sys.Date(), date_format)
      yesterday_char <- as.character(Sys.Date()-1, date_format)

      tryCatch({download.file(gsub("DATE",today_char,url), destfile = tmpfile, quiet = FALSE, mode =
                                "wb")}, silent = FALSE, condition = function(err) { } )
      if (file.size(tmpfile)==0) {
        tryCatch({download.file(gsub("DATE",yesterday_char,url), destfile = tmpfile, quiet = FALSE, mode =
                                  "wb")}, silent = FALSE, condition = function(err) { } )
        if (file.size(tmpfile)==0) {
          return(c(new_tests,tests_cumulative))
        }
      }
    } else {
      tryCatch({download.file(url, destfile = tmpfile, quiet = FALSE, mode =
                                "wb")}, silent = FALSE, condition = function(err) { } )
      if (file.size(tmpfile)==0) {
        return(c(new_tests,tests_cumulative))
      }
    }

    data <- read_excel(tmpfile, sheet = 1)
    sep <- ","

  } else if (type == "csv") {
    if (!is.na(date_format)) { #for now only Costa Rica, updated day before
      yesterday_char <- as.character(Sys.Date()-1, date_format)
      url <- gsub("DATE",yesterday_char,url)
    }
    message(url)
    seps <- c(str_extract(cumul,"[,;]"),str_extract(new,"[,;]"))
    sep <- seps[which(!is.na(seps))]
    data <- read.csv(file = url, sep= sep, stringsAsFactors = F,encoding = "UTF-8")
    data <- data[rowSums(is.na(data)|data=='') != ncol(data),]

  } else {
    return(c(new_tests,tests_cumulative))
  }

  if (!is.na(cumul)) {
    idx <- unlist(str_split(cumul,sep))
    cols <- grep(idx[[2]],names(data))
    data[,cols] <- sapply(data[,cols],as.numeric)
    type <- idx[[1]]
    if (type=="last") {
      tests_cumulative <- data[nrow(data),cols]
    } else if (type=="sum") {
      tests_cumulative <- sum(na.omit(data[,cols]))
    } else {
      tests_cumulative <- data[as.integer(type),cols]
    }
    tests_cumulative <- as.numeric(tests_cumulative)
    tests_cumulative <- tests_cumulative + backlog
  }

  if (!is.na(new)) {
    idx <- unlist(str_split(new,sep))
    cols <- grep(idx[[2]],names(data))
    data[,cols] <- sapply(data[,cols],as.numeric)
    type <- idx[[1]]
    if (type=="last") {
      new_tests <- data[nrow(data),cols]
    } else if (type=="sum") {
      new_tests <- sum(na.omit(data[,cols]))
    } else {
      new_tests <- data[as.integer(type),cols]
    }
    new_tests <- as.numeric(new_tests)
  }

  return(c(new_tests,tests_cumulative))
}

fetch_from_json <- function(url, cumul, new) {
  message(url)
  tests_cumulative <- NA
  new_tests <- NA

  getData <- httr::GET(url)
  getData_text <- httr::content(getData, "text")
  getData_json <- jsonlite::fromJSON(getData_text, flatten = TRUE)

  if (!is.na(cumul)) {
    tests_cumulative <- as.numeric(eval(parse(text = cumul)))
  }
  if (!is.na(new)) {
    new_tests <- as.numeric(eval(parse(text = new)))
  }
  return(c(new_tests,tests_cumulative))
}


is.error <- function(x) inherits(x, "try-error")

fetch_from_html <- function(url, cumul, new) {
  message(url)
  tests_cumulative <- NA
  new_tests <- NA

  page <- try(xml2::read_html(url),silent = TRUE)
  if (is.error(page)) {
    page <- try(xml2::read_html(url(url)),silent = TRUE)
    if (is.error(page)) {
      return(c(new_tests,tests_cumulative))
    }
  }
  if (!is.na(cumul)) {
    text <- page %>% rvest::html_node(xpath = cumul) %>% rvest::html_text()
    tests_cumulative <- as.numeric(gsub("[^0-9]","",text))
  }
  if (!is.na(new)) {
    text <- page %>% rvest::html_node(xpath = new) %>% rvest::html_text()
    new_tests <- as.numeric(gsub("[^0-9]","",text))
  }
  return(c(new_tests,tests_cumulative))
}

fetch_from_pdf <- function(country, url, date_format, pattern) {
  message(url)
  tests_cumulative <- NA
  new_tests <- NA

  tmpfile <- tempfile("country_data", fileext = ".pdf")

  if (is.na(date_format)) {
    tryCatch({download.file(url, destfile = tmpfile, quiet = FALSE, mode =
                              "wb")}, silent = FALSE, condition = function(err) { } )
    if (file.size(tmpfile)==0) {
      return(c(new_tests,tests_cumulative))
    }

  } else {
    today_char <- ifelse(grepl("%B",date_format)&country=="Afghanistan",str_to_lower(as.character(Sys.Date(), date_format)),
                         as.character(Sys.Date(), date_format))
    yesterday_char <- ifelse(grepl("%B",date_format)&country=="Afghanistan",str_to_lower(as.character(Sys.Date()-1, date_format)),
                             as.character(Sys.Date()-1, date_format))

    tryCatch({download.file(gsub("DATE",today_char,url), destfile = tmpfile, quiet = FALSE, mode =
                              "wb")}, silent = FALSE, condition = function(err) { } )
    if (file.size(tmpfile)==0) {
      tryCatch({download.file(gsub("DATE",yesterday_char,url), destfile = tmpfile, quiet = FALSE, mode =
                                "wb")}, silent = FALSE, condition = function(err) { } )
      if (file.size(tmpfile)==0) {
        return(c(new_tests,tests_cumulative))
      }
    }
  }
  content <- pdf_text(tmpfile)
  tests_cumulative <- as.numeric(gsub("[, .]","",unique(gsub(pattern,"\\1",na.omit(str_extract(content,pattern))))))

  return(c(new_tests,tests_cumulative))
}

fetch_from_pdf_list <- function(url, pattern_url, pattern_content) {
  message(url)
  tests_cumulative <- NA
  new_tests <- NA

  page <- xml2::read_html(url)
  hrefs <- rvest::html_attr(rvest::html_nodes(page, "a"), "href")

  pdfs <- grep(pattern_url, hrefs, ignore.case = T, value=T)

  pdf <- pdfs[1]

  content <- pdf_text(pdf)
  tests_cumulative <- as.numeric(gsub("[, .]","",unique(gsub(pattern_content,"\\1",na.omit(str_extract(content,pattern_content))))))

  return(c(new_tests,tests_cumulative))
}

fetch_from_html_list <- function(url_list, pattern_url, pattern_content) {
  message(url_list)
  tests_cumulative <- NA
  new_tests <- NA

  page <- xml2::read_html(url_list)
  hrefs <- rvest::html_attr(rvest::html_nodes(page, "a"), "href")

  urls <- grep(pattern_url, hrefs, ignore.case = T, value=T)

  url <- urls[1]

  content <- xml2::read_html(url) %>% rvest::html_text()
  tests_cumulative <- as.numeric(gsub("[, .]","",unique(gsub(pattern_content,"\\1",na.omit(str_extract(content,pattern_content))))))

  return(c(new_tests,tests_cumulative))
}

fetch_from_html2 <- function(url, date_format, pattern) {
  message(url)
  tests_cumulative <- NA
  new_tests <- NA

  if (!is.na(date_format)) {
    today_char <- as.character(Sys.Date(), date_format)
    yesterday_char <- as.character(Sys.Date()-1, date_format)

    page <- try(xml2::read_html(gsub("DATE",today_char,url)),silent = TRUE)
    if (is.error(page)) {
      page <- try(xml2::read_html(gsub("DATE",yesterday_char,url)),silent = TRUE)
      if (is.error(page)) {
        return(c(new_tests,tests_cumulative))
      }
    }

  } else {
    page <- try(xml2::read_html(url),silent = TRUE)
    if (is.error(page)) {
      page <- try(xml2::read_html(url(url)),silent = TRUE)
      if (is.error(page)) {
        return(c(new_tests,tests_cumulative))
      }
    }

  }
  content <- page %>% rvest::html_text()
  tests_cumulative <- as.numeric(gsub("[, .]","",unique(gsub(pattern,"\\1",na.omit(str_extract(content,pattern))))))

  return(c(new_tests,tests_cumulative))
}

fetch_from_zip <- function(url, cumul) {
  message(url)
  tests_cumulative <- NA
  new_tests <- NA

  tmpfile <- tempfile("country_data", fileext = ".zip")
  tryCatch({download.file(url, destfile = tmpfile, quiet = FALSE, mode =
                            "wb")}, silent = FALSE, condition = function(err) { } )

  if (file.size(tmpfile)>0) {
    file <- unzip(tmpfile)
    data <- read.csv(file)
    unlink(file)

    if (cumul=="nrow") {
      tests_cumulative <- nrow(data)
    }
  }

  return(c(new_tests,tests_cumulative))
}

fetch_from_selenium <- function(country, pattern) {
  tests_cumulative <- NA
  new_tests <- NA

  today <- Sys.Date()
  today_str <- as.character(today,format="%Y%m%d")

  country_to_grep <- country
  if (country == "Cape Verde") {
    country_to_grep <- "Cabo Verde"
  } else if (country == "The Gambia") {
    country_to_grep <- "Gambia"
  } else if (country == "United Republic of Tanzania") {
    country_to_grep <- "Tanzania"
  }
  line <- grep(paste0("echo: ",country_to_grep,";"),readLines(paste0("output_selenium_",today_str,".txt"),encoding = "UTF-8"),value = T)
  message(line)
  if (length(line)>0) {
    content <- gsub(paste0("echo: ",country_to_grep,";"),"",line)
    tests_cumulative <- as.numeric(gsub("[, .]","",gsub(pattern,"\\1",str_extract(content, pattern))))
  }

  return(c(new_tests,tests_cumulative))
}


################################################################################################################################################################################################################################
# get current data from dropbox
################################################################################################################################################################################################################################

# Load the Dropbox access info
# load(file = paste0("token_Covid19.rds"))

today <- Sys.Date()
today_str <- as.character(today,format="%Y%m%d")
yesterday <- today-1
yesterday_str <- as.character(yesterday,format="%Y%m%d")

# DB_dir <- 'FIND_Cov_19_Tracker/input_data/'
#DB_dir <- 'FIND_Cov_19_Tracker/test_CH'

filename <- paste0('https://raw.githubusercontent.com/dsbbfinddx/FINDCov19TrackerData/master/raw/','coronavirus_tests_',yesterday_str,'_sources_SO.csv')

cv_tests <- suppressWarnings(
  readr::read_delim(filename, col_types = readr::cols(),
  delim = ";")
)

# cv_tests <- drop_read_csv(file = filename, dtoken = token, sep=";", stringsAsFactors = F)
head(cv_tests)
cv_tests$date <- as.Date(cv_tests$date, tryFormats = c("%d.%m.%y", "%d/%m/%Y", "%Y/%m/%d", "%Y-%m-%d"))
cv_tests$new_tests <- as.numeric(cv_tests$new_tests)
cv_tests$tests_cumulative <- as.numeric(cv_tests$tests_cumulative)
if (any(is.na(cv_tests$tests_cumulative))) {
  id <- which(is.na(cv_tests$tests_cumulative))
  if (length(id)==1 & cv_tests[id,"country"]=="Malta" & cv_tests[id,"date"] == "2020-07-05") {
    message("warning: replace Malta number...")
    cv_tests[id,"tests_cumulative"] <- 100000 #replace 1,00E+05-this error is back every day!!
  }
}
countries <- unique(cv_tests$country)
cv_tests <- as.data.frame(cv_tests)
################################################################################################################################################################################################################################
# get urls file
################################################################################################################################################################################################################################

#info <- read.xlsx("coronavirus_tests_countries_urls_CH.xlsx", sheetIndex = 1, encoding="UTF-8", stringsAsFactors = F)
info <- read_xlsx("coronavirus_tests_countries_urls_CH_v7.xlsx", sheet = 1)
head(info)

################################################################################################################################################################################################################################
# fetch new data
################################################################################################################################################################################################################################

new_data <- cv_tests[0,]

nr = 0
lapply(1:nrow(info),function(r){
  
  country <- info[[r,"country"]]
  message(country)
  data <- fetch_data(r)
  if (length(data)>1) {
    message(paste(country,data[1],data[2],sep=","))
    nr <<- nr+1
    new_data[nr, ] <<- c(NA,country,NA,data[1],data[2],info[[r,"jhu_ID"]],info[[r,"source"]],NA, data[1],data[2])
  }
})
new_data$new_tests <- as.numeric(new_data$new_tests)
new_data$tests_cumulative <- as.numeric(new_data$tests_cumulative)
new_data$new_tests_corrected <- as.numeric(new_data$new_tests)
new_data$tests_cumulative_corrected <- as.numeric(new_data$tests_cumulative)


new_data$date <- today
new_data <- unique(new_data)


################################################################################################################################################################################################################################
# compute new_tests from yesterday data
################################################################################################################################################################################################################################

yesterday_data <- subset(cv_tests, date == yesterday)

#compute tests_cumulative when only new_tests is fetch (currently Philipines)
new_data$tests_cumulative <- ifelse(!is.na(new_data$new_tests)&is.na(new_data$tests_cumulative),
                                    as.numeric(yesterday_data$tests_cumulative[match(new_data$country,yesterday_data$country)])+as.numeric(new_data$new_tests),
                                    new_data$tests_cumulative)

#compute new_tests if not fecth
new_data$new_tests <- ifelse(!is.na(new_data$tests_cumulative)&is.na(new_data$new_tests),
                             new_data$tests_cumulative-yesterday_data$tests_cumulative[match(new_data$country,yesterday_data$country)],
                             new_data$new_tests)

#new countries, new_tests = tests_cumulative
new_countries <- setdiff(new_data$country,unique(yesterday_data$country))
for (c in new_countries) {
  r <- which(new_data$country==c)
  message("New country: ",c,new_data$tests_cumulative[r])
  new_data$new_tests[r] <- new_data$tests_cumulative[r]
}

################################################################################################################################################################################################################################
# save today data
################################################################################################################################################################################################################################

new_data$ind <- ifelse(is.na(new_data$tests_cumulative)&is.na(new_data$new_tests),"couldn't fetch new data",NA)
new_data$neg <- ifelse(new_data$new_tests < 0, 'Negative new test value', NA)


not_fetched_neg_new_tests <- subset(new_data, neg == 'Negative new test value'
                                    | ind == "couldn't fetch new data")


write.csv(new_data, paste0('coronavirus_tests_',today_str,'_newdata_SO.csv'), row.names = FALSE, na = "")


# if(nrow(neg_new_tests)>0){
#   send.mail(from = "anna.mantsoki@finddx.org",
#             to = c("anna.mantsoki@finddx.org", "Imane.ElIdrissi@finddx.org"),
#             subject = "Negative values on new tests",
#             body = paste0("There are ", nrow(cv_test_new_neg), 'new tests values in the coronavirus_tests.csv file'),
#             attach.files = c(paste0('coronavirus_tests_',today_str,'_newdata_SO.csv')),
#             smtp = list(host.name = "aspmx.l.google.com", port = 25),
#             authenticate = FALSE,
#             send = TRUE)
# }



################################################################################################################################################################################################################################
# prepare new file
################################################################################################################################################################################################################################

cv_tests_new <- cv_tests

#adds a new line per country with updated date
for (i in 1:length(countries)) {
  td <- subset(cv_tests_new, country == countries[i])
  new_line <- td[nrow(td), ]
  new_line$date <- new_line$date + 1
  fetch <- which(new_data$country == countries[i] & new_data$date == new_line$date)
  if (any(length(fetch)==0, is.na(new_data$new_tests[fetch]))) {
    new_line$new_tests <- 0
    new_line$new_tests_corrected <- 0
  } else {
    new_line$new_tests <- new_data$new_tests[fetch]
    new_line$tests_cumulative <- new_data$tests_cumulative[fetch]
    new_line$source <- new_data$source[fetch]
    new_line$new_tests_corrected <- new_data$new_tests[fetch]
    new_line$tests_cumulative_corrected <- new_data$tests_cumulative[fetch]
  }
  cv_tests_new <- rbind(cv_tests_new, new_line)
}

#add new countries
setdiff(new_data$country,countries)
new_countries <- setdiff(new_data$country,countries)
new_countries_data <-  subset(new_data, `country` %in% new_countries)
cv_tests_new <- rbind(cv_tests_new, new_countries_data)

#sort by country and date
cv_tests_new <- cv_tests_new[
  order( cv_tests_new[,2], cv_tests_new[,3] ),
  ]

filename <- paste0('coronavirus_tests_',today_str,'_sources_SO.csv')

if (file.exists(filename)) {
  time <- format(file.info(filename)$mtime, format="%H%M")
  today_str_time <- paste0(today_str,"_",time)

  filename_saveold <- gsub(today_str,today_str_time,filename)

  file.copy(filename, filename_saveold, copy.date = TRUE)
  message("saved a copy of current ongoing data as ",filename_saveold)

  ongoing <- read.csv(filename, stringsAsFactors = F)
  ongoing$date <- as.Date(ongoing$date, tryFormats = c("%d.%m.%y", "%d/%m/%Y", "%Y/%m/%d", "%Y-%m-%d"))

  lapply(1:nrow(new_data),function(r){
    if (!is.na(new_data$new_tests[r])) {
      idx <- which(ongoing$country == new_data$country[r] & ongoing$date == new_data$date[r])
      if (ongoing$new_tests[idx]==0 & new_data$new_tests[r]>0) {
        ongoing[idx, ] <<- new_data[r, ]
      }
    }
  })
  write.csv(ongoing, filename, row.names = FALSE, na = "")
  message("new updated data saved as ",filename)

} else {
  #save to new file

  write.csv(cv_tests_new, filename, row.names = FALSE, na = "")
  message("new file created as ",filename)
}
