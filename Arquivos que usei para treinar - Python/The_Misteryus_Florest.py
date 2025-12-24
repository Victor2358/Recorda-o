#In the florest

posição = 0

while True:
    print("You're in the florest")
    move = input("What will you do? Move to: ")
    if move == "r":
        posição = posição + 1
        print(f"Now you're at {posição}")
        print("")
    elif move == "l":
        posição = posição - 1
        print(f"Now you're at {posição}")
        print("")
    else:
        print("But you choose to do nothing")
        print(f"Now you're at {posição}")
        print("")
      
    if posição == 3 or posição == -3:
          break
#He never out of florest  
        
print("Great! You're out of florest") 