fhr = open("data.txt", "r")
cur_pos = fhr.tell()
print(cur_pos)
data = fhr.readline()
print(data)


cur_pos = fhr.tell()
print(cur_pos)
data = fhr.readline()
print(data)
fhr.close()

