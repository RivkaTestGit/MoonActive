import pytest

from backend.utils.assertions import assert_equals, assert_true
from backend.utils.helper import Helper
from front.data_for_tests.calender_data_for_tests import DataForTests
from front.pages.page import CalendarPage, CalendarConfiguration


@pytest.mark.usefixtures("setup", "test_config")
class TestCalender:

    @pytest.fixture(scope="class")
    def calendar_page(self, setup, test_config):
        driver = setup
        calendar_page = CalendarPage(driver)
        calendar_page.open_url(Helper.get_config_value_by_name(test_config, ["calender", "url"]))
        return calendar_page

    @pytest.fixture(scope="class")
    def switch_to_infinite_scroll_and_month_view(self, setup, calendar_page):
        driver = setup
        calendar_config = CalendarConfiguration(driver)
        calendar_config.enable_infinite_scroll()
        calendar_page.switch_view("Month")

    @pytest.mark.parametrize("test_data", DataForTests.switch_to_infinite_scroll_and_month_view())
    def test_switch_to_infinite_scroll_and_month_view(self, setup, test_data, calendar_page,
                                                      switch_to_infinite_scroll_and_month_view):
        driver = setup
        calendar_config = CalendarConfiguration(driver)
        calendar_configuration = calendar_config.get_calendar_configuration()
        assert_equals(calendar_configuration, test_data["configuration"])
        calendar_page.verify_requested_view_checked(test_data["view_type"])

    def test_create_events_check_element_count_increased(self, calendar_page,
                                                         switch_to_infinite_scroll_and_month_view):
        event_resource_id = calendar_page.create_event()
        assert_true(calendar_page.verify_event_was_created(event_resource_id),
                    "Error: After creating an event, Event not found!")
        event_resource_id = calendar_page.create_event()
        assert_true(calendar_page.verify_event_was_created(event_resource_id),
                    "Error: After creating an event, Event not found!")

    def test_create_event_and_go_ahead_one_month_and_check_dom_decrease(self, setup, calendar_page,
                                                                        switch_to_infinite_scroll_and_month_view):
        event_resource_id = calendar_page.create_event()
        calendar_page.navigation_forward(1)
        assert_true(not calendar_page.verify_event_was_created(event_resource_id),
                    "Error: After creating an event and going one month forward, Event found!")

    @pytest.mark.skip("This test have bug, so it will failed")
    def test_create_event_change_month_and_check_event_still_exist(self, setup, calendar_page,
                                                                   switch_to_infinite_scroll_and_month_view):
        event_resource_id = calendar_page.create_event()
        calendar_page.navigation_forward(1)
        assert_true(not calendar_page.verify_event_was_created(event_resource_id),
                    "Error: After creating an event and going one month forward, Event found!")
        calendar_page.navigation_backward(1)
        assert_true(calendar_page.verify_event_was_created(event_resource_id),
                    "Error: After creating an event, change month and go back.Event not found!")