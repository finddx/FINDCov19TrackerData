# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from datetime import date
import unittest

class TestDefaultSuite(unittest.TestCase):
  def setUp(self):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    # Required for test_france() to work
    # https://stackoverflow.com/questions/51220794/selenium-not-working-in-headless-mode
    # https://sqa.stackexchange.com/questions/33778/chromedriver-in-headless-mode-doesnt-work-correctly-because-of-windows-user-pol
    chrome_options.add_argument("--window-size=1920,1080")
    self.driver = webdriver.Chrome(chrome_options=chrome_options)
    #self.driver = webdriver.Chrome()
    self.vars = {}
    # FIXME: The data needs to be included
    # self.vars["date"] = date.today().strftime("%Y-%m-%d")

  def tearDown(self):
    self.driver.quit()

  def test_australia(self):
    # Test name: Australia
    # Step # | name | target | value
    # 1 | open | https://www.health.gov.au/resources/total-covid-19-tests-conducted-and-results |
    self.driver.get("https://www.health.gov.au/resources/total-covid-19-tests-conducted-and-results")
    # 2 | waitForElementNotPresent | css=.ng-scope:nth-child(1) > .ng-binding:nth-child(2) | 30000
    WebDriverWait(self.driver, 30000).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".ng-scope:nth-child(1) > .ng-binding:nth-child(2)")))
    # 3 | storeText | css=.ng-scope:nth-child(1) > .ng-binding:nth-child(2) | tests
    self.vars["tests_cumulative"] = self.driver.find_element(By.CSS_SELECTOR, ".ng-scope:nth-child(1) > .ng-binding:nth-child(2)").text
    # 4 | close |  |
    self.driver.close()

  def test_bosniaandHerzegovina(self):
    # Test name: BosniaandHerzegovina
    # Step # | name | target | value
    # 1 | open | https://covid-19.ba/ |
    self.driver.get("https://covid-19.ba/")
    # 2 | waitForElementVisible | id=total_tested_positive | 300000
    WebDriverWait(self.driver, 30000).until(expected_conditions.visibility_of_element_located((By.ID, "total_tested_positive")))
    # 3 | storeText | id=total_tested_positive | tests
    self.vars["tests_cumulative"] = self.driver.find_element(By.ID, "total_tested_positive").text
    # 4 | close |  |
    self.driver.close()

  def test_brunei(self):
    # Test name: Brunei
    # Step # | name | target | value
    # 1 | open | http://www.moh.gov.bn/Lists/Latest%20news/AllItems.aspx |
    self.driver.get("http://www.moh.gov.bn/Lists/Latest%20news/AllItems.aspx")
    # 2 | click | css=.ms-listlink:nth-of-type(1) |
    self.driver.find_element(By.CSS_SELECTOR, ".ms-listlink:nth-of-type(1)").click()
    # 3 | waitForElementVisible | css=.ms-rteTable-default:nth-child(17) .ms-rteTable-default:nth-child(2) > strong | 300000
    WebDriverWait(self.driver, 30000).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".ms-rteTable-default:nth-child(17) .ms-rteTable-default:nth-child(2) > strong")))
    # 4 | storeText | css=.ms-rteTable-default:nth-child(17) .ms-rteTable-default:nth-child(2) > strong | tests
    self.vars["tests_cumulative"] = self.driver.find_element(By.CSS_SELECTOR, ".ms-rteTable-default:nth-child(17) .ms-rteTable-default:nth-child(2) > strong").text
    # 5 | close |  |
    self.driver.close()

  def test_bulgaria(self):
    # Test name: Bulgaria
    # Step # | name | target | value
    # 1 | open | https://coronavirus.bg/ |
    self.driver.get("https://coronavirus.bg/")
    # 2 | waitForElementVisible | css=.col-lg-3:nth-child(1) > .statistics-value | 300000
    WebDriverWait(self.driver, 30000).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".col-lg-3:nth-child(1) > .statistics-value")))
    # 3 | storeText | css=.col-lg-3:nth-child(1) > .statistics-value | tests
    self.vars["tests_cumulative"] = self.driver.find_element(By.CSS_SELECTOR, ".col-lg-3:nth-child(1) > .statistics-value").text
    # 4 | close |  |
    self.driver.close()

  def test_canada(self):
    # Test name: Canada
    # Step # | name | target | value
    # 1 | open | https://health-infobase.canada.ca/covid-19/epidemiological-summary-covid-19-cases.html |
    self.driver.get("https://health-infobase.canada.ca/covid-19/epidemiological-summary-covid-19-cases.html")
    # 2 | waitForElementVisible | css=.numTested | 300000
    WebDriverWait(self.driver, 30000).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".numTested")))
    # 3 | storeText | css=.numTested | tests
    self.vars["tests_cumulative"] = self.driver.find_element(By.CSS_SELECTOR, ".numTested").text
    # 4 | close |  |
    self.driver.close()

  def test_estonia(self):
    # Test name: Estonia
    # Step # | name | target | value
    # 1 | open | https://koroonakaart.ee/et |
    self.driver.get("https://koroonakaart.ee/et")
    # 2 | waitForElementVisible | css=.row:nth-child(2) > .statsbar-item:nth-child(4) > h1 | 30000
    WebDriverWait(self.driver, 30000).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".row:nth-child(2) > .statsbar-item:nth-child(4) > h1")))
    # 3 | storeText | css=.row:nth-child(2) > .statsbar-item:nth-child(4) > h1 | tests
    self.vars["tests_cumulative"] = self.driver.find_element(By.CSS_SELECTOR, ".row:nth-child(2) > .statsbar-item:nth-child(4) > h1").text
    # 4 | close |  |
    self.driver.close()

  def test_france(self):
    # Test name: France
    # Step # | name | target | value
    # 1 | open | https://dashboard.covid19.data.gouv.fr/suivi-des-tests?location=FRA |
    self.driver.get("https://dashboard.covid19.data.gouv.fr/suivi-des-tests?location=FRA")
    # 2 | waitForElementVisible | css=.counter-container > .jsx-792689997 | 300000
    WebDriverWait(self.driver, 30000).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".counter-container > .jsx-792689997")))
    # 3 | storeText | css=.counter-container > .jsx-792689997 | tests
    self.vars["tests_cumulative"] = self.driver.find_element(By.CSS_SELECTOR, ".counter-container > .jsx-792689997").text
    # 4 | close |  |
    self.driver.close()

  def test_hungary(self):
    # Test name: Hungary
    # Step # | name | target | value
    # 1 | open | https://koronavirus.gov.hu/#aktualis |
    self.driver.get("https://koronavirus.gov.hu/#aktualis")
    # 2 | waitForElementVisible | id=content-mintavetel | 300000
    WebDriverWait(self.driver, 30000).until(expected_conditions.visibility_of_element_located((By.ID, "content-mintavetel")))
    # 3 | storeText | id=content-mintavetel | tests
    self.vars["tests_cumulative"] = self.driver.find_element(By.ID, "content-mintavetel").text
    # 4 | close |  |
    self.driver.close()

  def test_india(self):
    # Test name: India
    # Step # | name | target | value
    # 1 | open | https://www.icmr.gov.in/ |
    self.driver.get("https://www.icmr.gov.in/")
    # 2 | waitForElementVisible | css=.col-12:nth-child(1) > .single-cool-fact h2 | 300000
    WebDriverWait(self.driver, 30000).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".col-12:nth-child(1) > .single-cool-fact h2")))
    # 3 | storeText | css=.col-12:nth-child(1) > .single-cool-fact h2 | tests
    self.vars["tests_cumulative"] = self.driver.find_element(By.CSS_SELECTOR, ".col-12:nth-child(1) > .single-cool-fact h2").text
    # 4 | close |  |
    self.driver.close()

  def test_ireland(self):
    # Test name: Ireland
    # Step # | name | target | value
    # 1 | open | https://covid19ireland-geohive.hub.arcgis.com/pages/hospitals-icu--testing |
    self.driver.get("https://covid19ireland-geohive.hub.arcgis.com/pages/hospitals-icu--testing")
    # 2 | waitForElementVisible | css=#ember142 .ss-value | 300000
    WebDriverWait(self.driver, 30000).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "#ember142 .ss-value")))
    # 3 | storeText | css=#ember142 .ss-value | tests
    self.vars["tests_cumulative"] = self.driver.find_element(By.CSS_SELECTOR, "#ember142 .ss-value").text
    # 4 | close |  |
    self.driver.close()

  def test_latvia(self):
    # Test name: Latvia
    # Step # | name | target | value
    # 1 | open | https://infogram.com/covid-19-izplatiba-latvija-1hzj4ozwvnzo2pw |
    self.driver.get("https://infogram.com/covid-19-izplatiba-latvija-1hzj4ozwvnzo2pw")
    # 2 | waitForElementVisible | css=.InfographicEditor-Contents-Item:nth-child(11) .igc-textual-figure > div | 300000
    WebDriverWait(self.driver, 30000).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".InfographicEditor-Contents-Item:nth-child(11) .igc-textual-figure > div")))
    # 3 | storeText | css=.InfographicEditor-Contents-Item:nth-child(11) .igc-textual-figure > div | tests
    self.vars["tests_cumulative"] = self.driver.find_element(By.CSS_SELECTOR, ".InfographicEditor-Contents-Item:nth-child(11) .igc-textual-figure > div").text
    # 4 | close |  |
    self.driver.close()

  def test_lithuania(self):
    # Test name: Lithuania
    # Step # | name | target | value
    # 1 | open | https://osp.stat.gov.lt/praejusios-paros-covid-19-statistika |
    self.driver.get("https://osp.stat.gov.lt/praejusios-paros-covid-19-statistika")
    # 2 | waitForElementVisible | css=tr:nth-child(13) > td:nth-child(1) span > span | 300000
    WebDriverWait(self.driver, 30000).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "tr:nth-child(13) > td:nth-child(1) span > span")))
    # 3 | storeText | css=tr:nth-child(13) > td:nth-child(1) span > span | tests
    self.vars["tests_cumulative"] = self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(13) > td:nth-child(1) span > span").text
    # 4 | close |  |
    self.driver.close()

  def test_nepal(self):
    # Test name: Nepal
    # Step # | name | target | value
    # 1 | open | https://covid19.mohp.gov.np/ |
    self.driver.get("https://covid19.mohp.gov.np/")
    # 2 | waitForElementVisible | css=.ant-col-md-24 .ant-typography:nth-child(2) | 300000
    WebDriverWait(self.driver, 30000).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".ant-col-md-24 .ant-typography:nth-child(2)")))
    # 3 | storeText | css=.ant-col-md-24 .ant-typography:nth-child(2) | tests
    self.vars["tests_cumulative"] = self.driver.find_element(By.CSS_SELECTOR, ".ant-col-md-24 .ant-typography:nth-child(2)").text
    # 4 | close |  |
    self.driver.close()

  def test_newZealand(self):
    # Test name: NewZealand
    # Step # | name | target | value
    # 1 | open | https://www.health.govt.nz/our-work/diseases-and-conditions/covid-19-novel-coronavirus/covid-19-data-and-statistics/covid-19-testing-data |
    self.driver.get("https://www.health.govt.nz/our-work/diseases-and-conditions/covid-19-novel-coronavirus/covid-19-data-and-statistics/covid-19-testing-data")
    # 2 | waitForElementVisible | css=.table-responsive:nth-child(9) tr:nth-child(1) > td | 300000
    WebDriverWait(self.driver, 30000).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".table-responsive:nth-child(9) tr:nth-child(1) > td")))
    # 3 | storeText | css=.table-responsive:nth-child(9) tr:nth-child(1) > td | tests
    self.vars["tests_cumulative"] = self.driver.find_element(By.CSS_SELECTOR, ".table-responsive:nth-child(9) tr:nth-child(1) > td").text
    # 4 | close |  |
    self.driver.close()

  def test_northMacedonia(self):
    # Test name: NorthMacedonia
    # Step # | name | target | value
    # 1 | open | https://datastudio.google.com/embed/u/0/reporting/9f5104d0-12fd-4e16-9a11-993685cfd40f/page/1M |
    self.driver.get("https://datastudio.google.com/embed/u/0/reporting/9f5104d0-12fd-4e16-9a11-993685cfd40f/page/1M")
    # 2 | waitForElementVisible | css=.cd-vmd90p9a8b .valueLabel | 30000
    WebDriverWait(self.driver, 30000).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".cd-vmd90p9a8b .valueLabel")))
    # 3 | storeText | css=.cd-vmd90p9a8b .valueLabel | tests
    self.vars["tests_cumulative"] = self.driver.find_element(By.CSS_SELECTOR, ".cd-vmd90p9a8b .valueLabel").text
    # 4 | close |  |
    self.driver.close()

  def test_norway(self):
    # Test name: Norway
    # Step # | name | target | value
    # 1 | open | https://www.fhi.no/en/id/infectious-diseases/coronavirus/daily-reports/daily-reports-COVID19/ |
    self.driver.get("https://www.fhi.no/en/id/infectious-diseases/coronavirus/daily-reports/daily-reports-COVID19/")
    # 2 | waitForElementVisible | css=.c-key-figure:nth-child(1) .c-key-figure__number > span | 300000
    WebDriverWait(self.driver, 30000).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".c-key-figure:nth-child(1) .c-key-figure__number > span")))
    # 3 | storeText | css=.c-key-figure:nth-child(1) .c-key-figure__number > span | tests
    self.vars["tests_cumulative"] = self.driver.find_element(By.CSS_SELECTOR, ".c-key-figure:nth-child(1) .c-key-figure__number > span").text
    # 4 | close |  |
    self.driver.close()

  def test_occupiedPalestinianterritory(self):
    # Test name: occupiedPalestinianterritory
    # Step # | name | target | value
    # 1 | open | https://corona.ps/ |
    self.driver.get("https://corona.ps/")
    # 2 | waitForElementVisible | css=.roundbox:nth-child(1) > div:nth-child(2) | 300000
    WebDriverWait(self.driver, 30000).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".roundbox:nth-child(1) > div:nth-child(2)")))
    # 3 | storeText | css=.roundbox:nth-child(1) > div:nth-child(2) | tests
    self.vars["tests_cumulative"] = self.driver.find_element(By.CSS_SELECTOR, ".roundbox:nth-child(1) > div:nth-child(2)").text
    # 4 | close |  |
    self.driver.close()

  def test_qatar(self):
    # Test name: Qatar
    # Step # | name | target | value
    # 1 | open | https://covid19.moph.gov.qa/EN/Pages/default.aspx# |
    self.driver.get("https://covid19.moph.gov.qa/EN/Pages/default.aspx#")
    # 2 | waitForElementVisible | id=strgPeopleTested | 30000
    WebDriverWait(self.driver, 30000).until(expected_conditions.visibility_of_element_located((By.ID, "strgPeopleTested")))
    # 3 | storeText | id=strgPeopleTested | tests
    self.vars["tests_cumulative"] = self.driver.find_element(By.ID, "strgPeopleTested").text
    # 4 | close |  |
    self.driver.close()

  def test_republicofKorea(self):
    # Test name: RepublicofKorea
    # Step # | name | target | value
    # 1 | open | http://ncov.mohw.go.kr/en/ |
    self.driver.get("http://ncov.mohw.go.kr/en/")
    # 2 | waitForElementVisible | css=li:nth-child(1) > .misil_r > span | 300000
    WebDriverWait(self.driver, 30000).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "li:nth-child(1) > .misil_r > span")))
    # 3 | storeText | css=li:nth-child(1) > .misil_r > span | tests
    self.vars["tests_cumulative"] = self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(1) > .misil_r > span").text
    # 4 | close |  |
    self.driver.close()

  def test_southAfrica(self):
    # Test name: SouthAfrica
    # Step # | name | target | value
    # 1 | open | https://gis.nicd.ac.za/portal/apps/opsdashboard/index.html#/0ec12f471aaa4055999366669b38482d |
    self.driver.get("https://gis.nicd.ac.za/portal/apps/opsdashboard/index.html#/0ec12f471aaa4055999366669b38482d")
    # 2 | waitForElementVisible | css=#ember232 text | 300000
    WebDriverWait(self.driver, 30000).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "#ember232 text")))
    # 3 | storeText | css=#ember232 text | tests
    self.vars["tests_cumulative"] = self.driver.find_element(By.CSS_SELECTOR, "#ember232 text").text
    # 4 | close |  |
    self.driver.close()

  def test_singapore(self):
    # Test name: Singapore
    # Step # | name | target | value
    # 1 | open | https://www.moh.gov.sg/covid-19 |
    self.driver.get("https://www.moh.gov.sg/covid-19")
    # 2 | waitForElementVisible | css=#ContentPlaceHolder_contentPlaceholder_C095_Col00 b | 300000
    WebDriverWait(self.driver, 30000).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "#ContentPlaceHolder_contentPlaceholder_C095_Col00 b")))
    # 3 | storeText | css=#ContentPlaceHolder_contentPlaceholder_C095_Col00 b | tests
    self.vars["tests_cumulative"] = self.driver.find_element(By.CSS_SELECTOR, "#ContentPlaceHolder_contentPlaceholder_C095_Col00 b").text
    # 4 | close |  |
    self.driver.close()

  def test_slovakia(self):
    # Test name: Slovakia
    # Step # | name | target | value
    # 1 | open | https://korona.gov.sk/ |
    self.driver.get("https://korona.gov.sk/")
    # 2 | waitForElementVisible | css=#block_5e9990e25ffff .govuk-heading-l | 300000
    WebDriverWait(self.driver, 30000).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "#block_5e9990e25ffff .govuk-heading-l")))
    # 3 | storeText | css=#block_5e9990e25ffff .govuk-heading-l | tests
    self.vars["tests_cumulative"] = self.driver.find_element(By.CSS_SELECTOR, "#block_5e9990e25ffff .govuk-heading-l").text
    # 4 | close |  |
    self.driver.close()

  def test_sriLanka(self):
    # Test name: SriLanka
    # Step # | name | target | value
    # 1 | open | https://www.hpb.health.gov.lk/en |
    self.driver.get("https://www.hpb.health.gov.lk/en")
    # 2 | waitForElementVisible | css=.total-count | 300000
    WebDriverWait(self.driver, 30000).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".total-count")))
    # 3 | storeText | css=.total-count | tests
    self.vars["tests_cumulative"] = self.driver.find_element(By.CSS_SELECTOR, ".total-count").text
    # 4 | close |  |
    self.driver.close()

  def test_turkey(self):
    # Test name: Turkey
    # Step # | name | target | value
    # 1 | open | https://covid19.saglik.gov.tr/ |
    self.driver.get("https://covid19.saglik.gov.tr/")
    # 2 | waitForElementVisible | css=.toplam-test-sayisi | 300000
    WebDriverWait(self.driver, 30000).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".toplam-test-sayisi")))
    # 3 | storeText | css=.toplam-test-sayisi | tests
    self.vars["tests_cumulative"] = self.driver.find_element(By.CSS_SELECTOR, ".toplam-test-sayisi").text
    # 4 | close |  |
    self.driver.close()

  def test_unitedArabEmirates(self):
    # Test name: UnitedArabEmirates
    # Step # | name | target | value
    # 1 | open | https://fcsa.gov.ae/en-us/Pages/Covid19/UAE-Covid-19-Updates.aspx |
    self.driver.get("https://fcsa.gov.ae/en-us/Pages/Covid19/UAE-Covid-19-Updates.aspx")
    # 2 | waitForElementVisible | css=.total_tests > .numbers | 300000
    WebDriverWait(self.driver, 30000).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".total_tests > .numbers")))
    # 3 | storeText | css=.total_tests > .numbers | tests
    self.vars["tests_cumulative"] = self.driver.find_element(By.CSS_SELECTOR, ".total_tests > .numbers").text
    # 4 | close |  |
    self.driver.close()

  def test_unitedKingdom(self):
    # Test name: UnitedKingdom
    # Step # | name | target | value
    # 1 | open | https://coronavirus.data.gov.uk/testing |
    self.driver.get("https://coronavirus.data.gov.uk/testing")
    # 2 | waitForElementVisible | id=value-item-virus_tests_conducted-total-cumvirustests-1_modal | 300000
    WebDriverWait(self.driver, 30000).until(expected_conditions.visibility_of_element_located((By.ID, "value-item-virus_tests_conducted-total-cumvirustests-1_modal")))
    # 3 | storeText | id=value-item-virus_tests_conducted-total-cumvirustests-1_modal | tests
    self.vars["tests_cumulative"] = self.driver.find_element(By.ID, "value-item-virus_tests_conducted-total-cumvirustests-1_modal").text
    # 4 | close |  |
    self.driver.close()

  def test_ethiopia(self):
    self.driver.get("https://africacdc.maps.arcgis.com/apps/opsdashboard/index.html#/9d8d4add4dcb456997fd83607b5d0c7c")
    self.driver.implicitly_wait(20)
    self.driver.find_element(By.CSS_SELECTOR, "circle:nth-child(3)").click()
    self.vars["tests_cumulative"] = self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(8) .esriNumericValue").text
    self.driver.close()

  def test_kenya(self):
    self.driver.get("https://africacdc.maps.arcgis.com/apps/opsdashboard/index.html#/9d8d4add4dcb456997fd83607b5d0c7c")
    self.driver.implicitly_wait(20)
    self.driver.find_element(By.CSS_SELECTOR, "circle:nth-child(5)").click()
    self.vars["tests_cumulative"] = self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(8) .esriNumericValue").text
    self.driver.close()

  def test_libya(self):
    self.driver.get("https://africacdc.maps.arcgis.com/apps/opsdashboard/index.html#/9d8d4add4dcb456997fd83607b5d0c7c")
    self.driver.implicitly_wait(20)
    self.driver.find_element(By.CSS_SELECTOR, "circle:nth-child(6)").click()
    self.vars["tests_cumulative"] = self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(8) .esriNumericValue").text
    self.driver.close()

  def test_nigeria(self):
    self.driver.get("https://africacdc.maps.arcgis.com/apps/opsdashboard/index.html#/9d8d4add4dcb456997fd83607b5d0c7c")
    self.driver.implicitly_wait(20)
    self.driver.find_element(By.CSS_SELECTOR, "circle:nth-child(7)").click()
    self.vars["tests_cumulative"] = self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(8) .esriNumericValue").text
    self.driver.close()

  def test_ghana(self):
    self.driver.get("https://africacdc.maps.arcgis.com/apps/opsdashboard/index.html#/9d8d4add4dcb456997fd83607b5d0c7c")
    self.driver.implicitly_wait(20)
    self.driver.find_element(By.CSS_SELECTOR, "circle:nth-child(8)").click()
    self.vars["tests_cumulative"] = self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(8) .esriNumericValue").text
    self.driver.close()

  def test_uganda(self):
    self.driver.get("https://africacdc.maps.arcgis.com/apps/opsdashboard/index.html#/9d8d4add4dcb456997fd83607b5d0c7c")
    self.driver.implicitly_wait(20)
    self.driver.find_element(By.CSS_SELECTOR, "circle:nth-child(9)").click()
    self.vars["tests_cumulative"] = self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(8) .esriNumericValue").text
    self.driver.close()

  def test_cameroon(self):
    self.driver.get("https://africacdc.maps.arcgis.com/apps/opsdashboard/index.html#/9d8d4add4dcb456997fd83607b5d0c7c")
    self.driver.implicitly_wait(20)
    self.driver.find_element(By.CSS_SELECTOR, "circle:nth-child(10)").click()
    self.vars["tests_cumulative"] = self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(8) .esriNumericValue").text
    self.driver.close()

  def test_sudan(self):
    self.driver.get("https://africacdc.maps.arcgis.com/apps/opsdashboard/index.html#/9d8d4add4dcb456997fd83607b5d0c7c")
    self.driver.implicitly_wait(20)
    self.driver.find_element(By.CSS_SELECTOR, "circle:nth-child(11)").click()
    self.vars["tests_cumulative"] = self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(8) .esriNumericValue").text
    self.driver.close()

  def test_cotedivoire(self):
    self.driver.get("https://africacdc.maps.arcgis.com/apps/opsdashboard/index.html#/9d8d4add4dcb456997fd83607b5d0c7c")
    self.driver.implicitly_wait(20)
    self.driver.find_element(By.CSS_SELECTOR, "circle:nth-child(12)").click()
    self.vars["tests_cumulative"] = self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(8) .esriNumericValue").text
    self.driver.close()

  def test_zambia(self):
    self.driver.get("https://africacdc.maps.arcgis.com/apps/opsdashboard/index.html#/9d8d4add4dcb456997fd83607b5d0c7c")
    self.driver.implicitly_wait(20)
    self.driver.find_element(By.CSS_SELECTOR, "circle:nth-child(13)").click()
    self.vars["tests_cumulative"] = self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(8) .esriNumericValue").text
    self.driver.close()

  def test_senegal(self):
    self.driver.get("https://africacdc.maps.arcgis.com/apps/opsdashboard/index.html#/9d8d4add4dcb456997fd83607b5d0c7c")
    self.driver.implicitly_wait(20)
    self.driver.find_element(By.CSS_SELECTOR, "circle:nth-child(14)").click()
    self.vars["tests_cumulative"] = self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(8) .esriNumericValue").text
    self.driver.close()

  def test_angola(self):
    self.driver.get("https://africacdc.maps.arcgis.com/apps/opsdashboard/index.html#/9d8d4add4dcb456997fd83607b5d0c7c")
    self.driver.implicitly_wait(20)
    self.driver.find_element(By.CSS_SELECTOR, "circle:nth-child(16)").click()
    self.vars["tests_cumulative"] = self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(8) .esriNumericValue").text
    self.driver.close()

  def test_mauritania(self):
    self.driver.get("https://africacdc.maps.arcgis.com/apps/opsdashboard/index.html#/9d8d4add4dcb456997fd83607b5d0c7c")
    self.driver.implicitly_wait(20)
    self.driver.find_element(By.CSS_SELECTOR, "circle:nth-child(19)").click()
    self.vars["tests_cumulative"] = self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(8) .esriNumericValue").text
    self.driver.close()

  def test_gabon(self):
    self.driver.get("https://africacdc.maps.arcgis.com/apps/opsdashboard/index.html#/9d8d4add4dcb456997fd83607b5d0c7c")
    self.driver.implicitly_wait(20)
    self.driver.find_element(By.CSS_SELECTOR, "circle:nth-child(20)").click()
    self.vars["tests_cumulative"] = self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(8) .esriNumericValue").text
    self.driver.close()

  def test_rwanda(self):
    self.driver.get("https://africacdc.maps.arcgis.com/apps/opsdashboard/index.html#/9d8d4add4dcb456997fd83607b5d0c7c")
    self.driver.implicitly_wait(20)
    self.driver.find_element(By.CSS_SELECTOR, "circle:nth-child(21)").click()
    self.vars["tests_cumulative"] = self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(8) .esriNumericValue").text
    self.driver.close()

  def test_congo(self):
    self.driver.get("https://africacdc.maps.arcgis.com/apps/opsdashboard/index.html#/9d8d4add4dcb456997fd83607b5d0c7c")
    self.driver.implicitly_wait(20)
    self.driver.find_element(By.CSS_SELECTOR, "circle:nth-child(22)").click()
    self.vars["tests_cumulative"] = self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(8) .esriNumericValue").text
    self.driver.close()

  def test_malawi(self):
    self.driver.get("https://africacdc.maps.arcgis.com/apps/opsdashboard/index.html#/9d8d4add4dcb456997fd83607b5d0c7c")
    self.driver.implicitly_wait(20)
    self.driver.find_element(By.CSS_SELECTOR, "circle:nth-child(23)").click()
    self.vars["tests_cumulative"] = self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(8) .esriNumericValue").text
    self.driver.close()

  def test_mali(self):
    self.driver.get("https://africacdc.maps.arcgis.com/apps/opsdashboard/index.html#/9d8d4add4dcb456997fd83607b5d0c7c")
    self.driver.implicitly_wait(20)
    self.driver.find_element(By.CSS_SELECTOR, "circle:nth-child(24)").click()
    self.vars["tests_cumulative"] = self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(8) .esriNumericValue").text
    self.driver.close()

  def test_djibouti(self):
    self.driver.get("https://africacdc.maps.arcgis.com/apps/opsdashboard/index.html#/9d8d4add4dcb456997fd83607b5d0c7c")
    self.driver.implicitly_wait(20)
    self.driver.find_element(By.CSS_SELECTOR, "circle:nth-child(25)").click()
    self.vars["tests_cumulative"] = self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(8) .esriNumericValue").text
    self.driver.close()

  def test_equatorialguinea(self):
    self.driver.get("https://africacdc.maps.arcgis.com/apps/opsdashboard/index.html#/9d8d4add4dcb456997fd83607b5d0c7c")
    self.driver.implicitly_wait(20)
    self.driver.find_element(By.CSS_SELECTOR, "circle:nth-child(26)").click()
    self.vars["tests_cumulative"] = self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(8) .esriNumericValue").text
    self.driver.close()

  def test_centralafricanrepublic(self):
    self.driver.get("https://africacdc.maps.arcgis.com/apps/opsdashboard/index.html#/9d8d4add4dcb456997fd83607b5d0c7c")
    self.driver.implicitly_wait(20)
    self.driver.find_element(By.CSS_SELECTOR, "circle:nth-child(27)").click()
    self.vars["tests_cumulative"] = self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(8) .esriNumericValue").text
    self.driver.close()

  def test_somalia(self):
    self.driver.get("https://africacdc.maps.arcgis.com/apps/opsdashboard/index.html#/9d8d4add4dcb456997fd83607b5d0c7c")
    self.driver.implicitly_wait(20)
    self.driver.find_element(By.CSS_SELECTOR, "circle:nth-child(28)").click()
    self.vars["tests_cumulative"] = self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(8) .esriNumericValue").text
    self.driver.close()

  def test_burkinafaso(self):
    self.driver.get("https://africacdc.maps.arcgis.com/apps/opsdashboard/index.html#/9d8d4add4dcb456997fd83607b5d0c7c")
    self.driver.implicitly_wait(20)
    self.driver.find_element(By.CSS_SELECTOR, "circle:nth-child(29)").click()
    self.vars["tests_cumulative"] = self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(8) .esriNumericValue").text
    self.driver.close()
    
  def test_benin(self):
    self.driver.get("https://africacdc.maps.arcgis.com/apps/opsdashboard/index.html#/9d8d4add4dcb456997fd83607b5d0c7c")
    self.driver.implicitly_wait(20)
    self.driver.find_element(By.CSS_SELECTOR, "circle:nth-child(33)").click()
    self.vars["tests_cumulative"] = self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(8) .esriNumericValue").text
    self.driver.close()
    
  def test_burundi(self):
    self.driver.get("https://africacdc.maps.arcgis.com/apps/opsdashboard/index.html#/9d8d4add4dcb456997fd83607b5d0c7c")
    self.driver.implicitly_wait(20)
    self.driver.find_element(By.CSS_SELECTOR, "circle:nth-child(40)").click()
    self.vars["tests_cumulative"] = self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(8) .esriNumericValue").text
    self.driver.close()
  
  def test_chad(self):
    self.driver.get("https://africacdc.maps.arcgis.com/apps/opsdashboard/index.html#/9d8d4add4dcb456997fd83607b5d0c7c")
    self.driver.implicitly_wait(20)
    self.driver.find_element(By.CSS_SELECTOR, "circle:nth-child(37)").click()
    self.vars["tests_cumulative"] = self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(8) .esriNumericValue").text
    self.driver.close()
    
  def test_comoros(self):
    self.driver.get("https://africacdc.maps.arcgis.com/apps/opsdashboard/index.html#/9d8d4add4dcb456997fd83607b5d0c7c")
    self.driver.implicitly_wait(20)
    self.driver.find_element(By.CSS_SELECTOR, "circle:nth-child(42)").click()
    self.vars["tests_cumulative"] = self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(8) .esriNumericValue").text
    self.driver.close()
       
  def test_democraticrepublicofthecongo(self):
    self.driver.get("https://africacdc.maps.arcgis.com/apps/opsdashboard/index.html#/9d8d4add4dcb456997fd83607b5d0c7c")
    self.driver.implicitly_wait(20)
    self.driver.find_element(By.CSS_SELECTOR, "circle:nth-child(17)").click()
    self.vars["tests_cumulative"] = self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(8) .esriNumericValue").text
    self.driver.close()
    
  def test_eritrea(self):
    self.driver.get("https://africacdc.maps.arcgis.com/apps/opsdashboard/index.html#/9d8d4add4dcb456997fd83607b5d0c7c")
    self.driver.implicitly_wait(20)
    self.driver.find_element(By.CSS_SELECTOR, "circle:nth-child(41)").click()
    self.vars["tests_cumulative"] = self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(8) .esriNumericValue").text
    self.driver.close()
    
  def test_ghana(self):
    self.driver.get("https://africacdc.maps.arcgis.com/apps/opsdashboard/index.html#/9d8d4add4dcb456997fd83607b5d0c7c")
    self.driver.implicitly_wait(20)
    self.driver.find_element(By.CSS_SELECTOR, "circle:nth-child(8)").click()
    self.vars["tests_cumulative"] = self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(8) .esriNumericValue").text
    self.driver.close()
    
  def test_guineabissau(self):
    self.driver.get("https://africacdc.maps.arcgis.com/apps/opsdashboard/index.html#/9d8d4add4dcb456997fd83607b5d0c7c")
    self.driver.implicitly_wait(20)
    self.driver.find_element(By.CSS_SELECTOR, "circle:nth-child(35)").click()
    self.vars["tests_cumulative"] = self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(8) .esriNumericValue").text
    self.driver.close()

  def test_liberia(self):
    self.driver.get("https://africacdc.maps.arcgis.com/apps/opsdashboard/index.html#/9d8d4add4dcb456997fd83607b5d0c7c")
    self.driver.implicitly_wait(20)
    self.driver.find_element(By.CSS_SELECTOR, "circle:nth-child(38)").click()
    self.vars["tests_cumulative"] = self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(8) .esriNumericValue").text
    self.driver.close()

  def test_mali(self):
    self.driver.get("https://africacdc.maps.arcgis.com/apps/opsdashboard/index.html#/9d8d4add4dcb456997fd83607b5d0c7c")
    self.driver.implicitly_wait(20)
    self.driver.find_element(By.CSS_SELECTOR, "circle:nth-child(24)").click()
    self.vars["tests_cumulative"] = self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(8) .esriNumericValue").text
    self.driver.close()

  def test_niger(self):
    self.driver.get("https://africacdc.maps.arcgis.com/apps/opsdashboard/index.html#/9d8d4add4dcb456997fd83607b5d0c7c")
    self.driver.implicitly_wait(20)
    self.driver.find_element(By.CSS_SELECTOR, "circle:nth-child(36)").click()
    self.vars["tests_cumulative"] = self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(8) .esriNumericValue").text
    self.driver.close()

  def test_congo(self):
    self.driver.get("https://africacdc.maps.arcgis.com/apps/opsdashboard/index.html#/9d8d4add4dcb456997fd83607b5d0c7c")
    self.driver.implicitly_wait(20)
    self.driver.find_element(By.CSS_SELECTOR, "circle:nth-child(22)").click()
    self.vars["tests_cumulative"] = self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(8) .esriNumericValue").text
    self.driver.close()

  def test_saotomeandprincipe(self):
    self.driver.get("https://africacdc.maps.arcgis.com/apps/opsdashboard/index.html#/9d8d4add4dcb456997fd83607b5d0c7c")
    self.driver.implicitly_wait(20)
    self.driver.find_element(By.CSS_SELECTOR, "circle:nth-child(39)").click()
    self.vars["tests_cumulative"] = self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(8) .esriNumericValue").text
    self.driver.close()

  def test_seychelles(self):
    self.driver.get("https://africacdc.maps.arcgis.com/apps/opsdashboard/index.html#/9d8d4add4dcb456997fd83607b5d0c7c")
    self.driver.implicitly_wait(20)
    self.driver.find_element(By.CSS_SELECTOR, "circle:nth-child(44)").click()
    self.vars["tests_cumulative"] = self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(8) .esriNumericValue").text
    self.driver.close()

  def test_sierraleone(self):
    self.driver.get("https://africacdc.maps.arcgis.com/apps/opsdashboard/index.html#/9d8d4add4dcb456997fd83607b5d0c7c")
    self.driver.implicitly_wait(20)
    self.driver.find_element(By.CSS_SELECTOR, "circle:nth-child(34)").click()
    self.vars["tests_cumulative"] = self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(8) .esriNumericValue").text
    self.driver.close()

  def test_gambia(self):
    self.driver.get("https://africacdc.maps.arcgis.com/apps/opsdashboard/index.html#/9d8d4add4dcb456997fd83607b5d0c7c")
    self.driver.implicitly_wait(20)
    self.driver.find_element(By.CSS_SELECTOR, "circle:nth-child(30)").click()
    self.vars["tests_cumulative"] = self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(8) .esriNumericValue").text
    self.driver.close()

  def test_southsudan(self):
    self.driver.get("https://africacdc.maps.arcgis.com/apps/opsdashboard/index.html#/9d8d4add4dcb456997fd83607b5d0c7c")
    self.driver.implicitly_wait(20)
    self.driver.find_element(By.CSS_SELECTOR, "circle:nth-child(32)").click()
    self.vars["tests_cumulative"] = self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(8) .esriNumericValue").text
    self.driver.close()

  def test_tanzania(self):
    self.driver.get("https://africacdc.maps.arcgis.com/apps/opsdashboard/index.html#/9d8d4add4dcb456997fd83607b5d0c7c")
    self.driver.implicitly_wait(20)
    self.driver.find_element(By.CSS_SELECTOR, "circle:nth-child(43)").click()
    self.vars["tests_cumulative"] = self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(8) .esriNumericValue").text
    self.driver.close()

  def test_westernsahara(self):
    self.driver.get("https://africacdc.maps.arcgis.com/apps/opsdashboard/index.html#/9d8d4add4dcb456997fd83607b5d0c7c")
    self.driver.implicitly_wait(20)
    self.driver.find_element(By.CSS_SELECTOR, "circle:nth-child(45)").click()
    self.vars["tests_cumulative"] = self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(8) .esriNumericValue").text
    self.driver.close()

  def test_egypt(self):
    self.driver.get("https://africacdc.maps.arcgis.com/apps/opsdashboard/index.html#/9d8d4add4dcb456997fd83607b5d0c7c")
    time.sleep(20)
    continent = self.driver.find_element_by_id('Dashboard_1day_Sht1_5411_layer')
    all_countries = self.driver.find_elements_by_tag_name('circle')

    final_tests = ""
    for country in all_countries:
        try:
            country.click()
            temp_name = self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(1) > td:nth-child(2)").text
            if temp_name == 'Egypt':
                final_tests = self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(8) .esriNumericValue").text
                break
        except:
            pass

    self.vars["tests_cumulative"] = final_tests
    self.driver.close()

