number = int(input())
tries = 0
guess = int(input())
while guess != number:
    if guess < number:
        print("c'est plus")
        tries += 1
    elif guess > number:
        print("c'est moins")
        tries += 1
    guess = int(input())
    print("Nombre d'essais nécessaires :")
    print(tries + 1)

    
    

