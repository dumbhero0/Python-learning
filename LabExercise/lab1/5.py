#WAP that reads a multi-sentence string from user. Separate each sentence in the string and display each sentence. Again separate each word in the string and display then. Comma should not be included in the words.

# Initialize an empty list to hold the input strings
str_list = []
print('Enter the multi-line string. If you want to stop writing, enter "00": ')

# Read input from the user until "00" is entered
while True:
    user_input = input()
    if user_input == "00":
        break
    str_list.append(user_input)

# Display each sentence
print("\nSentences:")
for line in str_list:
    print(line)

print("\nWords:")
# Separate each word in the string and display them without commas
for line in str_list:
    # Split the line into words, removing commas
    words = line.replace(",", "").split()
    for word in words:
        print(word)
