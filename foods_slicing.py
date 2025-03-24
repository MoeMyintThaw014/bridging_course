my_food=['pizza','falafel','carrot cake']
friend_food=my_food[:]#only (:) is mean start from 0 index and stop at last index
print("My food list")
print(my_food)

print("friend food list")
print(friend_food)

my_food[0]='cheese pizza'
print(my_food)
print(friend_food)

my_food.append('cannoli')
print(my_food)

friend_food.append('ice cream')
print(friend_food)