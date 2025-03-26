grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
average_grade= sum(grades)/len(grades)
grades.sort(reverse=True)
print(grades)
print('Average grade is ', (average_grade))