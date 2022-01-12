inp = input('Fahrenheit Number?')
celx = float(inp) - 32
cel = celx / 1.8
if cel >= 100 :
    print('Too hot')
elif cel <= 0 :
    print('Ice cold')
else :
    print('Chill')
print(cel, 'In Celsius')
