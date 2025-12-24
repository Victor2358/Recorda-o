def f(x):
    x = 2*x
    return x;
    
while True:
    try:      
        m = int(input("What number do you want? "))
        print(f"The double of {m} is equal {f(m)}")
    
    except: #if you insert s letter instead a number
            print("Ocurred an error. Try again.")

# Will result in error if you insert a letter