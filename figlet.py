import pyfiglet 
import sys 

text = input("Input: ") 
arglen = len(sys.argv)
result = ""

if arglen < 2: 
    result = pyfiglet.figlet_format(text)
elif arglen == 2: 
    try: 
        result = pyfiglet.figlet_format(text, font = sys.argv[1]) 
    except: 
        print("Invalid font!")
        sys.exit() 
else: 
    print("Invalid usage!")

print(result)
