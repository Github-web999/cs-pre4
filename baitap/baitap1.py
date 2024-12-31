import colorama
from colorama import Fore, Style

class Course:
    def __init__(self, course_id, course_name, mode, fee):
        self.course_id = course_id
        self.course_name = course_name
        self.mode = mode
        self.fee = fee

    def course_info(self):
        return f"Course ID: {self.course_id}, Name: {self.course_name}, Mode: {self.mode}, Fee: {self.fee} VND"


class Student:
    def __init__(self, student_id, student_name, birth_date):
        self.student_id = student_id
        self.student_name = student_name
        self.birth_date = birth_date
        self.enrolled_courses = []

    def register_course(self, course):
        if course not in self.enrolled_courses:
            self.enrolled_courses.append(course)
            print(Fore.GREEN + f"Student {self.student_name} successfully registered for the course {course.course_name}." + Style.RESET_ALL)
        else:
            print(Fore.YELLOW + f"The course {course.course_name} has already been registered." + Style.RESET_ALL)

    def cancel_course(self, course_id):
        for course in self.enrolled_courses:
            if course.course_id == course_id:
                self.enrolled_courses.remove(course)
                print(Fore.GREEN + f"Student {self.student_name} successfully canceled the course {course.course_name}." + Style.RESET_ALL)
                return
        print(Fore.RED + f"Course with ID {course_id} is not found in the registered list." + Style.RESET_ALL)

    def display_courses(self):
        if not self.enrolled_courses:
            print(Fore.YELLOW + f"Student {self.student_name} has not registered for any courses." + Style.RESET_ALL)
            return
        print(Fore.CYAN + f"Student {self.student_name} has registered for the following courses:" + Style.RESET_ALL)
        for course in self.enrolled_courses:
            print(f" - {course.course_name} ({course.mode}, {course.fee} VND)")


def display_all_courses():
    if not course_list:
        print(Fore.YELLOW + "No courses available." + Style.RESET_ALL)
        return
    print(Fore.CYAN + "Available Courses:" + Style.RESET_ALL)
    for course in course_list.values():
        print(Fore.BLUE + course.course_info() + Style.RESET_ALL)


def display_all_students():
    if not student_list:
        print(Fore.YELLOW + "No students available." + Style.RESET_ALL)
        return
    print(Fore.CYAN + "Registered Students:" + Style.RESET_ALL)
    for student in student_list.values():
        print(Fore.BLUE + f"Student ID: {student.student_id}, Name: {student.student_name}, Birth Date: {student.birth_date}" + Style.RESET_ALL)


colorama.init(autoreset=True)

course_list = {
    "C01": Course("C01", "Python Programming", "Offline", 3750000),
    "C02": Course("C02", "Web Development", "Online", 5560000),
}

student_list = {
    "S01": Student("S01", "Alice Nguyen", "2003-12-07"),
    "S02": Student("S02", "Bob Tran", "2001-05-09"),
}

while True:
    print(Fore.MAGENTA + "\nCommands:" + Style.RESET_ALL)
    print(" - 'add course course_id course_name mode fee' to add a new course")
    print(" - 'add student student_id student_name birth_date' to add a new student")
    print(" - 'register student_id course_id' to register a student for a course")
    print(" - 'cancel student_id course_id' to cancel a course for a student")
    print(" - 'display courses' to show all available courses")
    print(" - 'display students' to show all registered students")
    print(" - 'display student_courses student_id' to show a student's registered courses")
    print(" - 'exit' to quit the program")

    command = input(Fore.YELLOW + "\nEnter command: " + Style.RESET_ALL).strip().lower()
    if command == "exit":
        print(Fore.GREEN + "Exiting the program. Goodbye!" + Style.RESET_ALL)
        break

    parts = command.split()
    if not parts:
        print(Fore.RED + "Invalid command. Please try again." + Style.RESET_ALL)
        continue

    action = parts[0]

    if action == "add":
        if len(parts) < 2:
            print(Fore.RED + "Specify what to add: 'course' or 'student'." + Style.RESET_ALL)
            continue
        sub_action = parts[1]

        if sub_action == "course":
            if len(parts) < 5:
                print(Fore.RED + "Invalid format. Use: 'add course course_id course_name mode fee'." + Style.RESET_ALL)
                continue
            course_id, course_name, mode, fee = parts[2], parts[3], parts[4], " ".join(parts[5:])
            if course_id in course_list:
                print(Fore.RED + f"Course ID {course_id} already exists." + Style.RESET_ALL)
                continue
            course_list[course_id] = Course(course_id, course_name, mode, fee)
            print(Fore.GREEN + f"Course {course_name} added successfully." + Style.RESET_ALL)

        elif sub_action == "student":
            if len(parts) < 5:
                print(Fore.RED + "Invalid format. Use: 'add student student_id student_name birth_date'." + Style.RESET_ALL)
                continue
            student_id, student_name, birth_date = parts[2], parts[3], " ".join(parts[4:])
            if student_id in student_list:
                print(Fore.RED + f"Student ID {student_id} already exists." + Style.RESET_ALL)
                continue
            student_list[student_id] = Student(student_id, student_name, birth_date)
            print(Fore.GREEN + f"Student {student_name} added successfully." + Style.RESET_ALL)

        else:
            print(Fore.RED + "Invalid option. Use 'course' or 'student'." + Style.RESET_ALL)

    elif action == "register":
        if len(parts) < 3:
            print(Fore.RED + "Invalid format. Use: 'register student_id course_id'." + Style.RESET_ALL)
            continue
        student_id, course_id = parts[1], parts[2]
        if student_id not in student_list:
            print(Fore.RED + f"Student ID {student_id} does not exist." + Style.RESET_ALL)
            continue
        if course_id not in course_list:
            print(Fore.RED + f"Course ID {course_id} does not exist." + Style.RESET_ALL)
            continue
        student_list[student_id].register_course(course_list[course_id])

    elif action == "cancel":
        if len(parts) < 3:
            print(Fore.RED + "Invalid format. Use: 'cancel student_id course_id'." + Style.RESET_ALL)
            continue
        student_id, course_id = parts[1], parts[2]
        if student_id not in student_list:
            print(Fore.RED + f"Student ID {student_id} does not exist." + Style.RESET_ALL)
            continue
        student_list[student_id].cancel_course(course_id)

    elif action == "display":
        if len(parts) < 2:
            print(Fore.RED + "Specify what to display: 'courses', 'students', or 'student_courses'." + Style.RESET_ALL)
            continue
        sub_action = parts[1]

        if sub_action == "courses":
            display_all_courses()

        elif sub_action == "students":
            display_all_students()

        elif sub_action == "student_courses":
            if len(parts) < 3:
                print(Fore.RED + "Specify a student ID. Use: 'display student_courses student_id'." + Style.RESET_ALL)
                continue
            student_id = parts[2]
            if student_id not in student_list:
                print(Fore.RED + f"Student ID {student_id} does not exist." + Style.RESET_ALL)
                continue
            student_list[student_id].display_courses()

        else:
            print(Fore.RED + "Invalid option. Use 'courses', 'students', or 'student_courses'." + Style.RESET_ALL)

    else:
        print(Fore.RED + "Invalid command. Please try again." + Style.RESET_ALL)
