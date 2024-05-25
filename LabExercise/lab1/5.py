#WAP that reads a multi-sentence string from user. Separate each sentence in the string and display each sentence. Again separate each word in the string and display then. Comma should not be included in the words.

str=[]
print("Enter the multiline string, if you want to stop writing enter \"00\": ")
while(str!="00"):
    user_input= input()
    if user_input == "00":
        break
    str.append(user_input)
print(str)
    
for line in str:
    print(line)
print("\n\n")
for line in str:
    for word in line:
        print(word)
