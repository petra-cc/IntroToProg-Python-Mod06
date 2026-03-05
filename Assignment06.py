# ------------------------------------------------------------------------------------------ #
# Title: Assignment06
# Desc: This assignment demonstrates using functions
# with structured error handling
# Change Log: (Who, When, What)
#   Petra Chinsangaram, 2/28/2026, Created Script
# ------------------------------------------------------------------------------------------ #
import json

# Define the Data Constants
MENU: str = """
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
"""
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables
menu_choice: str = ""  # Hold the choice made by the user.
students: list = []  # a table of student data


# Processing layer
class FileProcessor:
    """
    A collection of processing layer functions that work with JSON files

    ChangeLog: (Who, When, What)
    Petra Chinsangaram, 2.28.2026, Created Class and Added Functions
    """

    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """
        This function reads and stores the data from the JSON file

        :param file_name: string containing the name of the file
        :param student_data: list of dictionaries containing student data
        :return: list of dictionaries containing student data
        """
        try:
            file = open(file_name, "r")
            student_data = json.load(file)
        except Exception as e:
            IO.output_error_messages(message="Error: There was a problem "
                                     "with reading the file.\n"
                                     "Please check that the file exists "
                                     "and that it is in a json format.",
                                     error=e)
        finally:
            # Check if a file object exists and is still open
            if file is not None and file.closed == False:
                file.close()
        return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """
        This function writes the current student data to the JSON file

        :param file_name: string containing the name of the file
        :param student_data: list of dictionaries containing student data
        :return: None
        """
        try:
            file = open(file_name, "w")
            json.dump(student_data, file, indent=2)
        except Exception as e:
            IO.output_error_messages(message="Error: There was a problem "
                                     "with writing to the file.\n"
                                     "Please check that the file "
                                     "is not open by another program.",
                                     error=e)
        finally:
            # Check if a file object exists and is still open
            if file is not None and file.closed == False:
                file.close()


# Presentation layer
class IO:
    """
    A collection of presentation layer functions
    that manage user input and output

    ChangeLog: (Who, When, What)
    Petra Chinsangaram, 2.28.2026, Created Class and Added Functions
    """

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """
        This function displays a custom error message to the user

        :param message: string containing the custom error message
        :param error: exception called by try/except block
        :return: None
        """
        print(message)
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep="\n")

    @staticmethod
    def output_menu(menu: str):
        """
        This function displays the menu of choices to the user

        :param menu: string containing the menu
        :return: None
        """
        print()
        print(menu)
        print()

    @staticmethod
    def input_menu_choice():
        """
        This function collects the user's menu choice

        :return: string containing the user's menu choice
        """
        try:
            choice = input("What would you like to do: ")
            if choice not in ("1", "2", "3", "4"):
                raise Exception("Please, only choose 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(message=e.__str__())
        return choice

    @staticmethod
    def output_student_courses(student_data: list):
        """
        This function displays the list of students to the user

        :param student_data: list of dictionaries containing student data
        :return: None
        """
        print("-" * 50)
        for student in student_data:
            print(f"Student {student["FirstName"]} {student["LastName"]} "
                  f"is enrolled in {student["CourseName"]}")
        print("-" * 50)

    @staticmethod
    def input_student_data(student_data: list):
        """
        This function collects the student's
        first name, last name, and course name from the user

        :param student_data: list of dicts containing previous student data
        :return: list of dicts containing previous and new student data
        """

        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("Error: The first name "
                                 "should not contain numbers.")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("Error: The last name "
                                 "should not contain numbers.")
            course_name = input("Please enter the name of the course: ")
            student_dict = {"FirstName": student_first_name,
                            "LastName": student_last_name,
                            "CourseName": course_name}
            student_data.append(student_dict)
            print(f"You have registered {student_first_name} "
                  f"{student_last_name} for {course_name}.")
        except ValueError as e:
            IO.output_error_messages(message=e.__str__(), error=e)
        except Exception as e:
            IO.output_error_messages(message="Error: There was a problem "
                                     "with your entered data.", error=e)
        return student_data


# Main body of the script
# Extract the data from the file
students = FileProcessor.read_data_from_file(file_name=FILE_NAME,
                                             student_data=students)

# Present and Process the data
while (True):

    # Present the menu of choices and collect the user's choice
    IO.output_menu(menu=MENU)
    menu_choice = IO.input_menu_choice()

    # Input user data
    if menu_choice == "1":

        students = IO.input_student_data(student_data=students)
        continue

    # Present the current data
    elif menu_choice == "2":

        IO.output_student_courses(student_data=students)
        continue

    # Save the data to a file
    elif menu_choice == "3":

        FileProcessor.write_data_to_file(file_name=FILE_NAME,
                                         student_data=students)
        IO.output_student_courses(student_data=students)
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop

print("Program Ended")
