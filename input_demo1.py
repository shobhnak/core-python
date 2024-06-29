student_name = input("Enter student name :")
student_age =int(input("Enter the student age :"))
student_course =input("Enter the  student course :")
print("the name of student is {0} and age is {1}".format(student_name,student_age))

"""
    Remember :
    input function always store the value in form of string
f
"""
    
    #Example
    
print("student_age is type of",type(student_age))
    
    
if student_age >=18:
        if student_age > 18 and student_age <=25:
            if student_course == "desd":
                print("Hello {student_name} you are lucky to get admission in one of the best courese of ACTS")
                
            elif student_course != "desd" :
              print("you might strugle to get placed")
            else:
                pass
              
          
                  
    