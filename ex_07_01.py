# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname, 'r')

for line in fh:
    line = line.strip()
    print(line.upper())


fh.close()
