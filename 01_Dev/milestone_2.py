# %% [markdown]
# TODO Task 1: Define list of possible words, Create a file named milestone_2.py. <br>
# [✔︎] 1.1. Create a list containing the names of your 5 favorite fruits. <br>
# [✔︎] 1.2. Assign this list to a variable called word_list. <br>
# [✔︎] 1.3. Print out the newly created list to the standard output (screen). <br>
# 

# %%
import random 
word_list = ['Apple','Orange','Plum','Breadfruit','Banana','Pineapples','Kiwis','Cherries']
print(word_list)

# %% [markdown]
# TODO Task 2: Choose a random word from list
# [✔︎] 2.2. Write import random on the first line. <br>
# [✔︎] 2.3. Create the random.choice method and pass the word_list variable into the choice method. <br>
# [✔︎] 2.4. Assign the randomly generated word to a variable called word.<br>
# [✔︎] 2.5. Print out word to the standard output. Run the code several times and observe the words printed out after each run. <br>

# %%
# Variable "word" defined using random method.
# Random method used to select one word from "word_list" randomly.
word = random.choice(word_list)
print(word)

# %% [markdown]
# TODO Task 3: Ask the user for input.<br>
# [✔︎] 3.1. Using the input function, ask the user to enter a single letter.<br>
# [✔︎] 3.2 Assign the input to a variable called guess.<br>
# 
# TODO Task 4: Check that the input is a single character<br>
# [✔︎] 4.1. Create an if statement that checks if the length of the input is equal to 1,
# and the input is an alphabet.<br>
# [✔︎] 4.2 In the body of the if statement, print a message that says "Good guess!".<br>
# [✔︎] 4.3 Create an else block that prints "Oops! That is not a valid input.",
# if the preceeding conditions are not met.<br>

# %%
#Invalid letter selection error messages:
err_msg_1 = "Oops! That is not a valid input,"
err_msg_2 = "please select only 1 [A-Z] letter"

# While loop used to ask for input and tests if input is a valid alphabet letter.
# Loop controlled by "valid_guess" variable, when it is "No", loop stays True and continues.
vaild_guess = "No"
while vaild_guess != "Yes":
    guess = input("Please select one letter or type 'quite' to end game:: ").strip()
    if guess.isnumeric() == True:
        print(err_msg_1)
        print(err_msg_1)
        vaild_guess = "No"
    elif guess == guess.lower() == "quite":
        print("Ok game will quite!")
        break
    elif guess.isalpha() == False:
        print(err_msg_1)
        print(err_msg_1)
        vaild_guess = "No"
    elif len(guess) > 1:
        print("Only one [A to Z] letter allowed")
        print(err_msg_1)
        print(err_msg_1)
    else:
        print("great choice")
        vaild_guess = "Yes"


