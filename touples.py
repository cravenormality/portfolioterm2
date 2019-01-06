game_list = ["Sudoku",
    "Pokemon Ruby",
    "Cards Against Humanity",
    "God Of War",
    "Pokemon Black",
    "Overwatch",
    "Red Dead Redemption",
    "assassin's creed",
    "Pokemon Heartgold",
    "Call of Duty Blacks Ops"]
print(len(game_list))
num5game=game_list[4]
print(num5game)
middle5 = game_list[3:7]
print(middle5)
last4 = game_list[6:]
print(last4)
evens = game_list[::2]
print(evens)
backward = game_list[::-1]
print(backward)
for i in game_list:
    print(i)
print(game_list)
game_list +=("11",12,13.0,14,"15")
print(game_list)
game_list[0]="Pokemon Ruby"
game_list[1]="Sudoku"
print(game_list)
