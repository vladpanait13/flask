# import qrcode

'''
def stars():
    for _ in range(5):
        print("*" * _)

stars()

####################

def qr():

    img = qrcode.make("https://youtu.be/-4FPIL6e4SQ")
    img.save("qr.png", "PNG")

qr()

'''
'''
####################
names = ["Petrila", "Sapunaru", "Boupendza"]

name = input("Ce jucator iti place?  ")

for n in names:
    if name == n:
        print("Found")
        break
else:
    print("Not found")


###############
persons = ["Papeau", "Albion", "Rrahmani"]

person = input("Type the name: ")

if person in persons:
    print("Found")
else:
    print("Not found")

'''

'''
###############
phonebook = [
    {"name": "Carter", "number": "0723-232-231"},
    {"name": "David", "number": "0745-539-000"},
    {"name": "John", "number": "0764-349-934"},
]

name = input("Pe cine cauti? ")

for person in phonebook:
    if person["name"] == name:
        number = person["number"]
        print(f"Found {number}")
        break
else: 
    print("Not found")

###########################################

x = int(input("X: "))
y = int(input("Y: "))

z = x + y
if x < y:
    print ("x is smaller than y")
elif x > y:
    print ("x is bigger than y")
else:
    print ("x is equal to y")
print(z)

##########
nume = input("What's your name? ").strip().title()

# Split user's name into first name and last name
first, last = nume.split(" ")

print(f"hello, {nume}")
print(f"hello, {first}")

'''
'''

input_string = "Good Morning"
reverse_string = input_string[::-1]
print(reverse_string)

###########################

string = input("What word do you want to reverse? ")
words = string.split() #Split the string into words
print(words)

#Reverse each word individually
reversed_words = [word[::-1] for word in words]
print(reversed_words)
# Join the reversed words back together with a space
result = " ".join(reversed_words)
print(result)


###################################################################

numbers = [12, 5, 13, 1, 50, 20, 100, 500]

# Check if 13 is in the array
if 13 in numbers:
    print("13 is in the array")
else:
    print("13 is not in the array")

# Cauta un numar de la tastatura
n = int(input("Ce numar cauti?"))

if n in numbers:
    print(f"{n} is in the array")
else:
    print(f"{n} is not in the array")

# Bubble sort algorithm
n = len(numbers)

for i in range(n):
    #Last i elements are already sorted
    for j in range(0, n-i-1):
        #Swap if the element found is greater than the next element
        if numbers[j] > numbers[j+1]:
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
print(numbers)

'''
'''

def newPassword(a, b):
    # Initialize an empty string result
    result = " "
    # Get the length of the shorter string
    min_length = min(len(a), len(b))

    for i in range (min_length):
        result += a[i] + b[i]
        
    if len(a) > len(b):
        result += a[min_length:]
        
    else:
        result += b[min_length:]
        
    return result

# Example usage
a = "hacker"
b = "mountain"
print (newPassword(a,b)) 


class VendingMachine:
    def __init__(self, num_items, item_price):
        self.num_items = num_items
        self.item_price = item_price
        
    def buy(self, req_items, money):
        if req_items > self.num_items:
            raise ValueError("Not enough items in the machine")
            
        total_cost = req_items * self.item_price
        if money < total_cost:
            raise ValueError("Not enough coins")
            
        self.num_items -= req_items
        return money - total_cost
        
        
if __name__ == '__main__':
    
    vm = VendingMachine(10,2) # how many items are in the vm and the price for each item (10,2)
    print(vm.buy(5,150)) # how many items we want to purchase and how much money we insert (5,150)


'''

'''

def calc():

    Number1 = eval(input("Number 1: "))
    Number2 = eval(input("Number 2: "))

    sum = Number1 + Number2
    sub = Number1 - Number2
    division = Number1 / Number2
    multi = Number1 * Number2
    power = Number1 ** Number2

    print(f"The sum of numbers is: {sum}")
    print(f"The substriction of numbers is: {sub}")
    print(f"The division of numbers is: {division}")
    print(f"The multiplication of numbers is: {multi}")
    print(f"The power of numbers is: {power}")

calc()

'''

def oddeven():

    x = int(input("Enter a number: "))

    if x % 2 == 0:
        print(f"{x} is an Even number")
    else:
        print(f"{x} is an Odd number")

oddeven()

def leapyear():

    year = int(input("Please provide a year: "))
    if (year % 4 == 0) or (year % 100 == 0) or (year % 400 == 0):
        print(f"{year} is a Leap Year")
    else:
        print(f"{year} is not a Leap Year")

leapyear()


###################################
string = "Good morning"
words = string.split()
reverse_string = [word[::-1] for word in words]
result = " ".join(reverse_string)
print(result)






