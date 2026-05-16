word = 'Sssss'
length = len(word)-1
rev = ''

while length >=0:
    # print(word[length].upper(), end="")
    rev += word[length].upper() #concatination is important
    length -= 1 #to stop the loop

print(rev)
if word.upper() == rev.upper():
    print("pallendrome")
else:
    print("Bad luck")