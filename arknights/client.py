from arknights.services import data_fetcher
from .models import Operator, Skill

__all__ = ["Arknights"]


class OperatorNotFoundError(Exception):
    pass


class Arknights:
    def __init__(self):

        self.operator_data = data_fetcher.fetch_operator_data()
        self.skills_data = data_fetcher.fetch_skills_data()

    def build_operator_with_skills(
        self, operator_info: dict[str, dict], skills_data: dict[str, any]
    ) -> Operator:
        """
        Build an `Operator` instance with the associated skills.

        :param operator_info: Information about the operator.
        :param skills_data: A dictionary containing skill details.
        :return: An `Operator` instance.
        """
        skill_details = []
        skill_ids = (skill["skillId"] for skill in operator_info["skills"])

        for skill_id in skill_ids:
            skill_info = skills_data.get(skill_id)
            if skill_info:
                skill_details.append(Skill(**skill_info))

        operator_info["skills"] = skill_details
        return Operator(**operator_info)

    def fetch_operator(self, lookup_id: str) -> Operator | None:
        """
        Fetch an operator by its ID.

        :param lookup_id: The ID of the operator to fetch.
        :return: An `Operator` instance or None if not found.
        """
        operator_info = self.operator_data.get(lookup_id)
        if operator_info:
            return self.build_operator_with_skills(operator_info, self.skills_data)
        raise OperatorNotFoundError(f"Operator with ID {lookup_id} not found.")
