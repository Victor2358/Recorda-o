class car:
    type = "volvo"
    def __init__ (self, color, miles):
        self.color = color
        self.miles = miles
        
    def describe(self, type, color, miles):
        return f"the {type} color is {color} and it drived {miles} miles"     

    def noise(self, sound):
        return f"the car sound is: {sound}. Now, the magic car will devour you"
        
        
mozila = car("red", 600) # When you pass the parameters, will need at firsty insert all the parameters
print(mozila.describe(mozila.type, mozila.color, mozila.miles)) # Say the parameters

mozila.type = "ford" # Change data for especifically mozila type
mozila.color = "blue"
mozila.miles = 1000
print(mozila.describe(mozila.type, mozila.color, mozila.miles)) # Say the parameters for other datas

mozila = car("yellow", 1500) #change everyone again and "volvo" gonna back
print(mozila.describe(mozila.type, mozila.color, mozila.miles)) 

print(mozila.noise("I'm a car and I can to speak"))


                       
                        
     