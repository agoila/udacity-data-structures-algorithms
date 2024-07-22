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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
callers = set()
call_receivers = set()
text_numbers = set()

for record in texts:
    text_numbers.add(record[0])
    text_numbers.add(record[1])

for record in calls:
    callers.add(record[0])
    call_receivers.add(record[1])

for number in list(callers):
    if number in list(call_receivers) and number in list(text_numbers):
        callers.remove(number)

print("These numbers could be telemarketers: ", '\n')
print('\n'.join(sorted(callers)))

