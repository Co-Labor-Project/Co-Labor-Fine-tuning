from transformers import AutoTokenizer
import json

# 토크나이저 로드 (예: BERT)
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

# JSONL 파일 경로
file_path = "train-data4.jsonl"

# 전체 토큰 수 계산
total_tokens = 0

# 파일을 읽고 토큰 수 계산
with open(file_path, "r", encoding="utf-8") as file:
    for line in file:
        try:
            data = json.loads(line)
            # 모든 메시지를 합쳐 하나의 텍스트로 처리
            combined_text = " ".join([msg["content"] for msg in data["messages"]])
            # 텍스트를 토큰화하고 토큰 수 계산
            tokens = tokenizer.encode(combined_text, truncation=False)
            total_tokens += len(tokens)
        except json.JSONDecodeError:
            continue  # 잘못된 JSON 라인을 건너뜀

print(f"Total token count: {total_tokens}")
