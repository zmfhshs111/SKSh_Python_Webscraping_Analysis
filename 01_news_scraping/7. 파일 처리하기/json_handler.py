# json_handler.py
import json

data = {
    "이름": "김철수",
    "나이": 25,
    "직업": "개발자",
    "취미": ["독서", "영화감상", "코딩"],
    "주소": "서울시 강남구"
}
json_file_name = "data.json"

# JSON 파일에 쓰기
with open(json_file_name, 'w', encoding='utf-8') as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=4)
print(f"데이터가 {json_file_name}에 저장되었습니다.")

# JSON 파일에서 읽기
print("\nJSON에서 읽어온 데이터:")
with open(json_file_name, 'r', encoding='utf-8') as json_file:
    loaded_data = json.load(json_file)
    for key, value in loaded_data.items():
        if isinstance(value, list):
            print(f"{key}: {', '.join(value)}")
        else:
            print(f"{key}: {value}")