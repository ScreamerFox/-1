grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
stud_scores = (sum(grades[0])/len(grades[0]),
            sum(grades[1])/len(grades[1]),
            sum(grades[2])/len(grades[2]),
            sum(grades[3])/len(grades[3]),
            sum(grades[4])/len(grades[4]))

s = sorted(students)

av_st = {}
av_st.update({
    s[0]: stud_scores[0],
    s[1]: stud_scores[1],
    s[2]: stud_scores[2],
    s[3]: stud_scores[3],
    s[4]: stud_scores[4]
})
print(av_st)

#Вывод:
# {'Aaron': 4.0, 'Bilbo': 2.25, 'Johnny': 4.0, 'Khendrik': 3.6666666666666665, 'Steve': 4.8}
