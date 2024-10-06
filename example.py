from arknights import client
from arknights.services import data_fetcher

ak = client.Arknights()

operator_data = data_fetcher.fetch_operator_data()
skills_data = data_fetcher.fetch_skills_data()

operator = ak.fetch_operator(
    "char_4100_caper",
    operator_data,
    skills_data,
)

print(operator.model_dump_json(indent=4))
