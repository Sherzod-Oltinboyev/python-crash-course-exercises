# Author: Sherzod Oltinboyev:
# Date: 27.12.2020:
# Theme: 8 Functions:

# 8-1. Message:
def display_message():
    print("What you are learning in this chapter?")


display_message()

# 8-2. Favourite Book:
def favourite_book(book):
    print("One of my favourite books is "+book.title()+".")


favourite_book ("python crash course")

# 8-3. T-Shirt:
# Positional Arguments
def make_shirt(size,text):
    '''Displaying information about a shirt'''
    print("\nThe size of shirt is "+size+".")
    print("The brand of the shirt is a "+text+".")


make_shirt('40','Guchchi')

# Keyword Arguments
def make_shirt(size,text):
    '''Displaying information about a shirt'''
    print("\nThe size of shirt is "+size+".")
    print("The brand of the shirt is a "+text+".")


make_shirt(size='40',text='Guchchi')

# 8-5. Cities:
def describe_city(name,country='America'):
    print("\n"+name.title()+" is located in the "+country.title()+".")


describe_city(name="washington")
describe_city(name='paris',country='france')
describe_city(name='istanbul',country='turkey')

# 8-6.City Names:
def city_country(name,country):
    info='\n"'+name.title()+","+country.title()+'"'
    return info


formatted=city_country('Dubai','BAA')
formatted1=city_country('Tashkent','uzbekistan')
formatted2=city_country('Chikago','america')
print(formatted)
print(formatted1)
print(formatted2)

# 8-7.Album:
def make_album(artist_name,album_title,track_number=""):
    album={"name":artist_name,'title':album_title}
    if track_number:
        album["track number"]=track_number
    return album

ready=make_album('Imron','yomon qiz',track_number=str(88))
ready1=make_album('Ummon','sensiz')
ready2=make_album('sardor raximxon','ona',str(34))

print(ready)
print(ready1)
print(ready2)

 # Author: Sherzod Oltinboyev:
 # Date: 29.12.2020:
 # Theme: 8 Functions:

 # 8-8. User Albums:

def make_album(artist_name,album_title,trace_number):
    album={"name":artist_name,'title':album_title,'album number':trace_number}


    return album


while True:
    print("\nPlease tell me about your favourite artist")
    print("enter 'q' at any time to quit")
    artist=input("Artist name: ")
    if artist=="q":
        break

    title=input("Album title: ")
    if title=="q":
        break

    number=input("Album number: ")
    if number=="q":
        break

    ready=make_album(artist,title,number)
    print(ready)

 # Author: Sherzod Oltinboyev:
 # Date: 30.12.2020:
 # Theme: 8 Functions:

 # 8-9.Magicians:


             
