team_a = ['A-1', 'A-2', 'A-3', 'A-4', 'A-5', 'A-6', 'A-7', 'A-8', 'A-9', 'A-10', 'A-11']
team_b = ['B-1', 'B-2', 'B-3', 'B-4', 'B-5', 'B-6', 'B-7', 'B-8', 'B-9', 'B-10', 'B-11']
red_cart = input().split()
index = 0
game_was_terminated = False
while index < len(red_cart):
    if red_cart[index] in team_a:
        removed_el = team_a.remove(red_cart[index])

    if red_cart[index] in team_b:
        removed_el = team_b.remove(red_cart[index])
    index += 1

    if len(team_a) < 7 or len(team_b) < 7:
        game_was_terminated = True
        break
print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
if game_was_terminated:
    print("Game was terminated")





# team_a = ["B-" + str(x) for x in range(1, 12)]
# print(team_a)
