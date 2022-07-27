
# for reading a file line by line, tedious process
fhr = open("data.txt", "r")
line1 = fhr.readline()
print(line1, end="")
line2 = fhr.readline()
print(line2, end="")
line3 = fhr.readline()
print(line3, end="")
fhr.close()

fhr = open("data.txt", "r")
# reading literally the whole thing
list_var = fhr.readlines()
for line in list_var:
    print(line, end="")
fhr.close()

