def password_validator(password):

    letters_count = 0
    digits_count = 0
    symbol_count = 0

    if not 5 < len(password) < 11:
        print("Password must be between 6 and 10 characters")
    for el in password:
        if el.isalpha():
            letters_count += 1
        elif el.isdigit():
            digits_count += 1
        else:
            symbol_count += 1

    if symbol_count > 0:
        print("Password must consist only of letters and digits")
    if digits_count < 2:
        print("Password must have at least 2 digits")
    if 5 < len(password) < 11 and digits_count > 1 and symbol_count == 0:
        print("Password is valid")


user_pass = input()
password_validator(user_pass)


# def validate_password(password):
#     errors = []
#
#     if not (6 <= len(password) <= 10):
#         errors.append("Password must be between 6 and 10 characters")
#
#     if not password.isalnum():
#         errors.append("Password must consist only of letters and digits")
#
#     digit_count = sum(char.isdigit() for char in password)
#     if digit_count < 2:
#         errors.append("Password must have at least 2 digits")
#
#     if errors:
#         for error in errors:
#             print(error)
#     else:
#         print("Password is valid")
#
#
# password = input()
#
# validate_password(password)



# def password_validator():
#     password = input()
#     letters_list = []
#     digits_list = []
#     symbol_list = []
#
#     sum_of_characters = False
#     letters_and_digits = False
#     least_two_digits = False
#     for el in password:
#         if el.isalpha():
#             letters_list.append(el)
#         if el.isdigit():
#             digits_list.append(el)
#         if not el.isalpha() and not el.isdigit():
#             symbol_list.append(el)
#
#     if 5 < len(password) < 11:
#         sum_of_characters = True
#     else:
#         print("Password must be between 6 and 10 characters")
#     if len(letters_list) > 0 and len(symbol_list) < 1:
#         letters_and_digits = True
#     else:
#         print("Password must consist only of letters and digits")
#     if len(digits_list) > 1:
#         least_two_digits = True
#     else:
#         print("Password must have at least 2 digits")
#     if sum_of_characters and letters_and_digits and least_two_digits:
#         print("Password is valid")
#
#
# password_validator()
