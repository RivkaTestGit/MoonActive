from typing import Optional, List

from deepdiff import DeepDiff


class Helper:

    @staticmethod
    def get_config_value_by_name(config, param_name):
        try:
            value = config
            for key in param_name:
                value = value[key]
            return value
        except (KeyError, TypeError):
            raise Exception(f"Parameter '{param_name}' not found in the configuration file.")

    @staticmethod
    def is_dictionary_empty(dictionary: dict) -> bool:
        return not bool(dictionary)

    @staticmethod
    def validate_json_response(json_to_compare, response_json, exclude_properties: Optional[List] = None) -> None:
        """
        Compare between two json file if the assertion failed return the diff
        :param json_to_compare: the json we want to check
        :param response_json: the json we compare to
        :param exclude_properties: optional param in case we want to ignore checking some roots
        :rtype: None
        """
        roots_exclude_paths = []

        if exclude_properties is not None:

            for root in exclude_properties:
                exclude_path = f"root['{root}']"
                roots_exclude_paths.append(exclude_path)

            diff: dict = DeepDiff(json_to_compare, response_json, exclude_paths=roots_exclude_paths)
        else:
            diff: dict = DeepDiff(json_to_compare, response_json)

        result: bool = Helper.is_dictionary_empty(diff)
        assert result, f"Error: Json objects are not match {diff}"

