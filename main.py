11 = [23, 87, 98, 34, 67, 89, 12, 8, 45, 78, 23, 56, 23]

sum = 0

for c in 11: 
    sum = sum + c

print('The sum of elements of list:', sum) 
avg = sum / len(11)

print('The average of elements of list:', avg)

print('Maximum element is:', max(11))

print('Minimum element is:', min(11))

print('Count of 23 is:', 11.count(23))

11.append(77)

print('Updated list:', 11)

11.insert(3, 66)

print('Updated list:', 11)

11.remove(34)

print('Updated list:', 11)
