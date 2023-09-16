from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class DriverManager:

    @staticmethod
    def get_driver(browser_name='chrome'):
        if browser_name.lower() == 'chrome':
            option = webdriver.ChromeOptions()
            return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)
        else:
            raise ValueError(f"Unsupported browser: {browser_name}")

    @staticmethod
    def maximized_window(driver):
        driver.maximize_window()

