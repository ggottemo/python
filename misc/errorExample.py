#errorExample.py - An example demonstrating getting Tracebacks as a string 
#From Automate the Boring Stuff
def spam():
    bacon()
    
    
def bacon():
    raise Exception('This is the error message.')
    
    
    
    
spam()


#Example using traceback to gracefully handle error, writing to file as a string
import traceback
try:
    raise Exception('This is an error message')
except:
    errorFile = open('errorInfo.txt','w')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('The traceback info was written to errorInfo.txt')
    
#Example using assert statements to check that code is working properly,
#If not, immediately stop the program
ages = [26, 57, 92, 54, 22, 15, 17, 80, 47, 73]
ages.sort()
ages
assert ages [0] <= ages[-1] # Will stop if sort fails to order properly


    