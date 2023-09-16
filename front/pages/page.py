from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from front.pages.base_page import BasePage


class CalendarPage(BasePage):

    CALENDER_VIEWS = (By.CSS_SELECTOR, "label.ant-radio-button-wrapper")
    DATE = (By.CSS_SELECTOR, "span.header2-text-label")
    NAVIGATION_BACKWARD = (By.CSS_SELECTOR, "i[aria-label='icon: left']")
    NAVIGATION_FORWARD = (By.CSS_SELECTOR, "i[aria-label='icon: right']")
    RESOURCE_VIEW = (By.CSS_SELECTOR, "table.resource-table>tbody")
    CALENDER = (By.CSS_SELECTOR, "div.event-container")

    def __init__(self, driver):
        super().__init__(driver)

    def click_on_date(self) -> None:
        self.click_element(self.DATE)

    def get_possible_views(self) -> dict:
        views = self.find_elements(self.CALENDER_VIEWS)
        radio_buttons = {}

        for label in views:
            text = label.get_attribute('innerText')
            radio_buttons[text] = label

        return radio_buttons

    def switch_view(self, requested_view) -> None:
        button = self.get_possible_views().get(requested_view)

        if not button:
            raise Exception("Error: The requested view not found!")

        self.wait_for_element_to_be_clickable(button)
        button.click()

    def verify_requested_view_checked(self, requested_view: str) -> bool:
        button = self.get_possible_views().get(requested_view)
        button_class = button.get_attribute("class")
        if "ant-radio-button-wrapper-checked" in button_class:
            return True
        else:
            raise Exception("Error:The requested view is not checked!")

    def verify_event_was_created(self, event_resource_id: int) -> bool:
        calender_rows = self.find_elements(self.CALENDER)

        if 2 <= event_resource_id < len(calender_rows):
            event_container = calender_rows[event_resource_id]
            exists_events = self.find_element_within(event_container, "a", timeout=2, elem_none_if_no_found=True)
            return exists_events is not None

    def create_event(self) -> int:
        calender_rows: list = self.find_elements(self.CALENDER)
        resource_id: int = None

        for i in range(2, len(calender_rows)):
            # check if row have event already,
            # start from 2 because in the first row it is not possible to create events
            # and in the second row there are always events on the whole row
            row = calender_rows[i]
            exists_events = self.find_element_within(row, "a", timeout=2, elem_none_if_no_found=True)
            if not exists_events:
                action = ActionChains(self.driver)
                action.move_to_element(row).click().perform()
                confirm = self.driver.switch_to.alert
                confirm.accept()
                resource_id = i
                break

        return resource_id

    def navigation_forward(self, skip_forward_num: int) -> None:
        for _ in range(skip_forward_num):
            self.click_element(self.NAVIGATION_FORWARD)

    def navigation_backward(self, skip_backward_num: int) -> None:
        for _ in range(skip_backward_num):
            self.click_element(self.NAVIGATION_BACKWARD)


class CalendarConfiguration(BasePage):
    CONFIGURATION_BUTTONS_LIST = (By.CSS_SELECTOR, "div>ul>li")
    INFINITE_SCROLL = "Infinite scroll"

    def __init__(self, driver):
        super().__init__(driver)

    def get_button_from_configuration_list(self, button_link_text):
        found = False

        configuration_button_list = self.find_elements(self.CONFIGURATION_BUTTONS_LIST)
        for config_button in configuration_button_list:
            button_text = config_button.text

            if button_text == button_link_text:
                found = True
                break

        if not found:
            raise Exception("Config button not found!")

        return config_button

    def enable_infinite_scroll(self) -> None:
        infinite_scroll = self.get_button_from_configuration_list(self.INFINITE_SCROLL)
        self.click_element(infinite_scroll)

    def get_calendar_configuration(self) -> str:
        url = self.driver.current_url
        parts = url.split('/')
        configuration = parts[-1]

        return configuration



