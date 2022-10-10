numbers = [0, 0, 0, 0, 0]
sum = 0
for i in range(5):
    numbers[i] = (int(input("Enter your input")))
lowest = numbers[0]
highest = numbers[0]
for i in range(5):
    if lowest > numbers[i]:
        lowest = numbers[i]
    if highest < numbers[i]:
        highest = numbers[i]
numbers.remove(lowest)
numbers.remove(highest)
for i in range(len(numbers)):
    sum += numbers[i]
print(sum)