my_food=['pizza','falafel','carrot cake']
friend_food=my_food[:]
my_food.append('cheese pizza')
friend_food.append('pineapple pizza')

print("My fav foods are:")
for pizza in my_food:
    print(pizza)

print("My friend fav foods are:")
for pizza in friend_food:
    print(pizza)