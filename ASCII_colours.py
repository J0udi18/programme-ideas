print('/x1b[6;30;42m' + 'done it!!'+ '/x1b[0m')

x = 0
for row in range (24):
    colours: ""
    for columns in range (5):
        code = str(x+columns)
        colours = colours + "m//33[" + code + "m/033[0m "
    print(colours)
        x += 5
