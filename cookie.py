class jar: 
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.cookies = list() 


    def __str__(self): 
        output = ""
        for cookie in self.cookies:  
            output += "🍪"
        return output   


    def deposit(self, n): 
        if n > self.capacity:
            print("You are out of capacity!") 
            return 0
        for i in range(n): 
            self.cookies.append("🍪") 


    def withdraw(self, n): 
        if n > self.capacity:
            print("You are out of capacity!") 
            return 0
        for i in range(n): 
            self.cookies.pop()  


    def volume(self): 
        return f"The cookie jar’s capacity: {self.capacity}" 


    def size(self):
        count = 0
        for cookie in self.cookies: 
            count += 1 
        return f"The number of cookies in the cookie jar: {count}"  



hamza = jar() 

hamza.deposit(12)
hamza.withdraw(6)

print(hamza)
print(hamza.volume()) 
print(hamza.size())