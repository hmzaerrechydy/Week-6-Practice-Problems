greeting = input("Greeting: ").split()

if greeting[0].lower() == "hello": 
    print("$0")
elif greeting[0][0] == "h": 
    print("$20")
else : 
    print("$100")