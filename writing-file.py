fhr = open("data.txt", "r")
data = fhr.read()
print("Before writing:")
print(data)
fhr.close()

fhw = open("data.txt", "w")
num = fhw.write("this new first line written\n")
num1 = fhw.write("this new second line written\n")
print("num:", num)
print("num1:", num1)
fhw.close()

fhr = open("data.txt", "r")
data = fhr.read()
print("After Writing: ")
print(data)
fhr.close()

