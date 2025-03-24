threes=list(range[3,31,3])
for three  in threes:
    print (three)
    
cubes=[]
for value in range(1,11):
    cubes.append(value **3)
print ("First ten cubes")
print (cubes)
cube_list =[value **3 for value in range(1,11)]
print("using list comprehension-cun list")
print(cube_list)