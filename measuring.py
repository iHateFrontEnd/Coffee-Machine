strong_light = -1

while strong_light < 0 or strong_light > 4:
    print('Type 1 for strong coffee, 2 for normal coffee, 3 for light coffee')

    strong_light = int(input('What type of coffee do you want: '))

#this is in grams 
weightOfCoffeeBean = 0.1325

#water to be poured per 5 grams of coffee
pour_water = 88.7206 

#define make strong coffee (line 75)
def make_strong_coffee():
    strong_coffee = int(input('How many beans did you put [STRONG COFFEE]: '))

    if strong_coffee <= 45:
        #strong coffee for one person 
        print('ML of water ', pour_water * weightOfCoffeeBean * strong_coffee, ' strong coffee for one person')
    elif strong_coffee <= 60:
        #strong coffee for two people 
        print('ML of water ', pour_water * weightOfCoffeeBean * strong_coffee, ' strong coffee for two people')
    elif strong_coffee <= 75:
        #strong coffee for three people 
        print('ML of water ', pour_water * weightOfCoffeeBean * strong_coffee, ' strong coffee for three people')
    elif strong_coffee <= 90:
        #strong coffee for four people 
        print('ML of water ', weightOfCoffeeBean * pour_water * strong_coffee, ' strong coffee for four people')
    else:
        print('Please restart the program')

#define normal coffee (line 78)
def make_normal_coffee():
    normal_coffee = int(input('How many beans did you put [NORMAL COFFEE]: '))

    if normal_coffee <= 30:
        #normal coffee for one person 
        print('ML of water ', pour_water *weightOfCoffeeBean * normal_coffee, ' normal coffee for one person')
    elif normal_coffee <= 40:
        #normal coffee for two people 
        print('ML of water ', pour_water * weightOfCoffeeBean * normal_coffee, 'normal coffee for two people')
    elif normal_coffee <= 50:
        #normal coffee for three people
        print('ML of water ', pour_water * weightOfCoffeeBean * normal_coffee, ' normal coffee for three people')
    elif normal_coffee <= 60:
        #normal coffee for four people 
        print('ML of water ', pour_water * weightOfCoffeeBean * normal_coffee, ' normal coffee for four people')
    else:
        print('Please restart the program')


#define make light coffee (line 81)
def make_light_coffee():
    light_coffee = int(input('How many beans did you put [LIGHT COFFEE]: '))

    if light_coffee <= 20:
        #light coffee for one person 
        print('ML of water ', pour_water * weightOfCoffeeBean * light_coffee, ' light coffee for one person only')
    elif light_coffee <= 25:
        #light coffee for two people 
        print('ML of water ', pour_water * weightOfCoffeeBean * light_coffee, ' light coffee for two people only')
    elif light_coffee <= 30:
        #light coffee for three people
        print('ML of water ', pour_water * weightOfCoffeeBean * light_coffee, ' light coffee for three people only')
    elif light_coffee <= 40:
        #light coffee for four people 
        print('ML of water ', pour_water * weightOfCoffeeBean * light_coffee, ' light coffee for four people only')

    else:
        print('Please restart the program')

if strong_light == 1: 
    #make strong coffee 
    make_strong_coffee()
elif strong_light == 2:
    #make normal coffee
    make_normal_coffee()
elif strong_light == 3:
    #make light coffee 
    make_light_coffee()
else:
    print('Please restart the program')
