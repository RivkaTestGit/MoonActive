class DataForTests:

    @staticmethod
    def switch_to_infinite_scroll_and_month_view() -> list:
        test_data = {
            "configuration": "infinitescroll",
            "view_type": "Month"
        }
        return [test_data]
