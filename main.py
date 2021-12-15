#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P


# Eazy level

random_letter = random.sample(letters, nr_letters)
random_numbers = random.sample(numbers, nr_numbers)
random_symbols = random.sample(symbols, nr_symbols)
password_generator = random_letter + random_numbers + random_symbols


password_string_eazy_level = "".join(password_generator) #- преобразование списка в строку
print(f"Here is your (eazy#1) password: {password_string_eazy_level}")

password1 = ""

for letter in range(1, nr_letters + 1):
  password1 += random.choice(letters)

for number in range(1, nr_numbers +1):
  password1 += random.choice(numbers)

for symbol in range(1, nr_symbols +1):
  password1 += random.choice(symbols)

print(f"Here is your (eazy#2) password: {password1}")

# Hard level

password_length = nr_letters + nr_symbols + nr_numbers
full_list = letters + numbers + symbols
password_hard = random.sample(full_list, password_length)
password_string_hard_level = "".join(password_hard)
print(f"Here is your (hard#1) password: {password_string_hard_level}")

password = ""

for char in range(1, password_length + 1):
  password += random.choice(full_list)
print(f"Here is your (hard#2) password: {password}")


password_list = []

for char in range(1, nr_letters + 1):
  password_list.append(random.choice(letters))

for char in range(1, nr_symbols + 1):
  password_list += random.choice(symbols)

for char in range(1, nr_numbers + 1):
  password_list += random.choice(numbers)

random.shuffle(password_list)

password1= ""
for char in password_list:
  password1 += char

print(f"Here is your (hard#3) password: {password1}")
