def get_input_int(prompt = "Enter Your choice: "):
    user_input = input(prompt).strip()
    while not user_input.isdigit():
        user_input = input(prompt).strip()
    return int(user_input)
def get_str(prompt = "Enter Your choice: "):
    user_input = input(prompt).strip()
    while not user_input.isalpha():
        user_input = input(prompt).strip()
    return user_input

def is_email(p: str):
    return "@" in p