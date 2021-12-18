def gradingStudents(grades):
    answer = []
    for grade in grades:
        if grade >= 38:
            if 5 - grade % 5 < 3:
                grade += 5 - grade % 5
        answer.append(grade)
                
    return answer