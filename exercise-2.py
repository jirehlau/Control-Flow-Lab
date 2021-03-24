# exercise-02 Length of Phrase

# Write the code that:
# 1. Prompts the user to enter a phrase:
#      Please enter a word or phrase: 
# 2. Print the following message:
#      - What you entered is xx characters long
# 3. Return to step 1, unless the word 'quit' was entered.

# word = input("Enter a word or a phrase")
# while word != "quit":
#     if word == ""
#         print(f"What you entered is {word} long")
#     else:

while(True):
    user_typed_in = input("Enter a word or a phrase")
    if user_typed_in == "":
        print(f"What you entered is {user_typed_in} long")
    else == "quit":
        break