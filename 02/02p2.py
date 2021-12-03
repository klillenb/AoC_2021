file = open("02.input\input.txt", "r")

horizontal = 0
depth = 0
aim = 0

for line in file:
    
    if "forward" in line:
        n = int(line.strip("forward \n"))
        horizontal += n
        depth += aim*n
    
    if "up" in line:
        n = int(line.strip("up \n"))
        aim -= n
        
    if "down" in line:
        n = int(line.strip("down \n"))
        aim += n

print(f"{depth*horizontal}")