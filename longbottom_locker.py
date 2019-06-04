import pickle

# Setup variables
filename = "donotshare"
result = ""

# Parse file
for line in pickle.load(open(filename)):
   for char, n in line:
      result += char*n
   result += "\n"

# Printing result
print result

