import requests


def fetch_operator_data():
    operator_resp = requests.get(
        "https://raw.githubusercontent.com/Kengxxiao/ArknightsGameData_YoStar/main/en_US/gamedata/excel/character_table.json"
    )
    return operator_resp.json()


def fetch_skills_data():
    skills_resp = requests.get(
        "https://raw.githubusercontent.com/Kengxxiao/ArknightsGameData_YoStar/refs/heads/main/en_US/gamedata/excel/skill_table.json"
    )
    return skills_resp.json()
