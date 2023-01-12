#student_id = int(input("enter student id:"))
def get_English_grades(student_id):
    import json
    group1_id = [202201, 202202, 202203, 202204, 202205]
    group2_id = [202206, 202207, 202208, 202209, 202210]
    if student_id in group1_id:
        with open('file156(g).txt') as f:
               data = f.read()
               English_156= json.loads(data)
               return(English_156)
    elif student_id in group2_id:
        with open('file156(g2).txt') as f:
               data = f.read()
               English_156_2= json.loads(data)
               return(English_156_2)
def get_Ethics_grades(student_id):
    import json
    group1_id = [202201, 202202, 202203, 202204, 202205]
    group2_id = [202206, 202207, 202208, 202209, 202210]
    if student_id in group1_id:
        with open('file150(g).txt') as f:
               data = f.read()
               Ethics_150= json.loads(data)
               return(Ethics_150)
    elif student_id in group2_id:
        with open('file150(g2).txt') as f:
               data = f.read()
               Ethics_150_2= json.loads(data)
               return(Ethics_150_2)
# Ethicgrades=(get_Ethics_grades(student_id))
# Englishgrades=(get_English_grades(student_id))
def GPA_calculator(student_id):
    Ethicgrades = (get_Ethics_grades(student_id))
    Englishgrades=(get_English_grades(student_id))
    Ethics_grade=Ethicgrades[str(student_id)]
    English_grade=Englishgrades[str(student_id)]
    Student_GPA=((Ethics_grade+English_grade)/200)*4
    return Student_GPA
#studentgpa=(GPA_calculator(student_id))
#print(studentgpa)
def check_GPA(o):
    if o < 2.2 :
        print('THIS IS YOUR WARNING if you dont raise your GPA you will be entered into avademic probation')
#check_GPA(studentgpa)
def get_English_absence(student_id):
    import json
    group1_id = [202201, 202202, 202203, 202204, 202205]
    group2_id = [202206, 202207, 202208, 202209, 202210]
    if student_id in group1_id:
        with open('file156(a).txt') as f:
               data = f.read()
               English_156_a= json.loads(data)
               return(English_156_a)
    elif student_id in group2_id:
        with open('file156(a2).txt') as f:
               data = f.read()
               English_156_a2= json.loads(data)
               return(English_156_a2)
def get_Ethics_absence(student_id):
    import json
    group1_id = [202201, 202202, 202203, 202204, 202205]
    group2_id = [202206, 202207, 202208, 202209, 202210]
    if student_id in group1_id:
        with open('file150(a).txt') as f:
               data = f.read()
               Ethics_150_a= json.loads(data)
               return(Ethics_150_a)
    elif student_id in group2_id:
        with open('file150(a2).txt') as f:
               data = f.read()
               Ethics_150_a2= json.loads(data)
               return(Ethics_150_a2)
def absence_warning(student_id):
    Ethicabsences = (get_Ethics_absence(student_id))
    Englishabsences = (get_English_absence(student_id))
    Ethics_absence = Ethicabsences[str(student_id)]
    English_absence = Englishabsences[str(student_id)]
    if English_absence > 4:
        print("THIS IS YOUR WARNING, you have exceeded your allowed number of absences for your English course , please go talk to your academic advisor")
        print("check with your English doctor if you have failed this course")
    if Ethics_absence > 4:
        print("THIS IS YOUR WARNING, you have exceeded your allowed number of absences for your Ethics course , please go talk to your academic advisor")
        print("check with your Ethics doctor if you have failed this course")
def scholarship(student_id):
    P=GPA_calculator(student_id)
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
def Student_portal():
    group1_id = [202201, 202202, 202203, 202204, 202205]
    group2_id = [202206, 202207, 202208, 202209, 202210]
    student_id=int(input("Enter your student id here:"))
    while student_id not in group1_id and student_id not in group2_id:
        student_id=int(input("Please enter a correct id:"))
def Financial_Grades():
    cont = "n"
    g = ["G", "g"]
    f = ["F", "f"]
    y = ["y", "Y"]
    n = ["n", "N"]
    while cont == "n" or cont == "N":
        x = input("would you like to look at your Financials or your GPA? (F/G?):")
        while x not in g and x not in f:
            x = input("Please enter a valid answer:")





#absence_warning(student_id)
# print(Ethicgrades)
# print(Englishgrades)
# file = open('file156.txt', 'r')
# print(file.read())
#file156(g)
#file156(a)
#file156(g2)
#file156(a2)
#file150(g)
#file150(a)
#file150(g2)
#file150(a2)
# student_id=input("enter your id here:")
# def get_156_g_and_a_dicts(student_id):
#     group1_id = [202201, 202202, 202203, 202204, 202205]
#     group2_id = [202206, 202207, 202208, 202209, 202210]
#     if student_id in group1_id:
#         with open('file156(g).txt') as f:
#             data = f.read()
#             English_156 = json.loads(data)
#             f.close()
#             return (English_156)
    # elif student_id in group2_id:
    #     with open('file156(2).txt') as f:
    #         data = f.read()
    #         English_156_2_grades = json.loads(data)
    #         return (English_156_2_grades)
# Ethics_grade=Ethicgrades[student_id]
# print(get_Ethics_absence(student_id))
# print(get_English_absence(student_id))
# print(get_English_grades(student_id))
# print(get_Ethics_grades(student_id))
#scholarship(student_id)
Student_portal()
