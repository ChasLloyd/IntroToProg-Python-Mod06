# ========================================================================== 79
# FILE: Assignment06.py
#
# TITLE: Assignment 6 for UW "Foundations of Python" Course
#
# DESCRIPTION: Program demonstrates the use of functions, classes, and script
# organization following the "separation of concerns" design pattern
#
# CHANGE LOG:
#   11/11/25: Created overall program structure, drawing from two scripts:
#   Assignment06_Starter from RRoot,1/1/2030, and
#   Assignment05 script by Charles Lloyd, 11/4/2025
#   Created classes & moved code from the body of the starter script into the
#   corresponding methods
#
#   11/18/25: Charles Lloyd, Created external documentation while making minor
#   updates to the script
#
#        1         2         3         4         5         6         7        7
# ====== 0 ======= 0 ======= 0 ======= 0 ======= 0 ======= 0 ======= 0 ====== 9


# DIRECTIVES - DIRECTIVES - DIRECTIVES - DIRECTIVES - DIRECTIVES - DIRECTIVES
import _io
import json


# DATA LAYER - DATA LAYER - DATA LAYER - DATA LAYER - DATA LAYER - DATA LAYER
# Constants -- Constants -- Constants -- Constants -- Constants -- Constants
MENU: str = '''
------ Course Registration Program ------
  Select from the following menu:  
    1. Register a Student for a Course
    2. Show current data
    3. Save data to a file
    4. Exit the program
-----------------------------------------
'''

FILE_NAME: str = "Enrollments.json"


# Variables - Variables - Variables - Variables - Variables - Variables
menu_choice: str = ''   # Hold the menu choice made by the user.
students: list = []     # Table of student data

# file = None  # Holds a reference to an opened file.



# PROCESSING LAYER - PROCESSING LAYER - PROCESSING LAYER - PROCESSING LAYER
class FileProcessor:
    """ Methods relating to  file input/output & processing
    CHANGE LOG: 11/11/25, Charles Lloyd, Class and methods created
    """

    @staticmethod
    def read_data_from_file(file_name: str, students_data: list) -> list:
        """ Read JSON file and puts in table of dictionary rows.
        CHANGE LOG: 11/11/25, Charles Lloyd, created
        """
        file = _io.TextIOWrapper
        try:
            file = open(file_name, "r")
            students_data = json.load(file)
            file.close()
        except Exception as e:
            IO.output_error_messages(message=
                    "There was a problem with reading the file.", error=e)
        finally:
            if file.closed == False:
                file.close()
        return students_data


    @staticmethod
    def write_data_to_file(file_name: str, students_data: list) -> None:
        """ Write stud_dat (list of dictionary rows) to JSON file
        CHANGE LOG: 11/11/25, Charles Lloyd, created
        """
        file = _io.TextIOWrapper
        try:
            file = open(file_name, "w")
            json.dump(students_data, file, indent=2)
            file.close()
        except Exception as e:
            IO.output_error_messages(message=
                    "There was a problem with writing to the file.\n"
               "Check that file is not open by another program", error=e)
        finally:
            if file.closed == False:
                file.close()


# PRESENTATION LAYER ------- PRESENTATION LAYER ------- PRESENTATION LAYER
class IO:
    """ Methods relating to user interface
    CHANGE LOG: 11/11/25, Charles Lloyd, Class and methods created
    """

    @staticmethod
    def input_menu_choice() -> str:
        """ Method queries user for and collects menu choice
        CHANGE LOG:
        11/11/25, Charles Lloyd, created
        """
        selection = input("Please enter selection, 1 to 4: ")
        return selection


    @staticmethod
    def input_student_data(students_data: list) -> list:
        """ Method collects first, last, and course names from user
        Custom error messages are raised for numeric errors
        CHANGE LOG:
        11/11/25, Charles Lloyd, adapted from method by RRoot
        """
        stud_dat = {}   # Data for a single student
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("Please use only alphabetic characters "
                                 "for the first name.\n")

            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("Please use only alphabetic characters "
                                 "for the last name.\n")

            course_name = input("Enter the name of the course: ")

            stud_dat = {"FirstName": student_first_name,
                            "LastName": student_last_name,
                            "CourseName": course_name}

            students_data.append(stud_dat)
            print(f"You have registered {student_first_name} "
                                 f"{student_last_name} for {course_name}.")

        except ValueError as e:
            IO.output_error_messages(e, error=None)

        finally:
            pass

        return students_data


    @staticmethod
    def output_menu(menu: str) -> None:
        """ Method presents menu choices to user
        CHANGE LOG:
        11/11/25, Charles Lloyd, created
        """
        # Present the menu of choices
        print(menu)


    @staticmethod
    def output_student_courses(student_data: list, print_style: str) -> None:
        """ Method prints current student registration data in three styles:
        print_style = 1: Includes keys, quotes, and brackets
        print_style = 2: Includes explanatory text
        print_style = 3: Comma separated values, no keys, quotes or brackets
        CHANGE LOG:
        11/11/25, Charles Lloyd, created
        """

        print("\n------------------ Current Data ------------------")
        if print_style == '1':
            for row in student_data:
                print(row)
        elif print_style == '2':
            for row in student_data:
                print(f'Student {row["FirstName"]} '
                f'{row["LastName"]} is enrolled in {row["CourseName"]}')
        else:
            for row in student_data:
                print(f'{row["FirstName"]},{row["LastName"]},'
                                                   f'{row["CourseName"]}')
        print("-" * 50)


    @staticmethod
    def output_error_messages(message: str, error: Exception = None) -> None:
        """ Method displays custom and Python-generated error messages
            message: String with the custom message
            error: Exception object containing technical message from Python
        CHANGE LOG:
        11/11/25, Charles Lloyd, created, adapted from method by RRoot
        """
        print("-- Custom Error Message -- ")
        print(message, end="\n\n")      # Custom message
        if error is not None:           # Messages from Python
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')



# BODY ------- BODY ------- BODY ------- BODY ------- BODY ------- BODY

# Read the JSON file into a list of dictionaries (table)
students = FileProcessor.read_data_from_file(file_name=FILE_NAME,
                                                  students_data=students)

# Present menu, obtain selection, keep looping until break out in Option 4
while True:
    # Print the menu
    IO.output_menu(menu=MENU)

    # Obtain the menu selection
    menu_choice = IO.input_menu_choice()

    if menu_choice == "1":   # Input user data
        students = IO.input_student_data(students_data=students)
        continue

    elif menu_choice == "2":    # Present the current data
        style = '3'   # Select the style for listing the data
        IO.output_student_courses(students, print_style=style)
        continue

    elif menu_choice == "3":    # Save the data to a file
        FileProcessor.write_data_to_file(file_name=FILE_NAME,
                                                 students_data=students)
        continue

    elif menu_choice == "4":    # Exit the program
        break  # out of the while loop

    else:
        print("Invalid menu choice\n")

print("Program Ended Without Crashing!")

