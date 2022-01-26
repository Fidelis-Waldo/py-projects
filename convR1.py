rounds = list()
print('THIS IS A PROGRAM THAT CONVERTS FAHRENHEIT SCALE TO CELSIUS, TYPE done WHEN THROUGH')
while True:
    inp = input('Fahrenheit Number:')
    if inp == 'done': break
    celx = float(inp) - 32
    cel = celx / 1.8
    rounds.append(celx + 32)
    if cel >= 100 :
        print('Too hot')
    elif cel <= 0 :
        print('Ice cold')
    else :
        print('Chill')
    print(cel, 'In Celsius')
print(max(rounds), 'Is the hottest temperature recorded today')
print(min(rounds), 'Is the coolest recorded today')
print(sum(rounds), 'Is the sum of all temperatures recorded today')
print('Here are all the numbers you crunched today', rounds)
