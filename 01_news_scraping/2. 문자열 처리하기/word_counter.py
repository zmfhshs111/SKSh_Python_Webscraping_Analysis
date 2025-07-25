# word_counter.py
sentence = input("문장을 입력하세요: ")

no_spaces_sentence = sentence.replace(" ", "")
words = sentence.split()
word_count = len(words)

print(f"공백 제거: {no_spaces_sentence}")
print(f"단어 개수: {word_count}개")