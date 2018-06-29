#test file
from sys import argv
script, filename = argv

print(f"we are going to erase {filename}.")
input("?")

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file. Goodbye!")

target.truncate()

print("writing files")


line1 = ('line1 testing')
line2 = ('line2 testing')
line3 = ('line3 testing')

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)

print("and finally close it")
target.close
