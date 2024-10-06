from arknights import client

ak = client.Arknights()

operator = ak.fetch_operator("char_4100_caper")

print(operator.model_dump_json(indent=4))
