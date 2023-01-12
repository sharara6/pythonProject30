def get_grade_and_absence_dicts():
student_id
def Financial_grades(student_id):
    cont="n"
    g=["G","g"]
    f=["F","f"]
    y=["y","Y"]
    n=["n","N"]
    while cont== "n" or cont == "N":
        x=input("would you like to look at your Financials or your GPA? (F/G?):")
        while x not in g and x not in f :
            x = input("Please enter a valid answer:")
        if x in f:
                scholarship(GPA_calculator(Math_grades,English_grades,CS_grades,student_id))
                cont = input("do you want to exit the program?(y/n):")
        elif x in g:
                Student_GPA=GPA_calculator(Math_grades,English_grades,CS_grades,student_id)
                print("student",student_id2,"GPA=",Student_GPA)
                check_GPA(Student_GPA)
                Rank(student_id)
                cont=input("do you want to exit the program?(y/n):")
def GPA_calculator(g1,g2,,student_id):
    Ethics_grade=g1[student_id]
    English_grade=g2[student_id]
    Student_GPA=((Ethics_grade+English_grade)/200)*4
    return Student_GPA
def check_GPA(o):
    if o < 2.2 :
        print('THIS IS YOUR WARNING if you dont raise your GPA you will be entered into avademic probation')
def scholarship(P):
    if P <3.3:
        print("You are not applicable to any scholarships")
    if P > 3.3 and P<3.5:
        print ("Congratulations you are applicable to a 25% scholarship, please head to the finance office to register for it")
    if P > 3.5 and P<3.7:
        print ("Congratulations you are applicable to a 50% scholarship, please head to the finance office to register for it")
    if P > 3.7 and P<3.9:
        print ("Congratulations you are applicable to a 75% scholarship, please head to the finance office to register for it")
    if P > 3.9:
        print ("Congratulations you are applicable to a 100% scholarship, please head to the finance office to register for it")
def Rank(student_id):
    if section1_grades.get(student_id) is not None:
        sectionl=list(section1_grades.values())
        sectionl.sort(reverse=True)
        for i in range (len(sectionl)):
            if section1_grades[student_id]== sectionl[i]:
                student_id2=student_id+"'s"
                print("student",student_id2,"section rank is",(i+1))
    elif section2_grades.get(student_id) is not None:
        sectionl=list(section2_grades.values())
        sectionl.sort(reverse=True)
        for i in range (len(sectionl)):
            if section2_grades[student_id]== sectionl[i]:
                student_id2=student_id+"'s"
                print("student",student_id2,"section rank is",(i+1))
    elif section3_grades.get(student_id) is not None:
        sectionl=list(section3_grades.values())
        sectionl.sort(reverse=True)
        for i in range (len(sectionl)):
            if section3_grades[student_id]== sectionl[i]:
                student_id2=student_id+"'s"
                print("student",student_id2,"section rank is",(i+1))
Financial_grades(student_id)