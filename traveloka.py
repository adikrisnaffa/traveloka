import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

driver = webdriver.Chrome(options=options) 
driver.maximize_window()
driver.get("https://www.traveloka.com/en-id")


def test_car_product():
    car_product = driver.find_element(By.XPATH, "//div[contains(text(),'Car Rental')]")
    car_product.click()

    witouth_driver = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//h4[contains(text(),'Without Driver')]")))
    witouth_driver.click()

    input_location = driver.find_element(By.XPATH, "//input[@data-testid='rental-search-form-location-input']")
    input_location.click()
    input_location.send_keys('Jakarta')
    time.sleep(5)
    choose_location = driver.find_element(By.XPATH, "//div[contains(text(),'Jakarta Special Capital Region, Indonesia')]")
    actions = ActionChains(driver)
    actions.move_to_element(choose_location).click().perform()
    time.sleep(5)

    driver.execute_script("arguments[0].removeAttribute('readonly')", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@data-testid='rental-search-form-date-input-start']"))))
    pickup_date = driver.find_element(By.XPATH, "//input[@data-testid='rental-search-form-date-input-start']")
    pickup_date.send_keys("14 March 2024")
    pickup_date_text = pickup_date.get_attribute("value")
    print("Teks dari elemen input adalah:", pickup_date_text)

    # tanggal_yang_diinginkan = driver.find_element(By.XPATH, "//div[@data-testid='date-cell-16-2-2024']")

    # actions = ActionChains(driver)
    # actions.move_to_element(tanggal_yang_diinginkan).click().perform()

    # pickup_time = driver.find_element(By.XPATH, "//input[@data-testid='rental-search-form-time-input-start']")
    # pickup_time.click
    # pickup_time.send_keys("9-0")

    # dropOff_date = driver.find_element(By.XPATH, "//input[@data-testid='rental-search-form-date-input-end']")
    # dropOff_date.click()
    # dropOff_date.send_keys("19-2-2024")  

    # dropOff_time = driver.find_element(By.XPATH, "//input[@data-testid='rental-search-form-time-input-start']")
    # dropOff_time.click
    # dropOff_time.send_keys("11-0")
    
    time.sleep(10)