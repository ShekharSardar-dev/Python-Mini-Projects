#code for student report card system

def fun_grade(percent):
    if percent >= 90:
        return 'A'
    elif percent >= 75:
        return 'B'
    elif percent >= 60:
        return 'C'
    elif percent >= 40:
        return 'D'
    else:
        return 'F'

    
def add_student(students_list):
    #adding student
    marks_tuple = ()
    student_dict = {}
    total = 0

    student_dict['name'] = input("Enter Student Name: ").lower()

    sub = ['Maths', 'Science', 'English']
    #loop for inputing marks
    for i in range(3):
        mark = int(input(f"Enter {sub[0]} Marks: "))
        marks_tuple = marks_tuple + (mark,)
        total += marks_tuple[i]

    percent = round(total / 3, 2)
    grade = fun_grade(percent) #using fun_grade() to calculate garde

    student_dict['marks'] = marks_tuple
    student_dict['total'] = total
    student_dict['percentage'] = percent
    student_dict['grade'] = grade

    students_list.append(student_dict)
    print("Student Data Added Succesfully!")

def display_students(students_list):
    #displaying all students
    if 0 < len(students_list):
        print("Student Details: ")
        print("Name    Maths    Science    English     Total Marks     Percent%    Grade")
        for item in students_list:
            print(f"{item['name']}      {item['marks'][0]}      {item['marks'][1]}      {item['marks'][2]}      {item['total']}     {item['percentage']}    {item['grade']}")

    else:
        #exception handling
        print("No Students Details Available!")
        print("Please Add Student Data!")
    
def search_student(students_list):
    #searching student
    if 0 < len(students_list):
        name = input("Enter Student Name: ").lower()

        count = 0

        for item in students_list:
            if name == item['name']:
                print("Name    Maths    Science    English     Total Marks     Percent%    Grade")
                print(f"{item['name']}      {item['marks'][0]}      {item['marks'][1]}      {item['marks'][2]}      {item['total']}     {item['percentage']}    {item['grade']}")

            else:
                pass
                count += 1

        if count == len(students_list):
            print(f"No Data Available for {name}!")
    else:
        #exception handling
        print("No Students Details Available!")
        print("Please Add Student Data!")

def find_topper(students_list):
    #finding topper
    if 0 < len(students_list):
        highest = students_list[0]['marks'][0]
        for item in range(len(students_list)):
            if students_list[item]['marks'][item] >= highest:
                highest = students_list[item]['marks'][item]

        for item in range(len(students_list)):
            if highest == students_list[item]['marks'][item]:
                print("Topper Student: ")
                print("Name    Maths    Science    English     Total Marks     Percent%    Grade")
                print(f"{students_list[item]['name']}      {students_list[item]['marks'][0]}      {students_list[item]['marks'][1]}      {students_list[item]['marks'][2]}      {students_list[item]['total']}     {students_list[item]['percentage']}    {students_list[item]['grade']}")
                break
    else:
        #exception handling
        print("No Students Details Available!")
        print("Please Add Student Data!")

def student_report():

    #empty list
    students = []

    while True:
        print("=====STUDENT REPORT CARD=====\n")

        print("1. Add Student")
        print("2. Display All Students")
        print("3. Search Student")
        print("4. Find Topper")
        print("5. Exit")

        choice = input("Choose an option(1-5): ")

        #using match case for selecting conditions
        match choice:
            case '1':
                #function call for add_student
                add_student(students)

            case '2':
                #function call for display_students
                display_students(students)

            case '3':
                #function call for search_student
                search_student(students)

            case'4':
                #function call for find_topper
                find_topper(students)

            case '5':
                #function call for exit
                print("Exiting the Program...")
                print("Program Exited Successfully!")
                exit()

            case _:
                print("Invalid Input!, Please Enter from the given options! ")

student_report()