# Example Project Documentation Guideline

> Include here a brief description of the project, what technologies are used etc.
My first pratical assignment as part of the AiCore Ai-engineering bootcamp was to build a simple Hangman game. This repo conatins:
> * a template python script (found in the [00_Template](/00_Template) folder), which can be used as souce of insperation or framework to support in developing your own hangman game.<br><br>
> * Various prototype notebooks and python scripts, which I used to test & develop my end game in stages <i>(found in the [01_Dev](/01_Dev) folder). </i><b>Note!! The files in this folder are raw and my not resemable the end result or themost beatufil code.</b><br><br>
> * My end game <i>(found in the [02_Solution](/02_Solution) folder).</i><br><br>

<br>

The project deliverables have been broken up into units of work called "milestones", which in turn are divided into tasks as follows:<br>

---

## Milestone 1 - Set up the environment

### **Task 1:**  In this project, we'll use GitHub to track changes to our code and save them online in a GitHub repo.

Follow the instructions in the [Setup-guide.ipynb](/Setup-guide.ipynb) notebook found in the root directory.
<br>

---
<br>

## Milestone 2
<br>

### **Task 1:** Define list of possible words, Create a file named `milestone_2.py`. <br>
- 1.1. Create a list containing the names of your 5 favorite fruits. <br>
- 1.2. Assign this list to a variable called `word_list`. <br>
- 1.3. Print out the newly created list to the standard output (screen). <br>
<br>

### **Task 2:**  Choose a random word from list <br>
- 2.2. `import` python module called `random` at the very top of your script.<br>
- 2.3. Create the `random.choice` method and pass the `word_list` variable into the choice method. <br>
- 2.4. Assign the randomly generated word to a variable called `word`.<br>
- 2.5. Print out the varible `word`. Run your code several times and observe the words printed out after each run. 
    - <i><b>!!!Note: Random may sometimes choice the same word, every so often. Don't worry this is perfectly normal as the selection is random, however, no rule exist that random can't select the same string more than once.</b></i><br>

### **Task 3:**  Ask the user for input.<br>
- 3.1. Using the `input` function, ask the user to enter a single letter.<br>
- 3.2 Assign the input to a variable called `guess`.<br>
<br>

### **Task 4:**   Check that the input is a single character<br>
- 4.1. Create an `if` statement that checks if the length of the `input` is equal to 1, and the input is an alphabet.<br>
- 4.2 In the body of the `if` statement, print a message that says `"Good choice!"`.<br>
- 4.3 Create an else block that prints `"Oops! That is not a valid input."`, if the preceeding conditions are not met.<br>

### **Task 5:**   Start documenting your experience<br>
- 5.1 Create a README file for your project using a method of your choice. A simple way to create a "ReadMe" is by using the `echo` command from your command line\terminal, as follows:

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

- 5.2 Add documentation to your README file following this [Example Documentation](./00_Template/ExampleDocumentation.md) guide. Describe the code you wrote in this milestone.<br>

- 5.3 Upload your hangman files to your remote Git repository (e.g. GitHub), using the following commands:<br>

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
## Conclusions

- Maybe write a conclusion to the project, what you understood about it and also how you would improve it or take it further.

- Read through your documentation, do you understand everything you've written? Is everything clear and cohesive?
