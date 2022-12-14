<font size = 3> AiCore Project </font><br> 
<font size = 2> Python coding project by: [Joshua Payne](https://github.com/Josh-BI-UK) </font>

# Hangman Game Documentation


> My first pratical assignment as part of the AiCore Ai-engineering bootcamp was to build a simple Hangman game. This repo conatins:
> * a template python script (found in the [00_Template](/00_Template) folder), which can be used as souce of insperation or framework to support in developing your own hangman game.<br><br>
> * Various prototype notebooks and python scripts, which I used to develop my end game in stages <i>(found in the [01_Dev](/01_Dev) folder). </i><b>Note!! The files in this folder are raw and my not resemable the end result or the most beatufil code.</b><br><br>
> * [02_Test](/02_Test) folder has a test version vaildated by my course instructor.<br><br>
> * My end game <i>(found in the [02_Solution](/03_Solution) folder).</i><br><br>
> ### **Technology\framework used:**<br>
> This project is a simple Python project that's suitable for intermediate level Python programmers. There is no official framework used, however, I have attempted to implement object-oriented programming (OOP)[^1] and "“Don’t Repeat Yourself" (i.e., DRY)[^2] methodologies where I could.
>
> The game itself was written using `VS Code`, `Python version 3.9` using `jupyter notebooks` during the development stage, with the final game exported to python script format (*.ipy) with magic cells (`# %%`) to enable a user to step through code blocks if needed.
>
> [^1]: Tutorial on Python OOP - by realpython.com (https://realpython.com/python3-object-oriented-programming/) <br>
> [^2]: Blog on DRY methodology - by scientificallysound.org (https://scientificallysound.org/2018/07/19/python-functions/)<br>
<br>



---
The project deliverables have been broken up into units of work called "milestones", which in turn are divided into tasks as follows:<br>
<br>
<br>

## Milestone 1 - Set up the environment
The main objective of milestone 1 was to set-up our development enviroment.
<br>

### **Task 1:**  In this project, we'll use GitHub to track changes to our code and save them online in a GitHub repo.

Follow the instructions in the [Setup-guide.ipynb](/Setup-guide.ipynb) notebook found in the root directory.
<br>

---
<br>

## Milestone 2
During Milestone 2, we developed the components of the game that define the list of guessable words, a mechanism for picking a word at random from thw word list, and a method for asking the player to select a one charater guess letter.
<br>

### **Task 1:** Define list of possible words, Create a file named `milestone_2.py`. <br>
- **1.1** Create a list containing the names of your 5 favorite fruits. <br>
- **1.2** Assign this list to a variable called `word_list`. <br>
- **1.3** Print out the newly created list to the standard output (screen). <br>
<br>

### **Task 2:**  Choose a random word from list <br>
- **2.2** `import` python module called `random` at the very top of your script.<br>
- **2.3** Create the `random.choice` method and pass the `word_list` variable into the choice method. <br>
- **2.4** Assign the randomly generated word to a variable called `word`.<br>
- **2.5** Print out the varible `word`. Run your code several times and observe the words printed out after each run. 
    - <i><b>!!!Note: Random may sometimes choice the same word, every so often. Don't worry this is perfectly normal as the selection is random, however, no rule exist that random can't select the same string more than once.</b></i><br>

### **Task 3:**  Ask the user for input.<br>
- **3.1** Using the `input` function, ask the user to enter a single letter.<br>
- **3.2** Assign the input to a variable called `guess`.<br>
<br>

### **Task 4:**   Check that the input is a single character<br>
- **4.1** Create an `if` statement that checks if the length of the `input` is equal to 1, and the input is an alphabet.<br>
- **4.2** In the body of the `if` statement, print a message that says `"Good choice!"`.<br>
- **4.3** Create an else block that prints `"Oops! That is not a valid input."`, if the preceeding conditions are not met.<br><br>

### **Task 5:**   Start documenting your experience<br>
- **5.1** Create a README file for your project using a method of your choice. A simple way to create a "ReadMe" is by using the `echo` command from your command line\terminal, as follows:

    a. From the root directory for your project, launch terminal or navigate to the project root folder using `cd <YOUR-PROJECT-FILEPATH>`.<br>

    b. Then use the `echo` command to create your README

    ```console
    echo "# Project Hangman" > README.md
    ```
    <br>
    
    c. Check your README.md file has been created, by using command line\terminal command:

    ```console
    open README.md
    ```
     + Your ReadMe file should open in a new text editor window.<br><br>

- **5.2** Add documentation to your README file following this [Example Documentation](./00_Template/ExampleDocumentation.md) guide. Describe the code you wrote in this milestone.<br>

- **5.3** Upload your hangman files to your remote Git repository (e.g. GitHub), using the following commands:<br>

    a. From the root directory for your project, launch a terminal window or navigate to the project root folder using `cd <YOUR-PROJECT-FILEPATH>`.<br><br>

    b. Then use the `git add -all` and `git commit` commands to push your local changes to your remote  to repository.<br>

    ```console
    git init
    git status
    git add --all
    git commit -m "replace text with your commit notes/comments."
    ```

<br>

---
<br>

## Milestone 3
Milestone 3, The aim of this milestone was to code functionality that checks if the guessing letter is part of the randomly chosen word.
<br>

### **Task 1:** Iteratively check if the guessed letter is vaild guess
Write code that will continuously ask the user for a letter and validate it.

Create a new script called `milestone_3.py`, this file will contain the code for this milestone.<br>
- **1.1** Create a `while` loop and set the condition to `True`. Setting the condition to True ensures that the code run continuously. In the body of the loop, write the code required for the following tasks 3, 4 & 5. <br>
- **1.2** A Ask the user to guess a letter and assign this to a variable called `guess`. <br>
- **1.3** Check that the `guess` is a single, alphabetical character.
- **1.4** If the `guess` passes the checks, break out of the loop.
- **1.5** If the `guess` does not pass the checks, then print a message saying "Invalid letter. Please, enter a single alphabetical character."<br>

### **Task 2:** Cheak whether the guess in the word<br>

Check whether the letter guessed by the user is in the secret word that was randomly chosen by the computer. For example, if the user guesses the letter "a" and the secret word is "apple", then your code should check if "a" is in "apple".

- **2.1** Create an `if` statement that checks if the guess is in the word.
- **2.2** In the body of the `if` statement, print a message saying `"Good guess! {guess} is in the word."`. Obviously, format the string to show the actual guess instead of {guess}.

- **2.3** Create an `else` block that prints a message saying `"Sorry, {guess} is not in the word. Try again."`. This block of code will run if the guess is not in the word.
  <br>

### **Task 3:** Cheak whether the guess in the word<br>

Good job so far! But your code probably doesn't look great. It's hard to tell which lines do what.

Create 2 functions, `check_guess` and `ask_for_input` functions which contain the code for those two things.

#### **The check_guess function:**
The `check_guess` function will take the guessed letter as an argument and check if the letter is in the word.

- **3.1** Define a function called `check_guess`. pass in the `guess` as a parameter for the function. Write the code for the following steps in the body of this function.<br>
- **3.2** Convert the `guess` into lower case.<br>
- **3.3** Move the code that you wrote to check if the guess is in the word into this function block.<br>

#### **The ask_for_input:**

- **3.4** Define a function called `ask_for_input`.<br>

- **3.5** Move the code that you wrote in the `Iteratively check if the input is a valid guess` task into this function block.<br>

- **3.6** Outside the while loop, but within this function, call the `check_guess` function to check if the guess is in the word. Don't forget to pass in the guess as an argument to the method.<br>

- **3.7** Outside the function, call the `ask_for_input` function to test your code.<br>

---
<br>

## Milestone 4

Milestone 3, The aim of this milestone was to code functionality that checks if the guessing letter is part of the randomly chosen word.
<br>

### **Task 1:** Iteratively check if the guessed letter is vaild guess
Write code that will continuously ask the user for a letter and validate it.

Create a new script called `milestone_3.py`, this file will contain the code for this milestone.<br>
- **3.1** Create a `while` loop and set the condition to `True`. Setting the condition to True ensures that the code run continuously. In the body of the loop, write the code required for the following tasks 3, 4 & 5. <br>
- **3.2** A Ask the user to guess a letter and assign this to a variable called `guess`. <br>

---
## Conclusions

- Maybe write a conclusion to the project, what you understood about it and also how you would improve it or take it further.

- Read through your documentation, do you understand everything you've written? Is everything clear and cohesive?
