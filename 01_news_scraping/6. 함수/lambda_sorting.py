# lambda_sorting.py
students = [('김철수', 85), ('이영희', 92), ('박민수', 78), ('최수진', 95)]

# 이름순 정렬
sorted_by_name = sorted(students, key=lambda student: student[0])

# 점수순 정렬 (오름차순)
sorted_by_score_asc = sorted(students, key=lambda student: student[1])

# 점수 내림차순 정렬
sorted_by_score_desc = sorted(students, key=lambda student: student[1], reverse=True)

print(f"학생 정보: {students}")
print(f"이름순 정렬: {sorted_by_name}")
print(f"점수순 정렬: {sorted_by_score_asc}")
print(f"점수 내림차순: {sorted_by_score_desc}")