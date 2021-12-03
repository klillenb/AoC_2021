file = open("01.input\input.txt", "r")
data = [int(i) for i in file.readlines()]
count_increase = 0

for n1, n2 in zip(data, data[1:]):
    if n1 < n2:
        count_increase += 1
            
print(count_increase)