** Course name: Artifical Intelligence Part Time 09
** Student name: Beatrice Muthoni Macharia

------

A BEGINNER'S GUIDE TO PYTHON 3.14.3: HOW TO BUILD A CLI CHATBOT FROM SCRATCH

**Technology Chosen:** PYTHON

**Why I chose it**
 As a beginner in coding, I felt that this language would be a good starting point into my tech journey. It uses a simple readable syntax that closely mirrors plain English and therefore easier to learn. It is also versatile and the skills I learn from this are transfareable and can be used in web development, data science and Artifical Intelligence.

**End goal**
To buid a simple interactive chatbot that runs in the terminal, responds to user input and tells jokes. It focuses on key concepts e.g variables lists, functions, loops etc..

------

SUMMARY OF THE TECH

**What is Python? & Where it is used**
In simple terms, it is a highlevel programming language used in web applications, software development, data science and machine learning. It was created by Guido van Rossum in 1991.
he wanted to create a language that was efficient, easy to read, learn and understand.

**A real life example**
Instagram's backend runs on Django which is a Python web framework. Netflix also uses Python for its data pipeline and recommendation algorithms.

------

SYSTEM REQUIREMENTS

**OS System**  Windows 10/11 (What I used), macOS12
**Python version** 3.14.3 (latest version) can run on older versions but not older than 3.8
**Code Editor** VS Code
**Terminal** VS Code Terminal (Used this), Powershell
**Package Manager** pip

Does not need external packages. will only use in built python modules

------

INSTALLATION & SET UP INSTRUCTIONS

## Check if python is already installed
1. open your terminal of choice
2. run command
    python --version

## If not installed
1. Visit official python website https://www.python.org/downloads/
2. Download python install manager
3. run .exe file for Windows. excute prompts, ensure to accept the **Add Python to Path** option
4. For macOS: Use the `.pkg` installer from the website or run:
    brew install python3
5. For Linux (Ubuntu/Debian) rub    
    sudo apt update
    sudo apt install python3
6. Check if python is installed correctly
    python3 --version
    # Expected output: Python 3.x.x
7. Install Python extension for Visual Studio https://marketplace.visualstudio.com/items?itemName=ms-python.python

## Download Project File from my github
*Clone this repo:*

   ```bash
    git clone https://github.com/MuthoniBeatrice2020/joke-bot-beatrice-moringa.git
    cd joke-bot-beatrice-moringa
```
------

HOW TO RUN THE PROJECT

```bash
# 1. Navigate into the project folder
cd joke-bot-beatrice-moringa

# 2. Run the script in VSCode terminal or powershell(make sure your path is the same as the file location)
python joke_bot.py

or py joke_bot.py

#if successful you will see the welcome screen appear immediately.

# 3. Follow the on-screen menu

```

------

MINIMUM WORKING EXAMPLE

**What it does**
The Joke bot will launch a simple command line menu. User can pick a number from the list and hit enter. Bot will excute and close cleanly.

**My Code Overview**
==START OF CODE==

```python
import random  # Built-in module, no install needed

JOKES = [
    {"setup": "Why do programmers prefer dark mode?", "punchline": "Because light attracts bugs!"},
]

def tell_joke():
    joke = random.choice(JOKES)
    print(f"JokeBot: {joke['setup']}")
    input("Press Enter for the punchline...")
    print(f"JokeBot: {joke['punchline']}")

def main():
    while True:
        user_input = input("You: ").strip()
        if user_input == "1":
            tell_joke()
        elif user_input == "4":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
```
==END OF CODE==

**Expected Outcome**
-------------------------------------------------------
------------------------------------------------------
   Welcome to JokeBot - Muthoni hopes this gives you a smile to brighten up your day!!!
-------------------------------------------------------------
---------------------------------------------------------------

Hello! I am JokeBot. Here is what I can do:

  [1] Tell me a joke
  [2] Tell me another joke
  [3] How many jokes do you know?
  [4] Exit

You: 1

JokeBot: Why do programmers prefer dark mode?
(Press Enter for the punchline...)
JokeBot: Because light attracts bugs!

You: 3

JokeBot: I know 15 jokes! And I am always ready to tell them.

You: 4

JokeBot: Goodbye! Remember: laughter is the best debugging tool. Bye!
```
```

------

AI PROMPT JOURNAL

**Prompt one**

   *I am a complete beginner in Python. Give me a step by step guide to install Python 3 on Windows and run my first script.*
 
   ## AI Response summary
   1st the AI walked me through the steps to install python and confirm that the process was successful. It then walked me through how to install the "hello world" python script and then it gave me slightly more complex script to run and finally it explained common beginner mistakes eg 
        1. saving the file as hello.py.txt instead of hello.py
        2. typing the wrong folder in Command Prompt
        3. forgetting to reopen Command Prompt after install

   ## Evaluation
    It was very helpful, it did not assume that I had any prior knowledge and walked me through each step. I drew alot of inspiration for this project from the Learning a New Programming Language with AI section of the course

