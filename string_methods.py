#formatting

var = str("hello world").capitalize()
#print(f"\"capitalize()\" converts first character to upper case: \"{var}\"")

var = str("HELLO WORLD").casefold()
#print(f"\"casefold()\" converts string into lower case : \"{var}\"")

var = str("Hello world").center(20) #add a position index
#print(f"\"center()\" returns a centered string : \"{var}\"")

var = str("HELLO WORLD").lower()
#print(f"\"lower()\" converts a string to lower case : \"{var}\"")

var = str("hello world").upper()
#print(f"\"upper()\" converts a string to upper case : \"{var}\"")
    
var = str("data science : python integration").title()
#print(f"\"title()\" converts first character of each word to upper case : \"{var}\"")

var = str("Apple").ljust(20) #add a spacing index
#print(f"\"ljust()\" Returns a left justified version of the string : \"{var + " is my favourite fruit."}\"")

var = str("Apple").rjust(20) #add a spacing index
# print(f"\"rjust()\" Returns a right justified version of the string : \"{var + " is not my favourite fruit."}\"")

var = str("     Python      ").strip()
#print(f"\"strip()\" Remove spaces at the beginning and at the end of the string : \"{"My favourite Programming language is "+var}\"")

var = str("HeLLo WoRlD").swapcase()
#print(f"\"swapcase()\" lowercase become uppercase then vice versa : \"{var}\"")

var = str("     Python      ").lstrip() #the left space is trimmed.
#print(f"\"lstrip()\" Returns a left trim version of the string: \"{"My favourite Programming language is "+var}\"")

var = str("     Python      ").rstrip() #removes the spacing in the end of a string
#print(f"\"rstrip()\" Returns a right trim version of the string: \"{"My favourite Programming language is "+var}\"")

var = str("50").zfill(10) #what is this for anyways
#print(f"\"{var}\"")

var = str("Hello World").split()
#print(f"\"split()\" splits string into a list where each word is a list item: \"{var} -> access index of list [0] = 'Hello' -> \"{var[0]}\" \"")

var = str("apple, banana, orange").rsplit(", ")
#print(f"\"rsplit()\" Splits a string into a list, using a comma, followed by a space as the operator: \"{var}\"")

var = str("Hello World").replace("World", "I love Python!!") #replace("original word", "word to replace")
#print(f"\"replace()\" Replaces a word in string: \"{var}\"")