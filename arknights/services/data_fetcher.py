import requests

__all__ = ["fetch_operator_data", "fetch_skills_data"]


def fetch_operator_data():
    try:
        operator_resp = requests.get(
            "https://raw.githubusercontent.com/Kengxxiao/ArknightsGameData_YoStar/main/en_US/gamedata/excel/character_table.json"
        )
        operator_resp.raise_for_status()
        return operator_resp.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching operator data: {e}")
        return None


def fetch_skills_data():
    try:
        skills_resp = requests.get(
            "https://raw.githubusercontent.com/Kengxxiao/ArknightsGameData_YoStar/refs/heads/main/en_US/gamedata/excel/skill_table.json"
        )
        skills_resp.raise_for_status()
        return skills_resp.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching skills data: {e}")
        return None
