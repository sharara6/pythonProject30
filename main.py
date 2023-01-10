import teacher



def student_teacher(s_t):
    t= ['t','T']
    s= ['s','S']
    if s_t in t:
        return 'teacher' #teacher portal
    elif s_t in s:
        return "student" #student portal
    while s_t not in t or s:
        s_t = input('Please enter a valid answer:')


#######
#missing functions
#######