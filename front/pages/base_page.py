from selenium.common import NoSuchElementException, TimeoutException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        self.driver.get(url)

    def click_element(self, locator, timeout=10):
        element = self.wait_for_element_to_be_clickable(locator, timeout)
        element.click()

    def _find(self, condition, locator, timeout, exception_message, elem_none_if_no_found=False):
        try:
            return WebDriverWait(self.driver, timeout).until(condition(locator))
        except (NoSuchElementException, TimeoutException, StaleElementReferenceException):
            if elem_none_if_no_found:
                return None
            else:
                raise Exception(exception_message)

    def find_element(self, locator, timeout=60, elem_none_if_no_found=False):
        return self._find(EC.presence_of_element_located, locator, timeout, "Element not found or timed out",
                          elem_none_if_no_found)

    def find_elements(self, locator, timeout=60, elem_none_if_no_found=False) -> list:
        return self._find(EC.presence_of_all_elements_located, locator, timeout, "Elements not found or timed out",
                          elem_none_if_no_found)

    @staticmethod
    def find_element_within(parent_element, search_param, search_type=By.CSS_SELECTOR, timeout=10,
                            elem_none_if_no_found=False):
        try:
            element = WebDriverWait(parent_element, timeout).until(
                EC.presence_of_element_located((search_type, search_param))
            )
            return element
        except TimeoutException:
            if elem_none_if_no_found:
                return
            raise TimeoutException(
                f"Could not find element with search parameter '{search_param}' within {parent_element}")

    def wait_for_element_to_be_clickable(self, locator, timeout=60):
        return self._find(EC.element_to_be_clickable, locator, timeout, "Timed out waiting for element to be clickable")

    def wait_for_element(self, locator, timeout=60, elem_none_if_no_found=False):
        return self._find(EC.visibility_of_element_located, locator, timeout,
                          f"Timed out waiting for element locator: {locator}",
                          elem_none_if_no_found)
