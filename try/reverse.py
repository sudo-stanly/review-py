word = "Programming"
stored_chars = []


for char in word:
    stored_chars.append(char)
  
string_version = ''.join(stored_chars)  
print(string_version)

for char in word[::-1]:
    print(char, end='')
