import random
letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers=["1","2","3","4","5","6","7","8","9"]
symbols=["!","@","#","$","%","^","&","*","(","_","-","+","="]

random.shuffle(letters)
#makeitastring = ''.join(map(str, letters))

random.shuffle(numbers)
#strn= ''.join(map(str,numbers))

random.shuffle(symbols)
#sym_s=''.join(map(str,symbols))

print("Welcome to my password generator")
charc=int(input("Enter the number of characters you want in your password "))

num=int(input("How many numbers would you like ? "))
let=int(input("How many letters would you like ? "))
sym=int(input("How many symbols would you like ? "))

check_len=num+let+sym

if check_len <= charc:
    password=letters[0:let] + numbers[0:num] + symbols[0:sym]
    random.shuffle(password)
    string_pass= ''.join(map(str,password))
    print("\nThe generated password is :\n" +string_pass)  
else:
    print("\nInvalid attempt")