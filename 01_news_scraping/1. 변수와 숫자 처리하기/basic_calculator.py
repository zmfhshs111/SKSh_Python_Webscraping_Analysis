# basic_calculator.py
num1 = int(input("첫 번째 숫자를 입력하세요: "))
num2 = int(input("두 번째 숫자를 입력하세요: "))

print(f"{num1}+{num2}={num1 + num2}")
print(f"{num1}-{num2}={num1 - num2}")
print(f"{num1}*{num2}={num1 * num2}")
print(f"{num1}/{num2}={num1 / num2:.2f}") # 소수점 두 자리까지 출력