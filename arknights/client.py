from .models import OperatorDetail, SkillDetails
from .services import fetch_operator_data, fetch_skills_data
from typing import Dict, Any, Optional


class Arknights:
    def build_operator_with_skills(
        self, operator_info: Dict[str, Any], skills_data: Dict[str, Any]
    ) -> OperatorDetail:
        """
        Build an OperatorDetail instance with the associated skills.

        :param operator_info: Information about the operator.
        :param skills_data: A dictionary containing skill details.
        :return: An OperatorDetail instance.
        """
        skill_details = []

        skill_ids = [skill["skillId"] for skill in operator_info["skills"]]

        for skill_id in skill_ids:
            skill_info = skills_data.get(skill_id)
            if skill_info:
                skill_details.append(SkillDetails(**skill_info))

        operator_info["skills"] = skill_details
        return OperatorDetail(**operator_info)

    def fetch_operator(
        self, lookup_id: str, operator_data: Dict[str, Any], skills_data: Dict[str, Any]
    ) -> Optional[OperatorDetail]:
        """
        Fetch an operator by its ID.

        :param lookup_id: The ID of the operator to fetch.
        :param operator_data: A dictionary containing operator data.
        :param skills_data: A dictionary containing skill data.
        :return: An OperatorDetail instance or None if not found.
        """
        operator_info = operator_data.get(lookup_id)
        if operator_info:
            return self.build_operator_with_skills(operator_info, skills_data)
        return None
