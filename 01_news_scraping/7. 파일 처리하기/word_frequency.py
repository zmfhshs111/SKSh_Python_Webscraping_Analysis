# word_frequency.py
from collections import Counter
import re

text_content = """파이썬은 프로그래밍 언어입니다.
파이썬은 배우기 쉽고 강력한 언어입니다.
파이썬 프로그래밍."""

file_name = "sample_text.txt"

# 샘플 텍스트 파일 생성
with open(file_name, 'w', encoding='utf-8') as f:
    f.write(text_content)

word_counts = Counter()
with open(file_name, 'r', encoding='utf-8') as f:
    for line in f:
        # 특수문자 제거 및 소문자 변환 후 단어 분리
        words = re.findall(r'\b\w+\b', line.lower())
        word_counts.update(words)

print("단어 빈도 분석 결과:")
for word, count in word_counts.items():
    print(f"{word}: {count}번")