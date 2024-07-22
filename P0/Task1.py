"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
unique_nums = []
counter = 0

for record1 in texts:
    for number1 in record1[0:2]:
        if number1 not in unique_nums:
            counter += 1
            unique_nums.append(number1)

for record2 in calls:
    for number2 in record2[0:2]:
        if number2 not in unique_nums:
            counter += 1
            unique_nums.append(number2)

print("There are {} different telephone numbers in the records.".format(counter))