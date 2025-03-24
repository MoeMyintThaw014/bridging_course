players=['charles','michel','eli','tom','jerry']
print(players[0:3])
#start from 0 and end in 3
players=['charles','michel','eli','tom','jerry']
#start from position 1 and end in 4 
print(players[1:4])
print(players[0:5])
print(players[0])
print(players[1])
print(players[2])
print(players[3])
print(players[4])
some_players=players[0:3]
print(some_players)
print(players[:4])
#start index(:) is default index that start from first item room zero
print(players[2:])
#omitting stop index (:) is will default end at the last item
#item order 0,1,2,3,4 backward order -1,-2,-3,-4
print(players[-3:])
print(players[:-2])

print("Here are the first three players on my team")
for player in players[:3]:
    print(player.title())
