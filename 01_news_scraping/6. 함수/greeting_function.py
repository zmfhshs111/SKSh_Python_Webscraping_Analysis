# greeting_function.py
def greet(name, greeting="안녕하세요", suffix="님!"):
    return f"{greeting}, {name}{suffix}"

print(greet("김철수"))
print(greet("John", greeting="Hello", suffix="!"))
print(greet("이영희", suffix="님! 좋은 하루 되세요!"))