word = input("Enter a word")

result = ''
for i in word:
    if i not in result:
       result = result + i
print(result)
