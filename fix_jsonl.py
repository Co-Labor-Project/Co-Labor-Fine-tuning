import json
import re

# 입력 파일과 출력 파일 경로
input_file = "clean-train-data-test.jsonl"
output_file = "fixed-train-data-test.jsonl"

valid_lines = []

with open(input_file, "r", encoding="utf-8") as infile:
    for line in infile:
        # 1️⃣ 불필요한 개행 및 공백 정리
        line = line.strip()
        line = line.replace("nn", "\n")  # "nn" → "\n" 변환
        line = re.sub(r"\s+", " ", line)  # 연속된 공백 제거

        # 2️⃣ JSON 키-값 형식 자동 복구
        line = re.sub(r'"\s*role""', r'"role"', line)  # "role"" → "role"
        line = re.sub(r'"\s*content""', r'"content"', line)  # "content"" → "content"
        line = re.sub(r'"\s*messages"\s*{', r'"messages": {', line)  # "messages" { → "messages": {

        # 3️⃣ JSON 형식 복구 및 검증
        try:
            json_obj = json.loads(line)  # JSON 파싱 확인
            valid_lines.append(json.dumps(json_obj, ensure_ascii=False))  # 올바른 JSON 저장
        except json.JSONDecodeError:
            print(f"❌ JSON 오류 발생: {line[:150]}...")  # 깨진 부분 출력

# 4️⃣ 정상 JSONL 파일로 저장
with open(output_file, "w", encoding="utf-8") as outfile:
    outfile.write("\n".join(valid_lines) + "\n")

print(f"✅ JSONL 복구 완료: {output_file}")
