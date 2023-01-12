def get_English_grades(student_id):#this function gets the english course grade from the file entered by the teacher
    import json#json is a function that extracts dictionaries from files
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
def get_Ethics_grades(student_id):#this function gets the ethics course grade from the file entered by the teacher
    import json#json is a function that extracts dictionaries from files
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
def GPA_calculator(student_id):#this is a function that calculates the students GPA
    Ethicgrades = (get_Ethics_grades(student_id))
    Englishgrades=(get_English_grades(student_id))
    Ethics_grade=Ethicgrades[str(student_id)]
    English_grade=Englishgrades[str(student_id)]
    Student_GPA=((Ethics_grade+English_grade)/200)*4
    return Student_GPA
def check_GPA(o):#this function check if the student's GPA requires him to be put into academic probation
    if o < 2.2 :
        print('THIS IS YOUR WARNING, if you dont raise your GPA you will be entered into avademic probation')
def get_English_absence(student_id):#this function gets the english course absences inputted by the teacher
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
def get_Ethics_absence(student_id):#this function gets the ethics course absences inputted by the teacher
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
def absence_warning(student_id):#this function checks if the student has exceeded his absences and gives a warning
    Ethicabsences = (get_Ethics_absence(student_id))
    Englishabsences = (get_English_absence(student_id))
    Ethics_absence = Ethicabsences[str(student_id)]
    English_absence = Englishabsences[str(student_id)]
    if English_absence > 4:
        print("THIS IS YOUR WARNING, you have exceeded your allowed number of absences for your English course , please go talk to your academic advisor")
        print("check with your English doctor to see if you have failed this course")
    if Ethics_absence > 4:
        print("THIS IS YOUR WARNING, you have exceeded your allowed number of absences for your Ethics course , please go talk to your academic advisor")
        print("check with your Ethics doctor to see if you have failed this course")
def scholarship(student_id):#this function checks if the student is applicable to any scholarships
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
def Financial_Grades(student_id):#this function lets the student choose if he wants to see his GPA or finances
    f=["f","F"]
    g=["g","G"]
    while True:
        try:
            f_g = input("Would you like to check your Finances or your GPA?(f/g):")
            break
        except:
            print('Please enter letters')
    while f_g not in f and f_g not in g:
        while True:
            try:
                f_g = input('Please enter a valid answer:')
                break
            except:
                print('Please enter letters')
    if f_g in f:
        scholarship(student_id)
        restart=input("do you wish to restart?(y/n)")
        if restart == "y":
            Financial_Grades(student_id)
        elif restart== "n":
            exit()
    elif f_g in g:
        student_GPA=GPA_calculator(student_id)
        print("your GPA=",student_GPA)
        check_GPA(student_GPA)
        absence_warning(student_id)
        restart = input("do you wish to restart?(y/n)")
        if restart == "y":
            Financial_Grades(student_id)
        elif restart == "n":
            exit()
def Student_portal():#this function runs the entire student portal
    group1_id = [202201, 202202, 202203, 202204, 202205]
    group2_id = [202206, 202207, 202208, 202209, 202210]
    student_id=int(input("Enter your student id here:"))
    while student_id not in group1_id and student_id not in group2_id:
        student_id=int(input("Please enter a correct id:"))
    Financial_Grades(student_id)

