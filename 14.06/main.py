import utils
import db.student_service

from logger_config import logger
options = [
    "create student",
    "get all students",
    "get by id",
    "delete by id",
    "update name by id",
    "get count students",
]

def main():
    user_choice = None
    while user_choice != len(options) +1:
        print("Welcome to student manager system")
        for (i, option) in enumerate(options):
            print(f"{i + 1}: {option}")
            
        print()
        user_choice = input("Enter Your choice: ")
        match user_choice:
            case "1":
                logger.info("Start case 1")
                name = utils.get_str("enter name: ")
                age = utils.get_input_int("enter age: ")
                course = utils.get_str("enter course: ")
                email = input("enter email: (optional)")
                if not utils.is_email(email):
                    email = None
                status = input("enter status: (optional)").strip()
                if len(status) == 0:
                    status = None
                id = db.student_service.create_student(name,age,course,email,status)
                if id:
                    print(f"Student created: id: {id}")
                else:
                    print("User not created.")
main()