# log_processor.py
import logging
import datetime

log_file_name = "application.log"

# 로거 설정
logging.basicConfig(filename=log_file_name, level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

# 로그 메시지 기록
logging.info("2025-07-20 09:00:00 - INFO - 애플리케이션 시작")
logging.warning("2025-07-20 09:15:00 - WARNING - 메모리 사용량이 높습니다")
logging.error("2025-07-20 10:30:00 - ERROR - 데이터베이스 연결 실패")
logging.info("2025-07-20 11:00:00 - INFO - 사용자 로그인 성공")
logging.error("2025-07-20 11:45:00 - ERROR - 파일을 찾을 수 없음")
logging.warning("2025-07-20 12:00:00 - WARNING - 디스크 공간 부족")

print("로그 파일이 생성되었습니다.")

# 특정 레벨의 로그 필터링 및 출력
def filter_logs_by_level(filename, level_str):
    filtered_logs = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            if f"- {level_str} -" in line:
                filtered_logs.append(line.strip())
    return filtered_logs

print("\nERROR 레벨 로그들:")
error_logs = filter_logs_by_level(log_file_name, "ERROR")
for log in error_logs:
    print(log)

print("\nWARNING 레벨 로그들:")
warning_logs = filter_logs_by_level(log_file_name, "WARNING")
for log in warning_logs:
    print(log)