# print("kannyiri")

fullname = "umar kannyiri"
age = 21
married = True
hobbies = ['football', 'gaming', 'travelling']
kids = {
    "paul": "male",
    "maurice": "male",
    "ama": "female"
}

# print(hobbies)

if(married == True):
    print("happy marriage")
else:
    print("save the date")

# function definition
def sayhello():
    print("Hello World")

def game_of_multiples():
    score = 0
    num = 3

    while(True):
        if(num % 3 == 0):
            response = input("please input a multiple")
            score = score + num
            num = int(response)
        else:
            print("game over,your score: " + str(score))
            break

def fullname(first, last):
    return first + " " + last

print(fullname("kannyiri","umar"))

arr = [100,15,45,90,"Gone", False]
print(arr[4])

fname = "umar kannyiri"


neg = -1
neg + -1
new_name = fname[neg]
print(new_name)

def reverser(data):
    rev = ""
    neg = -1
    while (len(rev) != len(data)):
        rev = rev + data[neg]
        neg = neg + -1

    return rev 
print(reverser("I am in Holland"))

def is_a_multiple(number, multiple):
    if (number % multiple == 0):
        return True
    else: 
        return False
print(is_a_multiple(72,5))