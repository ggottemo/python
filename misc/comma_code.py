def comma(arg):
    finalString =''
    for x in range(len(arg)-1):
        finalString += str(x) + ', '
    finalString += "and " + arg[-1]
    return finalString


inset = ['one', 'two', 'three', 'four', 'five', 'six', 'seven']
print(comma(inset))
    
        
