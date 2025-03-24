location=['Taungyi', 'Inlay','Seoul','Tokyo', 'Paris', 'Egyp']
print(location)

print(sorted(location))
#orginal
print(f"Orginal list \n {location}\n")
#reverse
location.reverse()
print(f"Reverse order of the list \n {location}\n")
#second time reverse leads to orginal list order
location.reverse()
print(f"Second time reverse order of the list \n{location}\n")
#list according to alphabetical
location.sort()
print(f"after sorting in alphabetical order\n{location}\n")
#list decreasing order
location.sort(reverse=True)
print(f"after sorting with the decresing order \n{location}\n")

print(f"NUmber of plcae that I like to travel {len(location)}")

print (location[6])
print(location[-6])



