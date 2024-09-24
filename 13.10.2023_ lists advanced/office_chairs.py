def check_the_rooms(number_of_rooms):
    free_chair = 0
    for number_of_room in range(1, number_of_rooms + 1):
        chairs, visitors = input().split()
        difference = len(chairs) - int(visitors)
        if difference < 0:
            print(f"{abs(difference)} more chairs needed in room {number_of_room}")
        free_chair += difference
    return free_chair


count_of_rooms = int(input())
total_free_chairs = check_the_rooms(count_of_rooms)
if total_free_chairs >= 0:
    print(f"Game On, {total_free_chairs} free chairs left")


def check_chairs(n):
    total_free_chairs = 0
    game_on = True  # Флаг, който проверява дали в някоя стая има недостиг на столове

#     # Обхождаме всяка стая
#     for room in range(1, n + 1):
#         # Въвеждаме информация за стаята
#         data = input(f"Room {room}: ").split()
#
#         chairs = data[0].count('X')  # Брой на столовете в стаята
#         visitors = int(data[1])  # Брой на посетителите в стаята
#
#         # Проверка дали има достатъчно столове
#         if chairs < visitors:
#             needed_chairs = visitors - chairs
#             print(f"{needed_chairs} more chairs needed in room {room}")
#             game_on = False  # Вдигаме флага, че има стая с недостатъчно столове
#         else:
#             total_free_chairs += chairs - visitors
#
#     # Ако във всички стаи има достатъчно столове
#     if game_on:
#         print(f"Game On, {total_free_chairs} free chairs left")
#
#
# # Въвеждаме броя на стаите
# n = int(input("Enter the number of rooms: "))
# check_chairs(n)
