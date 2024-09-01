from openai import OpenAI

client = OpenAI(api_key="")

response = client.files.create(
    file=open("train-data4.jsonl", "rb"), purpose="fine-tune"
)

print(response)
