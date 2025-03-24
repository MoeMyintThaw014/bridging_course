friends=['Kelvin', 'Lily', 'Mia', 'Sophia']
print(f"Please join dinner together {friends[0]}")
print(f"Please join dinner together {friends[1]}")
print(f"Please join dinner together {friends[2]}")
print(f"Please join dinner together {friends[3]}")

print(f"{friends[1]} can't join the dinner")
friends[2]="Emma"
print(f"Please join the dinner tonight {friends[0]}")
print(f"Please join the dinner tonight {friends[1]}")
print(f"Please join the dinner tonight {friends[2]}")
print(f"Please join the dinner tonight {friends[3]}")

friends= ['Emma', 'Lily', 'Charl']
print("Wow we've got a bigger dinner table")
friends.insert(0, 'Yuya')
friends.insert(2, 'Harry')
friends.append('SuSu')
print(f"{friends[0]}, please join the dinner tonight")
print(f"{friends[1]}, please join the dinner tonight")
print(f"{friends[2]}, please join the dinner tonight")
print(f"{friends[3]}, please join the dinner tonight")
print(f"{friends[4]}, please join the dinner tonight")

print("Unlickily, there is only two people we can stay")
print(f"{friends.pop()}, We are sorry")
print(f"{friends.pop()}, We are sorry")
print(f"{friends.pop()}, We are sorry")

print(f"{friends[0]}, you are still invited")
print(f"{friends[1]}, you are still invited")
del friends[0]
print(friends)




