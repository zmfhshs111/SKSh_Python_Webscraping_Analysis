# character_counter.py
input_string = input("문자열을 입력하세요: ")
char_to_find = input("찾을 문자를 입력하세요: ")

count = input_string.count(char_to_find)

print(f"문자 '{char_to_find}'이 {count}번 나타납니다.")