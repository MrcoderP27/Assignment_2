number = int(input("Enter a number: "))

if number%2 == 0 :
    print(f"{number} is a even number.")
elif number%2 != 0 :
    print(f"{number} is a odd number.")
else :
    print("There must be an error")