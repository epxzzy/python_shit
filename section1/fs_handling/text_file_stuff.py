# open file handle
file = open('gobblegobble.txt', 'r+')

# writing shit
file.write("ello biatch")
file.writelines( ["\n", "\n", "many lines later"])

# reading shit
AllFileContent = file.read()
FileFirstLine = file.readline()
FileLinesAsList = file.readlines()

# close file handle
file.close()