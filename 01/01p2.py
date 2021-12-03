file = open("01.input\input.txt", "r")
data = [int(i) for i in file.readlines()]

count_increase = 0
prev_sum = sum(data[:3])

for discard, add in zip(data, data[3:]):
    new_sum = prev_sum - discard + add
    count_increase += new_sum > prev_sum
    prev_sum = new_sum
            
print(count_increase)