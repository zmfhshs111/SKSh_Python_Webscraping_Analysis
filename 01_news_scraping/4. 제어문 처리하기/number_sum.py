# number_sum.py
total_sum = 0
while True:
    num = int(input("숫자를 입력하세요 (0을 입력하면 종료): "))
    if num == 0:
        break
    total_sum += num

print(f"입력된 숫자들의 합: {total_sum}")