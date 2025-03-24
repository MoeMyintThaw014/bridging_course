squares=[]
for value in range(1,11):
    square = value**2
    squares.append(square)
print(f"Square list\n{squares}")

tubes=[]
for value in range(1,11):
    tube = value**3
    tubes.append(tube)
    #tubes.append(value ** 3)
print(f"Tube list\n{tubes}")

digit=[1,2,3,4,5,6,7,8,9,10]
print(f"{min(digit)}")
print(f"{max(digit)}")
#list comprehension
square_list=[value ** 2 for value in range (1,11)]
print(square_list)
