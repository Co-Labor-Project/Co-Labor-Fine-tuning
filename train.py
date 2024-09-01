# from openai import OpenAI
# import time

# # OpenAI 클라이언트 초기화 (API 키 설정)
# client = OpenAI(
#     api_key=""
# )

# try:
#     # (1) 파일을 미리 OpenAI 플랫폼에 업로드한 후 해당 파일 ID를 사용
#     training_file_id = (
#         "file-2CpFpRsAxpKMnPvPvshwzv1A"  # 여기에 실제 파일 ID를 입력하세요
#     )
#     print(f"Using uploaded file ID: {training_file_id}")

#     # (2) Fine-tuning job 생성하기
#     fine_tune_response = client.fine_tuning.jobs.create(
#         training_file=training_file_id,  # 업로드한 파일의 ID를 사용
#         model="gpt-3.5-turbo",  # 사용할 모델 이름
#         suffix="colaw_fine_tuned_model",  # 모델의 사용자 정의 이름
#     )

#     fine_tune_job_id = fine_tune_response.id  # 생성된 fine-tune job의 ID 추출
#     print(f"Fine-tune Job ID: {fine_tune_job_id}")

#     # (3) 학습 상태 확인하기
#     # 모든 fine-tuning jobs 목록 확인
#     jobs_list = client.fine_tuning.jobs.list()
#     print("Fine-tuning jobs list:")
#     for job in jobs_list:
#         print(job)

#     # 특정 fine-tune job의 상태 확인
#     job_status = client.fine_tuning.jobs.retrieve(fine_tune_job_id)
#     print(f"Fine-tune Job Status: {job_status.status}")

#     # (선택사항) 작업 완료까지 대기
#     while job_status.status != "succeeded" and job_status.status != "failed":
#         print(f"Job status: {job_status.status}")
#         time.sleep(60)  # 1분마다 상태 확인
#         job_status = client.fine_tuning.jobs.retrieve(fine_tune_job_id)

#     print(f"Final job status: {job_status.status}")

# except Exception as e:
#     print(f"An error occurred: {e}")

from openai import OpenAI
import time

# OpenAI 클라이언트 초기화 (API 키 설정)
client = OpenAI(api_key="")

try:
    # (1) 파일을 미리 OpenAI 플랫폼에 업로드한 후 해당 파일 ID를 사용
    training_file_id = (
        "file-nB5ihQ9hURmLtZcEmkKqn8x0"  # 여기에 실제 파일 ID를 입력하세요
    )
    print(f"Using uploaded file ID: {training_file_id}")

    # (2) Fine-tuning job 생성하기
    fine_tune_response = client.fine_tuning.jobs.create(
        training_file=training_file_id,  # 업로드한 파일의 ID를 사용
        model="gpt-3.5-turbo",  # 사용할 모델 이름
        suffix="colaw_fine_tuned_model",  # 모델의 사용자 정의 이름
    )

    fine_tune_job_id = fine_tune_response.id  # 생성된 fine-tune job의 ID 추출
    print(f"Fine-tune Job ID: {fine_tune_job_id}")

    # (3) 학습 상태 확인하기
    # 모든 fine-tuning jobs 목록 확인
    jobs_list = client.fine_tuning.jobs.list()
    print("Fine-tuning jobs list:")
    for job in jobs_list:
        print(job)

    # 특정 fine-tune job의 상태 확인
    job_status = client.fine_tuning.jobs.retrieve(fine_tune_job_id)
    print(f"Fine-tune Job Status: {job_status.status}")

    # (선택사항) 작업 완료까지 대기
    while job_status.status != "succeeded" and job_status.status != "failed":
        print(f"Job status: {job_status.status}")
        time.sleep(60)  # 1분마다 상태 확인
        job_status = client.fine_tuning.jobs.retrieve(fine_tune_job_id)

    print(f"Final job status: {job_status.status}")

except Exception as e:
    print(f"An error occurred: {e}")
