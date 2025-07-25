# system_info.py
import os
import sys

# 현재 작업 디렉토리
current_directory = os.getcwd()
print(f"현재 작업 디렉토리: {current_directory}")

# Python 버전
python_version = sys.version
print(f"Python 버전: {python_version.splitlines()[0]}")

# 운영체제 정보
operating_system = sys.platform
print(f"운영체제: {operating_system}")

# 환경 변수 PATH 일부
path_env = os.environ.get('PATH')
if path_env:
    # PATH 환경 변수의 일부만 출력 (예: 처음 3개 경로)
    print(f"환경 변수 PATH 일부: {':'.join(path_env.split(':')[:3])}")
else:
    print("환경 변수 PATH를 찾을 수 없습니다.")


# 파일 경로 정보 다루기
file_path = "/Users/username/documents/report.txt"
directory_name = os.path.dirname(file_path)
file_name = os.path.basename(file_path)
file_extension = os.path.splitext(file_path)[1]

print("\n파일 경로 정보:")
print(f"- 디렉토리: {directory_name}")
print(f"- 파일명: {file_name}")
print(f"- 확장자: {file_extension}")

# 파일 존재 여부 확인 (예시이므로 실제 파일이 없어도 False 출력)
file_exists = os.path.exists(file_path)
print(f"파일 존재 여부: {file_exists}")