**Prompt two**

   *Explain Python functions to a complete beginner. Show a simple example and explain each line.*

   ## AI Response summary
   The AI explained that a function groups reusable code under a name. It showed `def`, parameters and the `return` keyword with a simple add function example and line by line comments.

   ## Evaluation:
   it was helpful in helping me understand the fundamental without difficult technical jargon. The line comments made understanding each part much faster than reading a textbook.

**Prompt three**
   After learning the fundamentals I felt comfortable enough to start on the project. I remembered how our lec emphasized on the use of AI as a helping guide instead of using it to write the code entirely last week. So I tried to execute code based on what I had learned and asked for help in areas I got stuck on.
 
   *How do I use a while loop with user input in Python to keep a program running until the user types exit?*

   ## AI Response summary
   The AI showed me how to excute a `while True` loop with an `if` check for a break condition, plus `.strip().lower()` how to handle sloppy user input. It gave a simple example with an explanation, showed me how the flow works and gave me an alternative example plus common mistakes eg.
    1. Forgetting break in an infinite loop
    2. Using = instead of ==
    3. Not handling uppercase input
    4. Expecting input() to return numbers automatically
   It also gave me a quick summary
    1. Quick summary
    2. Use while True for continuous execution
    3. Use input() to get user data
    4. Use if to check for "exit"
    5. Use break to stop the loop

   ## Evaluation
   It helped me create the menu for my bot. It helped me solve the core loop problem for the chatbot. The `.strip()` tip was a bonus insight that improved the bot's reliability.

**Prompt four**
   
   *Show me how to store jokes as a list of dictionaries in Python and pick one randomly.*

   ## AI Response summary
   AI gave me a simple working example with an explanation, it gave me how to store each dictionary eg. A dictionary stores data as key value pairs **"setup"** → question, **"punchline"** → answer. Then how to set up **random.choice(jokes)** how to access values and expected output. It summarized the key concepts for me:
   1. Key concepts you just used
   2. list → stores many items
   3. dictionary → stores structured data
   4. random.choice() → selects randomly
   5. key access → gets specific values

   ## Evaluation
   This prompt directly produced the data structure the whole project uses. It also introduced the `random` module which required no installation.

**Prompt five**

   *What does if __name__ == '__main__': mean in Python and why should a beginner use it?*

   ## AI Response summary
   The AI explained that this line stops the `main()` function from running when another file imports the script. It described it as a best practice even for small scripts.

   ## Evaluation
   This cleared up confusion around a line that appears in nearly every Python tutorial but rarely gets explained clearly.

------

COMMON ISSUE AND FIXES
   
   For the most part the entire process was fairly smooth. But the few issues that I did encounter included

## Issue 1: `SyntaxError: invalid syntax` near f-string
   **Error:**
    SyntaxError: invalid syntax
  **Cause:**  
    f-strings only work on Python 3.6 and above.
   **Fix:**  
    Check your Python version with `python3 --version`. Upgrade to 3.8 or higher from python.org.

## Issue 2: Script would run and exit immediately
   **Cause:**  
    Double-clicking the `.py` file opens and closes the terminal window before you can read output.
   **Fix:**  
    Always run scripts from the terminal with `python3 joke_bot.py`.

## Issue 3: IndentationError
   **Error:**
    IndentationError: expected an indented block
   **Fix:**  
    Python enforces indentation as part of its syntax. Use 4 spaces (not tabs) consistently. VS Code handles this automatically if you set your editor to "spaces: 4".

## Issue 5: `KeyError` when accessing dictionary
   **Error:**
    KeyError: 'Setup'
   **Cause:**  
    Dictionary keys are case-sensitive. `'Setup'` and `'setup'` are different keys.
   **Fix:**  
    Check the exact key name in your dictionary definition and match it exactly everywhere you use it.

## Issue 6: Some jokes kept repeating multiple times before the full joke rotation was done
    **Fix**
    I added refill_queue() to take all 15 jokes, make a copy of the list and shuffle it randomly. It now runs once at startup and again automatically whenever the queue empty
    Also adjusted get_next_joke() calls .pop() which removes and returns the last joke from the shuffled list each time. Once the list hits zero items it triggers refill_queue() and prints a message telling the user a fresh round started.





REFERENCES
 1. Download python link:https://www.python.org/downloads/
 2. W3Schools Python Tutorial: https://www.w3schools.com/python/
 3. Python Extension for VS Code: https://marketplace.visualstudio.com/items?itemName=ms-python.python
 4. StackOverflow: https://stackoverflow.com/questions/tagged/python





