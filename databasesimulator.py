def students_courses(stud1, stud2, courses):
    if stud1 in courses and stud2 in courses:
        courses_stud1 = set(courses[stud1])
        courses_stud2 = set(courses[stud2])
        same_courses = courses_stud1 & courses_stud2
        return list(same_courses)


students = {'Mike': ('Math', 'English', 'History'),
            'Max': ('English', 'Biology', 'Physics'),
            'Kate': ('Art', 'Biology')}

student1 = 'Mike'
student2 = 'Max'
student3 = "Kate"

result = students_courses(student1, student2, students)
result1 = students_courses(student2, student3, students)
print(f"Same coureses of {student1} and {student2}: {result}")
print(f"Same coureses of {student2} and {student3}: {result1}")
