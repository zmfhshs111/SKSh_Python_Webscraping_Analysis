# conditional_expression.py
# 삼항 연산자 예제
score = 85
result = "합격" if score >= 80 else "불합격"
print(f"점수: {score}, 결과: {result}")

age = 17
status = "성인" if age >= 19 else "미성년자"
print(f"나이: {age}, 상태: {status}")

# 리스트 컴프리헨션과 조건부 표현식
numbers = [5, -3, 12, 0, 8, -7, 23]
positive_numbers = [num for num in numbers if num > 0]
print(f"양수들: {positive_numbers}")

# 최대값 찾기 (간단한 예시)
num1 = 42
num2 = 18
max_value = num1 if num1 > num2 else num2
print(f"숫자들의 최대값: {max_value}")