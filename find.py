import openai

# API 키 설정
openai.api_key = ""

# 모든 fine-tuned 작업 목록 가져오기 (구버전 API)
response = openai.FineTune.list()

# fine-tuned 모델 이름 출력
for job in response["data"]:
    print(job.get("fine_tuned_model", "모델 이름 없음"))
