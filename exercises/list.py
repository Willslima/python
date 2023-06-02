notes = [8,9,8.5]
#list

notes.append(6) 
#add a number to list
 
print(notes)

notes.sort() 
#sorting the list of minor to major

print('of minor to major',notes) 

notes.sort(reverse=True) 
#sorting reverse

print('sorting reverse',notes) 

notes.pop() 
#exclude last position
print(notes)

notes.pop(1)
print(notes)

notes.insert(2,5)
#first arg position, second arg is the data
#insert data on any position

print(notes)