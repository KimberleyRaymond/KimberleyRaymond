#A 
str0 = "py"
print(str0[0]) # Only printed p 
print(str0[-1]) # Only printed y 
print(str0[:]) # printed both "py" 
print(str0[0], str0[-1], #even letter were in a colllum by itself, p by itself,y by it self and py together. 
str0[:], sep = ' ')
#B 
print('C'[0]) # C was printed by itself 
print("C"[-1]) # C was printed by itself 
print('C'[:]) # C was printed by itself
print('C'[0], 'C'[-1], # C was printed by itself three times 
'C'[:], sep = '\t')
#C 
str1 = 'coDE' 
print(str1.capitalize()+'\n'+str1.upper()+'\n'+str1.lower()) #Code was printing with different letters thats capatalized. 
print(str1)
#D 
str2 = "computer science" 
print(str2.title(),'|',str2[0:8],'|',str2[:3],'|', #Computer sceince was broken up in different words in colloums twice in a row  
str2[-5:-1], '|', str2[-2:] ) 
print(str2.title(), str2[0:8], str2[:3], 
str2[-5:-1], str2[-2:], sep = ' | ')
#E
str3 = "mississippi" 
print("i =",str3.count('i')) #This line gave the number even letter was in i was in the 4 
print("s = index[", str3.find('s'), ']') # this line talks about the position s was in 
print('p = ', str3.rfind('p')) # P position 
print("Miss = ", str3.find("Miss"))
#F
str4 = " Today's program " 
print('lstrip():',str4.lstrip()) # Todays program was writted the same for all 
print('rstrip():',str4.rstrip())
print('strip():',str4.strip() + " – Basic IO")
#G 
print("Price: ", '$', 19.99) # the pice was written with the doollar sign $19.99 
print("Price: ", '$', 19.99, sep = '')
#H 
print('Py', 'th', 'on', sep = '') # the word phyton was together 
print('Py', 'th', 'on', sep = '\t') # the words in seperated 
print('Py', 'th', 'on', sep = '\n') # The words are in different rows in two
#I 
print('tic', 'tac', 'toe', sep = '-', end = ' ') 
print("game starts", end = '!\n') 
print('in'.title(), 'person'.capitalize(), sep = '-', end = ' ') # it was printed as tic-tac-toe game starts! In-Person TUTORING 
print('tutoring'.upper()) # tutoring written as uppercase
#J 
print("Number\tSquare") 
print(str(2) + '\t' + str(2**2)) # numbers were in colloums and they were counting by 2 because they are squared 
print(str(3) + '\t' + str(3**2))
print(2, '\t', 2**2)
print(3, '\t', 3**2)
#K
print("STATE\tCAPITAL".expandtabs(15)) 
print('North Dakota\tBismarck'.expandtabs(15)) 
print('South Dakota\tPierre'.expandtabs(15)) 
print('Ohio\tColumbus'.expandtabs(15))
print('North Dakota\tBismarck') 
print('South Dakota\tPierre') 
print('Ohio\tColumbus')



