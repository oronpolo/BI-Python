#Print characters present at an even index number

def main():
    str = "PYnative"
    print(len(str))

    for i in range(0,len(str)):
        if i % 2 == 0:
            print(str[i])
       
        
main()


"""
# accept input string from a user
word = input('Enter word ')
print("Original String:", word)

# get the length of a string
size = len(word)

# iterate a each character of a string
# start: 0 to start with first character
# stop: size-1 because index starts with 0
# step: 2 to get the characters present at even index like 0, 2, 4
print("Printing only even index chars")
for i in range(0, size - 1, 2):
    print("index[", i, "]", word[i])


"""