# Author: Sherzod Oltinboyev:
# Date: 17.12.2020 11:00
# Theme: 4-Working With Lists:

# 4-1. Pizzas:
pizzas=['burger','lavash','hamburger','donar']
for pizza in pizzas:
    print('I like '+pizza.title()+' fast-food')
print('I really love fast-foods!')

# 4-2. Animals:
animals=['lion','tiger','wolf']
for animal in animals:
    print(animal.title()+", Wild world animal")
    print(animal.title()+", is dangerous animal in the forest \n")
print("Any of these animals make people afraid")

# 4-3. Counting to twenty:
for value in range(1,21):
    print(value)

# 4-4. One Million:

#for numbers in range(1,1000001):
 #   print(numbers)

# 4-5.Summing a Million:






# 4-6.Odd Numbers:
for odd_numbers in list(range(1,21,2)):
    print(odd_numbers)

# 4-7.Threes:
for threes in list(range(3,10,3)):
    print(threes)

# 4-8. Cubes:
cubes=[]
for value in list(range(1,11)):
    cubes.append(value**3)
print(cubes)

# 4-9. Cube Comprehension:
cubes=[value**3 for value in range(1,11)]
print(cubes)

# 4-10. Slices.
pizzas=['burger','lavash','hamburger','donar','pizza','chips','hotdog']
print("The first three item in the list are:")
for pizza in pizzas[:3]:
    print(pizza.title())

print("Three items from the middle of the list are:")
for pizza in pizzas[1:4]:
    print(pizza.title())

print("The last three itmes in the list are:")
for pizza in pizzas[-3:]:
    print(pizza.title())

# 4-11: My Pizzas,Your Pizzas:
pizzas=['burger','lavash','hamburger','donar']
friend_pizzas=pizzas[:]
pizzas.append('gamburger')
friend_pizzas.append('chips')
print("My favourite pizzas are:")
for pizza in pizzas:
    print(pizza.title())

print("My friend's favourite pizzas are:")
for pizza1 in friend_pizzas:
    print(pizza1.title())

# 4-12. More Loops:
pizzas=['burger','lavash','hamburger','donar']
for pizza in pizzas:
    print(pizza.title())
    for food in pizza:
        print(food.title())

# 4-13.Buffet:
foods=('Somsa','Shashlik','Osh','Shorva','Norin')
print("List of foods in the restaurant:")
for food in foods:
    print(food)
foods=('Somsa','Shashlik','Osh','Shorva','Norin',"Jiz",'Kabob')
print("\nChanged list of foods:")
for food in foods:
    print(food)
