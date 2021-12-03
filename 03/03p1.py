file = open("03.input\input.txt", "r")
data = file.readlines()


gamma_rate = list()
epsilon_rate = list()

for i in range(12):
    one = 0
    zero = 0
    for bit in data:
        if int(bit[i]) == 1:
            one += 1
        else:
            zero += 1
        
    if one > zero:
        gamma_rate.append("1")
        epsilon_rate.append("0")
    else:
        gamma_rate.append("0")
        epsilon_rate.append("1")
        
gamma_decimal = int("".join(gamma_rate), 2)
epsilon_decimal = int("".join(epsilon_rate), 2)

print(f"{gamma_decimal*epsilon_decimal}")
