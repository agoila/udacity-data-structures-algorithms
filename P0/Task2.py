"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
nums_and_timers = {}

for record in calls:
    for number in record[0:2]:
        if number not in nums_and_timers:
            nums_and_timers[number] = int(record[-1])
        else:
            nums_and_timers[number] += int(record[-1])

max_number = max(nums_and_timers, key=nums_and_timers.get)
max_seconds = nums_and_timers[max_number]
print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(max_number, max_seconds))

