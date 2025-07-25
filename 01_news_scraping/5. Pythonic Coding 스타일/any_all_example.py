# any_all_example.py
numbers1 = [2, 4, 6, 8, 10]
numbers2 = [1, 3, 5, 7, 12]

# numbers1에 대한 검사
all_even1 = all(num % 2 == 0 for num in numbers1)
any_greater_than_10_1 = any(num > 10 for num in numbers1)

print(f"숫자 리스트: {numbers1}")
print(f"모든 수가 짝수인가? {all_even1}")
print(f"하나라도 10보다 큰 수가 있는가? {any_greater_than_10_1}")

print("\n숫자 리스트2: [1, 3, 5, 7, 12]")
# numbers2에 대한 검사
all_even2 = all(num % 2 == 0 for num in numbers2)
any_greater_than_10_2 = any(num > 10 for num in numbers2)

print(f"모든 수가 짝수인가? {all_even2}")
print(f"하나라도 10보다 큰 수가 있는가? {any_greater_than_10_2}")