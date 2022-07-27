
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


# reading the whole document but using the read method
fhr = open("data.txt", "r")
data = fhr.read()
print(data)
fhr.close()
# so much easier

# you can limit the size of it, read only the first 10 characters
fhr = open("data.txt", "r")
data = fhr.read(10)
print(data)
fhr.close()

