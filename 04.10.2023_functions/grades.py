def grades():
    grades_data = float(input())
    if 2.00 <= grades_data <= 2.99:
        print("Fail")
    elif 3.00 <= grades_data <= 3.49:
        print("Poor")
    elif 3.50 <= grades_data <= 4.49:
        print("Good")
    elif 4.50 <= grades_data <= 5.49:
        print("Very Good")
    elif 5.50 <= grades_data <= 6.00:
        print("Excellent")


grades()

# grades_data = float(input())
#
#
# def grades():
#     if 2.00 <= grades_data <= 2.99:
#         return "Fail"
#     elif 3.00 <= grades_data <= 3.49:
#         return "Poor"
#     elif 3.50 <= grades_data <= 4.49:
#         return "Good"
#     elif 4.50 <= grades_data <= 5.49:
#         return "Very Good"
#     elif 5.50 <= grades_data <= 6.00:
#         return "Excellent"
#
#
# print(grades())
