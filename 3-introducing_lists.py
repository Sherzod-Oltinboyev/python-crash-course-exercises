# Author: Sherzod Oltinboyev:
# Date: 15.12.2020:
# Theme: 3 Introducing lists:

# 3-1.Names:
names=['Abdurasul','Islom','Lochin','Ixtiyor','Oybek']
print(names)
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4])

# 3-2.Gretings:
names=['Abdurasul','Islom','Lochin','Ixtiyor','Oybek']
print(names)
print("Hello my friend "+names[0])
print("Hello my friend "+names[1])
print("Hello my friend "+names[2])
print("Hello my friend "+names[3])
print("Hello my friend "+names[4])

# 3-3.Your Own List:
cars=['Mercedes Benz G63','Rols Roys','Ferrari',]
print("I would like to own a "+cars[0]+' car')

# Author: Sherzod Oltinboyev:
# Date: 16.12.2020:
# Theme: 3 Introducing Lists
# Started Time: 10:20

# 3-4.Guest List:
guest=['Sardor','Ixtiyor','Oybek','Akbar']
print("I would like to invite " +guest[0]+ " to my dinner")
print("I would like to invite " +guest[1]+ " to my dinner")
print("I would like to invite " +guest[2]+ " to my dinner")
print("I would like to invite " +guest[3]+ " to my dinner")

# 3-5.Changing Guest List:
guest=['Sardor','Ixtiyor','Oybek','Akbar']
guest[3]="Xurshid"
print("I would like to invite " +guest[0]+ " to my dinner")
print("I would like to invite " +guest[1]+ " to my dinner")
print("I would like to invite " +guest[2]+ " to my dinner")
print("I would like to invite " +guest[3]+ " to my dinner")

# 3-6. More Guests:
guest=['Sardor','Ixtiyor','Oybek','Akbar']
guest[3]="Xurshid"
guest.insert(0,"Lochin")
guest.insert(3, 'Abdurasul')
guest.append('Abdulaziz')
print("I would like to invite " +guest[0]+ " to my dinner")
print("I would like to invite " +guest[1]+ " to my dinner")
print("I would like to invite " +guest[2]+ " to my dinner")
print("I would like to invite " +guest[3]+ " to my dinner")
print("I would like to invite " +guest[4]+ " to my dinner")
print("I would like to invite " +guest[5]+ " to my dinner")
print("I would like to invite " +guest[6]+ " to my dinner")

# 3-7.Shrinking Guest List:
guest=['Sardor','Ixtiyor','Oybek','Akbar']
guest[3]="Xurshid"
guest.insert(0,"Lochin")
guest.insert(3, 'Abdurasul')
guest.append('Abdulaziz')
message1=guest.pop()
message2=guest.pop()
message3=guest.pop()
message4=guest.pop()
message5=guest.pop()
print("My guest list "+str(guest))
print("I would like to invite " +guest[0]+ " to my dinner")
print("I would like to invite " +guest[1]+ " to my dinner")
print(message1+". "+" Sorry,I can't invite you for my dinner.I have only two sits.")
print(message2+". "+" Sorry,I can't invite you for my dinner.I have only two sits.")
print(message3+". "+" Sorry,I can't invite you for my dinner.I have only two sits.")
print(message4+". "+" Sorry,I can't invite you for my dinner.I have only two sits.")
print(message5+". "+" Sorry,I can't invite you for my dinner.I have only two sits.")
del guest[1]
print("My guest list "+str(guest))
del guest[0]
print("My guest list "+str(guest))

# 3-8.Seeing the World:
countries=['France',"America",'Germany','Dubai','England']
print("Here is original order: ")
print("\t"+str(countries))
print("Here is alphabetical order: ")
print("\t"+str(sorted(countries)))
print("Here is again original order: ")
print("\t"+str(countries))
countries.reverse()
print("Here is reversed order: "+str(countries))
countries.reverse()
print("Here is again original order: "+str(countries))
countries.sort()
print("Sorted order: "+"\t"+str(countries))
countries.sort(reverse=True)
print("Original order again "+"\t"+str(countries))

#3-9.Dinner Guests:
guest=['Sardor','Ixtiyor','Oybek','Akbar']
guest[3]="Xurshid"
guest.insert(0,"Lochin")
guest.insert(3, 'Abdurasul')
guest.append('Abdulaziz')
print("Number of guests is "+str(len(guest)))

#3-10.
languages=['Uzbek','English','Russia','Arab','Tursia']
print("My native languages is "+languages[0])
print("My most used language is "+languages[1])
languages.append("Italian")
print(languages)
print("I am going to learn "+str(languages.append("Italian")))
best=languages.insert(4,"Hind")
print("Larger proportion of the world use "+str(best))

#3-11.Intentional Error:
languages=['Uzbek','English','Russia','Arab','Tursia']
print(languages[4])

# Finished time: 12:32 :






