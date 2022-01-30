print('to convert from Celsius to Fahrenheit, press ctf')
print('to convert from Celsius to Kelvin, press ctk')
print('to convert from Fahrenheit to Celsius, press ftc')
print('to convert from Fahrenheit to Kelvin, press ftk')
print('to convert from Kelvin to Celsius, press ktc')
print('to convert from Kelvin to Fahrenheit, press ktf')

#CODE BEGINS Here FOR FTC

def fahTcel():
    rounds = list()
    print('THIS IS A PROGRAM THAT CONVERTS FAHRENHEIT TO CELSIUS, TYPE done WHEN THROUGH')
    while True:
        inp = input('Fahrenheit Number:')
        if inp == 'done': break
        celx = float(inp) - 32
        cel = celx / 1.8
        rounds.append(celx + 32)
        print(cel, 'In Celsius')
    print(max(rounds), 'Is the hottest temperature recorded today')
    print(min(rounds), 'Is the coolest recorded today')
    print(sum(rounds), 'Is the sum of all temperatures recorded today')
    print('Here are all the numbers you crunched today', rounds)

#CODE FOR FTK BEGINS Here

def fahTkel():
    rounds = list()
    print('THIS IS A PROGRAM THAT CONVERTS FAHRENHEIT TO KELVIN, TYPE done WHEN THROUGH')
    while True:
        inp = input('Fahrenheit number:')
        if inp == 'done': break
        kelxx = float(inp) - 32
        kelx = kelxx * 5
        kel = kelx / 9
        Kelvin = kel + 273.15
        rounds.append(kelxx + 32)
        print(Kelvin, 'is the temperature in Kelvin')
    print(rounds)

#CODE FOR CTF BEGINS HERE

def celTfah():
    rounds = list()
    print('THIS IS A PROGRAM THAT CONVERTS CELSIUS TO FAHRENHEIT, TYPE done WHEN THROUGH')
    while True:
        inp = input('Celsius number:')
        if inp == 'done': break
        fahx = float(inp) * 1.8
        rounds.append(fahx / 1.8)
        fah = fahx + 32
        print(fah, 'is the temperature in Fahrenheit')
    print(rounds)

#CODE FOR CTK BEGINS HERE

def celTkel():
    rounds = list()
    print('THIS IS A PROGRAM THAT CONVERTS CELSIUS TO KELVIN, PRESS done WHEN THROUGH')
    while True:
        inp = input('Celsius number:')
        if inp == 'done': break
        kel = float(inp) + 273.15
        rounds.append(kel - 273.15)
        print (kel, 'is the temperature in Kelvin')
    print(rounds)

#CODE FOR KTF BEGINS HERE

def kelTfah():
    rounds = list()
    print('THIS IS A PROGRAM THAT CONVERTS KELVIN TO FAHRENHEIT, PRESS done WHEN THROUGH')
    while True:
        inp = input('temperature in Kelvin:')
        if inp == 'done': break
        fahxx = float(inp) - 273.15
        rounds.append(fahxx + 273.15)
        fahx = fahxx * 1.8
        fah = fahx + 32
        print(fah, 'degree Fahrenheit')
    print(rounds)

#CODE FOR KTC BEGINS HERE

def kelTcel():
    rounds = list()
    print('THIS IS A PROGRAM THAT CONVERTS KELVIN TO CELSIUS, PRESS done WHEN THROUGH')
    while True:
        inp = input('temperature in Kelvin:')
        if inp == 'done': break
        celx = float(inp) - 273.15
        rounds.append(celx + 273.15)
        print(celx, 'degree Celsius')
    print(rounds)


choice = input('what do you want to convert:')
if choice == 'ftc': fahTcel()
elif choice == 'ftk': fahTkel()
elif choice == 'ctf': celTfah()
elif choice == 'ctk': celTkel()
elif choice == 'ktf': kelTfah()
elif choice == 'ktc': kelTcel()
