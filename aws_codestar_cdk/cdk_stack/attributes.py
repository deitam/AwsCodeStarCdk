from typing import List


class Attributes():
    def __init__(self, project_name: str, bucket_name, subnet_ids: List[str], security_group_ids: List[str]):
        self.project_name = project_name
        self.bucket_name = bucket_name
        self.subnet_ids = Attributes._list_to_comma_separated_list(subnet_ids)
        self.security_group_ids = Attributes._list_to_comma_separated_list(security_group_ids)

    @staticmethod
    def _list_to_comma_separated_list(strings: List[str]) -> str:
        result = ''

        for i in range(len(strings) - 1):
            result += strings[i] + ', '
        result += strings[len(strings) - 1]

        return result
