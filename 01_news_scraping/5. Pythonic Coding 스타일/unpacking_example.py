# unpacking_example.py

# 언패킹 예제
# 튜플 언패킹
coordinates = (10, 20)
x, y = coordinates
print(f"좌표: x={x}, y={y}")

# 리스트 언패킹
data = [1, 2, 3]
a, b, c = data
print(f"리스트 언패킹: a={a}, b={b}, c={c}")

# *args (가변 위치 인수) 예제
def sum_all_numbers(*args):
    return sum(args)

print(f"가변 인수의 합: {sum_all_numbers(10, 20, 30)}")

# **kwargs (가변 키워드 인수) 예제
def print_user_info(**kwargs):
    info = []
    for key, value in kwargs.items():
        info.append(f"{key}={value}")
    print(f"키워드 인수들: {', '.join(info)}")

print_user_info(name="김철수", age=25, city="서울")