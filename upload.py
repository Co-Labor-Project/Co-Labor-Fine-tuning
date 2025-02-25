import os
from openai import OpenAI

client = OpenAI(api_key="")

# response = client.files.create(
#     file=open("train-data-test.jsonl", "rb"), purpose="fine-tune"
# )

# 현재 `upload.py`가 있는 폴더 기준으로 파일 경로 설정
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "data.jsonl")

response = client.files.create(
    file=open(file_path, "rb"), purpose="fine-tune"
)

print(response)
