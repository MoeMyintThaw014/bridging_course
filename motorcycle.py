motorcycles=['honda', 'yahma', 'suzuki']
print(motorcycles)

#changing
motorcycles[0]='ducati'
print(motorcycles)

#adding new one
motorcycles.append('honda')
print(motorcycles)

#adding all
motorcycles=[]
motorcycles.append('honda')
motorcycles.append('ýahma')
motorcycles.append('suzuki')
print(motorcycles)

#inserting
motorcycles.insert(0,'ducati')
print(motorcycles)

#removing
del motorcycles[3]
print(motorcycles)

#popped removing the last one
popped_motorcycles = motorcycles.pop()
print(f"popped motorcycles {popped_motorcycles}")

#popped with position 
print(motorcycles)
print(f"popped element {motorcycles.pop(0)}")
print(f"Remaining element {motorcycles}")


