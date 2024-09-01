import openai

# API 키로 OpenAI 클라이언트 초기화
openai.api_key = ""
# 모든 fine-tuned 작업 목록 가져오기
response = openai.FineTuningJob.list()

# 모든 fine-tuned 모델 이름 출력
for job in response["data"]:
    print(job.get("fine_tuned_model", "모델 이름 없음"))
