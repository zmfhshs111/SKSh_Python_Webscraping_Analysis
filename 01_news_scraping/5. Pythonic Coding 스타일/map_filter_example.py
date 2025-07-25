# map_filter_example.py
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 모든 수의 제곱 (map 사용)
squared_numbers = list(map(lambda x: x**2, numbers))

# 5보다 큰 수들 (filter 사용)
greater_than_5 = list(filter(lambda x: x > 5, numbers))

# 5보다 큰 수들의 제곱 (filter 후 map)
squared_greater_than_5 = list(map(lambda x: x**2, filter(lambda x: x > 5, numbers)))

print(f"원본 숫자: {numbers}")
print(f"모든 수의 제곱: {squared_numbers}")
print(f"5보다 큰 수들: {greater_than_5}")
print(f"5보다 큰 수들의 제곱: {squared_greater_than_5}")