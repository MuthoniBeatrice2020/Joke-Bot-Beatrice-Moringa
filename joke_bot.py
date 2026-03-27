import random  # built-in Python module - no install needed


# -------------------------------------------------------
# DATA: A list of joke dictionaries (setup + punchline)
# -------------------------------------------------------
JOKES = [
    {
        "setup": "Is Coffee for one still called Kahawa? ☕",
        "punchline": "Ama ni Ka-huyu 😏 "
    },
    {
        "setup": "Nimeget job kama motivational speaker",
        "punchline": "Bei yake ni ya kuongea..lol"
    },
    {
        "setup": "Hard work never killed anybody ",
        "punchline": "but why take a chance? 😎"
    },
    {
        "setup": "I never knew what happiness was until I got married",
        "punchline": "And then it was too late"
    },
    {
        "setup": "What do you call a bear with no teeth?",
        "punchline": "A gummy bear! 🐻"
    },
    {
        "setup": "Why do ducks have feathers? ",
        "punchline": "To cover their butt quacks!....😆"
    },
    {
        "setup": "What do you call fake spaghetti?",
        "punchline": "An impasta!"
    },
    {
        "setup": "Why don't skeletons fight each other",
        "punchline": "They don't have the guts"
    },
    {
        "setup": "Muthoni is writing a book about glue but guess what?",
        "punchline": "She's stuck on the 1st page!"
    },
    {
        "setup": "How does a computer get drunk?",
        "punchline": "It takes screenshots"
    },
    {
        "setup": "My doctor told me I'm going deaf",
        "punchline": "The news was hard to hear"
    },
    {
        "setup": "What do you call a man without a body or a nose",
        "punchline": "Nobody nose!"
    },
    {
        "setup": "Why is 69 afraid of 70",
        "punchline": "because they got in a fight and 71"
    },
    {
        "setup": "Katoto kaluhya kalipewa ugali...Kakafanya nini?",
        "punchline": "Ka-kamega"
    },
    {
        "setup": "Where do you go if you are driving and bees enter your car?",
        "punchline": "It doesn't matter cause unaenda Nanyuki!!...this is my favourite one!! lol..😅"
    },
]


# -------------------------------------------------------
# JOKE QUEUE: Manages the no-repeat shuffle system
# -------------------------------------------------------
joke_queue = []  # starts empty - refill_queue() fills it before the bot launches


def refill_queue():
    """
    Copies all jokes into the queue and shuffles them.
    Runs at startup and every time all jokes finish.
    """
    global joke_queue
    joke_queue = JOKES.copy()   # copy() prevents modifying the original list
    random.shuffle(joke_queue)  # shuffle() randomises the order in place


def get_next_joke():
    """
    Pops the next joke off the queue.
    Refills and reshuffles automatically when the queue runs out.
    """
    global joke_queue

    if len(joke_queue) == 0:
        refill_queue()
        print("\nJokeBot: I ran through all my jokes! Reshuffling for a fresh round...\n")

    return joke_queue.pop()  # .pop() removes and returns the last item


# -------------------------------------------------------
# FUNCTION: Print a welcome banner
# -------------------------------------------------------
def show_welcome():
    """Prints the welcome message when the bot starts."""
    print("=" * 55)
    print("   Welcome to JokeBot - Muthoni hopes this gives")
    print("   you a smile to brighten up your day!!!")
    print("=" * 55)
    print("\nHello! I am JokeBot. Here is what I can do:\n")
    print("  [1] Tell me a joke")
    print("  [2] Tell me another joke")
    print("  [3] How many jokes do you know?")
    print("  [4] Exit")
    print()


# -------------------------------------------------------
# FUNCTION: Pick and display the next joke (no repeats)
# -------------------------------------------------------
def tell_joke():
    """Gets the next joke from the queue and prints it."""
    joke = get_next_joke()
    print(f"\nJokeBot: {joke['setup']}")
    input("(Press Enter for the punchline...)")
    print(f"JokeBot: {joke['punchline']}\n")


# -------------------------------------------------------
# FUNCTION: Show joke count
# -------------------------------------------------------
def joke_count():
    """Tells the user how many jokes are stored and how many remain."""
    total = len(JOKES)
    remaining = len(joke_queue)
    print(f"\nJokeBot: I know {total} jokes total and {remaining} remain before I loop around!\n")


# -------------------------------------------------------
# FUNCTION: Handle unknown input
# -------------------------------------------------------
def unknown_input(user_input):
    """Responds when the user types something unexpected."""
    print(f"\nJokeBot: Hmm, I didn't understand '{user_input}'. Try typing 1, 2, 3 or 4.\n")


# -------------------------------------------------------
# MAIN FUNCTION: The app loop
# -------------------------------------------------------
def main():
    """The main loop that keeps the chatbot running until the user exits."""
    refill_queue()  # shuffle the full list once before the bot starts
    show_welcome()

    while True:
        user_input = input("You: ").strip()

        if user_input == "1" or user_input == "2":
            tell_joke()

        elif user_input == "3":
            joke_count()

        elif user_input == "4":
            print("\nJokeBot: Goodbye! Remember: laughter is the best debugging tool. Bye!\n")
            break

        else:
            unknown_input(user_input)


# -------------------------------------------------------
# Entry point - only runs when executed directly
# -------------------------------------------------------
if __name__ == "__main__":
    main()
