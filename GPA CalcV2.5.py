while True:
    print("GPA grade calculator")
    gpa = float(input("Enter marks: "))
    if gpa in range(80, 100):
        print("You got an A+")
    elif gpa in range(70, 79):
        print("You got an A")
    elif gpa in range(60, 69):
        print("You got an A-")
    elif gpa in range(50, 59):
        print("You got a B")
    elif gpa in range(40, 49):
        print("You got a D")
    elif gpa in range(0, 39):
        print("You got a F")
    else:
        print("Invalid")
