# split_join_example.py
text = "Python is awesome programming language"

# split을 사용하여 단어별로 분리
words = text.split(" ")

# 하이픈으로 연결
hyphenated_text = "-".join(words)

# 대문자로 변환 후 공백으로 연결
uppercase_text = " ".join([word.upper() for word in words])

print(f"원본 문자열: {text}")
print(f"분리된 단어들: {words}")
print(f"하이픈으로 연결: {hyphenated_text}")
print(f"대문자로 변환 후 공백으로 연결: {uppercase_text}")