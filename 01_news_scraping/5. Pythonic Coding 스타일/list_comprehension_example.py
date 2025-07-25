# list_comprehension_example.py
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 짝수만 추출 (리스트 컴프리헨션)
even_numbers = [num for num in numbers if num % 2 == 0]

# 짝수의 제곱 (리스트 컴프리헨션)
squared_evens = [num ** 2 for num in numbers if num % 2 == 0]

print(f"원본 리스트: {numbers}")
print(f"짝수들: {even_numbers}")
print(f"짝수의 제곱: {squared_evens}")