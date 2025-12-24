def fat(x):
    if x == 1:
        return x
        
    else:
        return x*fat(x-1)
   
             
number = int(input("What's the number do you want the fatorial? "))
print(fat(number))
        