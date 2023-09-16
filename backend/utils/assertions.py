
@staticmethod
def assert_true(boolean_value, msg=None):
    assert boolean_value, f"Error: The assertion was failed. {msg}"


@staticmethod
def assert_equals(expected_result, result, msg=None):
    assert expected_result == result, f"Error: The expected_text is different then the text. expected: {expected_result}" \
                                      f" result: {result},{msg}"
