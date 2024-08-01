from selenium import webdriver
from selenium.webdriver.safari.options import Options

def get_safari_driver():
    options = Options()
    driver = webdriver.Safari(options=options)
    return driver
