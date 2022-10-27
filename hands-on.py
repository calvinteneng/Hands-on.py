marks = (75, 52, 13, 67, 87)

for each_mark in marks:
    # print(each_mark)
    if each_mark >= 85 and each_mark <= 100:
        print('You got an A! Congrats!', each_mark)        
        grade = 'A'
    elif each_mark >= 75 and each_mark < 85:
        print('You got a B! Well done!', each_mark)       
        grade = 'B'
    elif each_mark >= 50 and each_mark < 75:
        print('You got a C. Not great, not terrible.', each_mark)
        grade = 'C'
    elif each_mark >= 40 and marks < 50:
        print('You got a D. But you can do better!', each_mark)
        grade = 'D'
    else:
        print("You did not pass the exam. Contact the teacher for more information.", each_mark)
        grade = 'Fail'
    print('Writing grade: {} into sheet!'.format(grade))


