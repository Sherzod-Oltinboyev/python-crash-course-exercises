# Author: Sherzod Oltinboyev:
# Date: 21.12.2020:
# Theme: 6-Dictionary:

# 6-1. Person;
info={'first_name': 'Anvar', 'last_name': 'Xudoyberdiyev', 'age': "18", 'city': 'Djizakh'}
print(info['first_name'])
print(info['last_name'])
print(info['age'])
print(info['city'])

# 6-2. Favourite Numbers:
favourite_numbers={
    'ilhom':'5',
    'islom':'7',
    'lochin':'3',
    "ulug'bek":'8',
    'abdurasul':'6',
}
print("Ilhom's favourite number is "+favourite_numbers['ilhom'].title()+'.')
print("Islom's favourite number is "+favourite_numbers['islom'].title()+'.')
print("Lochin's favourite number is "+favourite_numbers['lochin'].title()+'.')
print("Ulug'bek's favourite number is "+favourite_numbers["ulug'bek"].title()+'.')
print("Abdurasul's favourite number is "+favourite_numbers['abdurasul'].title()+'.')

# 6-3. Glossary:
glossary={
    'print':'It is used to display data',
    'list':'It allows you to store sets of information in one place ',
    'tuple':'It lools like the list,but it is safer and faster',
    'dictionary':'It allows you to connect piece of related information',
    'append':'It is used to add new items at the end of lists'

}
print("Print:\n\t"+glossary['print'])
print("List:\n\t"+glossary['list'])
print("Tuple:\n\t"+glossary['tuple'])
print("Dictionary:\n\t"+glossary['dictionary'])
print("Append:\n\t"+glossary['append'])

# Author: Sherzod Oltinboyev:
# Date: 21.12.2020:
# Theme: 6-Dictionary:

# 6-4. Glossary 2:
glossary={
    'print':'It is used to display data',
    'list':'It allows you to store sets of information in one place ',
    'tuple':'It lools like the list,but it is safer and faster',
    'dictionary':'It allows you to connect piece of related information',
    'append':'It is used to add new items at the end of lists',
    "sort":"It is used to sort the piece of information according to alphabetical order",
    'keys':'It is used to get all keys from the dictionary',
    'value':'It is used to choose all values from the dictionary',
    'set':'Al values in the output will be unique',
    'del':'It is used to delete items ',


}
for Key,Value in glossary.items():
    print("\nKey: "+Key)
    print("Value: "+Value)

# 6-5. Rivers:
rivers={
    'nile':'egypt',
    'amazonka':"america",
    'surxondaryo':'uzbekistan',
}
for river,country in rivers.items():
    print(river.title()+' is located in the '+country.title())
for river in rivers.keys():
    print(river.title())
for country in rivers.values():
    print(country.title())

# 6-6. Polling:
favourite_languages={
    'suxrob':'c',
    'xurshid':'python',
    'ixtiyor':'java',
    'sanjar':'php',
}
names=['sardor','akmal','xurshid','ixtiyor']
for name in favourite_languages.keys():
    print(name.title())
    if name in names:
        print("Hi "+name.title()+",please take our pol")

    if name not in names:
        print("Thank you for taking our pol")

# 6-7. People:
info1={
    'first_name': 'Anvar',
    'last_name': 'Xudoyberdiyev',
    'age': "18",
    'city': 'Djizakh',
}
info2={'first_name':'Lochin',
       'last_name':'Abdukarimov',
       'age':'18',
       'city':'Djizakh',
       }
info3={'first_name': 'Islom',
       'last_name': 'Xalilov',
       'age': "22",
       'city': 'Tashkent',
       }
people=[info1,info2,info3]
for person in people:
    print(person)

# Author: Sherzod Oltinboyev:
# Date: 21.12.2020:
# Theme: 6-Dictionary:

# 6-8. Pets:
cat={
    'type':'domestic',
    "owner's_name":'Bill',
}
dog={
    'type':'wild',
    "owner's_name":'John'
}
pets=[cat,dog]

for pet in pets:
    for key, value in pet.items():
        print("Key: "+key.title())
        print("Value: "+value.title())

# 6-9. Favourite Places:
favourite_places={
    'Anvar':'',
    'Lochin':'',
    'Ilhom':'',
}

# 6-10. Favourite Numbers:
favourite_numbers={
    'ilhom':[4,8,14],
    'islom':[7,17,3],
    'lochin':[6,10],
    "ulug'bek":[14,5],
    'abdurasul':[77,8,13],
}
for name,numbers in favourite_numbers.items():
    print("\n"+name.title()+"'s favourite numbers are:")
    for number in numbers:
        print("\t"+str(number))


# 6-11. Cities:
cities={
    'los angeles':{
        'country':'America',
        'population':'78 million',
        'fact':'It is the one of the beautiful place in the world ',
    },
        'istanbul':{
        'country':'Turkey',
        'population':'34 million',
        'fact':'It is the center of tourism.',
    },
    'toshkent':{
        'country':'Uzbekistan',
        'population':'4 million',
        'fact':'It is the historical city'
    },
}
for city,info in cities.items():
    print("\nCity: "+city.title())
    country='Country: '+info['country']
    population='Population:'+info['population']
    fact='Fact: '+info['fact']
    print("\t"+country)
    print("\t"+population)
    print("\t"+fact)


# Takrorlash:

aliens=[]
for alien_number in range(30):
    new_alien={'color':'green','points':5,"speed":'slow'}
    aliens.append(new_alien)

for alien in aliens[:7]:
    if alien['color']=='green':
        alien['color']='yellow'
        alien['points']=10
        alien['speed']='medium'
    if alien['color']=='yellow':
        alien['color']='red'
        alien['points']=15
        alien['speed']='fast'
for alien in aliens[:30]:
    print(alien)
print('FINISH')
print('Total number of aliens: '+str(len(aliens)))
