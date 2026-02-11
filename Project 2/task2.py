#Frequent word analyzer
import string
from collections import Counter
file = None
print('1. Use default file.\n2. Use your custom file.')
while True:
    try:
        ch = int(input("Enter your choice: "))
        if ch == 1 or ch == 2:
            break
        else:
            print('please enter a valid choice again!')
    except ValueError:
        print("Please enter 1 or 2 only")
if ch == 1:
    print('you chose default file!')
    file = 'task2.txt'

elif ch ==2:
    print('you chose your file!')
    file = input('Enter complete path of your file along with correct file name: ')

else:
    print('Wrong choice!')

try:
    with open(file, "r") as f:
        reading = f.read()
        print(reading)
except FileNotFoundError:
    print("File doesn't exist")
    exit()
except PermissionError:
    print("Permission denied")
    exit()
reading = reading.lower()
print(reading)

for punc in string.punctuation:
    reading = reading.replace(punc, "")
print(reading)

reading = reading.split()
print(reading)

frequency = Counter(reading)
print(frequency)

frequency = frequency.most_common(5)
print("most common words are: " , frequency)

final = list(filter(lambda x: x[0] in 'aeiou', reading))
print('List of words starting with vowel: ' , final)