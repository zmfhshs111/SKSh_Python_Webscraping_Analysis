# statistics_function.py
import math

def calculate_statistics(numbers):
    if not numbers:
        return None, None, None, None

    average = sum(numbers) / len(numbers)
    max_value = max(numbers)
    min_value = min(numbers)

    # 표준편차 계산
    variance = sum([(x - average) ** 2 for x in numbers]) / len(numbers)
    std_dev = math.sqrt(variance)

    return average, max_value, min_value, std_dev

data = [10, 20, 30, 40, 50]
avg, max_val, min_val, std = calculate_statistics(data)

print(f"숫자들: {data}")
print(f"평균: {avg:.1f}")
print(f"최댓값: {max_val}")
print(f"최솟값: {min_val}")
print(f"표준편차: {std:.2f}")