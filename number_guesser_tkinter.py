from tkinter import *
from tkinter import messagebox
import random

# Setting global count tracker
guessCount = 0

# Main Home Window
root = Tk()
root.title("Number Game")

lbl = Label(root, text="Welcome to this Number Game!", font=('arial', 18))
lbl.pack(padx=20, pady=10)

lbl2 = Label(root, text="How It Works:", font=('arial', 16))
lbl2.pack()

lbl3 = Label(root, text="You will give me a number.\nI will then pick a number between 0 and the number you gave me\n(including both 0 and the given number).\nYou will then try to guess the number I picked.\nI will give you feedback if it's higher or lower than your guess.\nI will also keep track of how many guesses you used.", font=('arial', 12))
lbl3.pack(padx=20)

lbl4 = Label(root, text="Please Enter A Number:", font=('arial', 16))
lbl4.pack(pady=(10, 0))

# top of range entry box
topNum = Entry(root, width=20, font=('arial', 12))
topNum.pack(pady=10)


def textGuess():  # if letters are entered or if guess field left blank
    textGuess = Tk()
    textGuess.title("Text Input Error")
    lbl = Label(
        textGuess, text="Please make sure your guess is only a number.")
    lbl.pack(padx=20, pady=20)

    # button back to guessing window
    back = Button(textGuess, text="Back", font=('arial', 14),
                  command=lambda: textGuess.destroy())
    back.pack(pady=(0, 20))


def negativeGuess():  # if negative number is entered in guess field
    negativeGuess = Tk()
    negativeGuess.title("Negative Number Input Error")

    lbl = Label(negativeGuess, text="Please enter a number higher than 0.")
    lbl.pack(padx=20, pady=20)

    # button back to guessing window
    back = Button(negativeGuess, text="Back", font=('arial', 14),
                  command=lambda: negativeGuess.destroy())
    back.pack(pady=(0, 20))


def guess_check():  # checking user guess
    global guessCount  # pulling global guessCount variable to update

    try:  # making sure guess is int
        int(uGuess.get())
    except ValueError:  # if not, push back text error window
        textGuess()
    else:  # checking if int is negative
        if int(uGuess.get()) < 0:  # if it is, push back negative error window
            negativeGuess()
        elif int(uGuess.get()) == r:  # checking if guess is correct
            guessCount += 1
            winScreen()
        elif int(uGuess.get()) < r:  # checking if guess is lower
            guessCount += 1
            higherScreen()
        else:  # guess is higher
            guessCount += 1
            lowerScreen()


def winScreen():  # window on correct guess

    # closing guessing window
    game.destroy()

    # creating win window
    win = Tk()
    win.title("You Win!")

    # displaying what the correct number was
    lbl = Label(win, text="Correct! The number was " +
                str(r)+". You win!", font=('arial', 16))
    lbl.pack(pady=20)

    # changing color of label to green with white text
    lbl['background'] = 'green'
    lbl.config(foreground="white")

    # displaying how many guesses user used
    lbl2 = Label(win, text="You guessed "+str(guessCount)+" time(s).")
    lbl2.pack()

    # button back to main (root) window
    back = Button(win, text="Play Again", font=(
        'arial', 14), command=lambda: win.destroy())
    back.pack(pady=20)


def higherScreen():  # window on guess when it's too low

    # creating higher window
    higher = Tk()
    higher.title("Number Game")

    lbl = Label(higher, text="Guess is too low, try again", font=('arial', 16))
    lbl.pack(pady=(20, 0), padx=10)

    # button back to guessing window
    back = Button(higher, text="Guess Again", font=(
        'arial', 14), command=lambda: higher.destroy())
    back.pack(pady=20)


def lowerScreen():  # window on guess when it's too high

    # creating lower window
    lower = Tk()
    lower.title("Number Game")

    lbl = Label(lower, text="Guess is too high, try again.",
                font=('arial', 16))
    lbl.pack(pady=(20, 0), padx=10)

    # button back to guessing window
    back = Button(lower, text="Guess Again", font=(
        'arial', 14), command=lambda: lower.destroy())
    back.pack(pady=20)


def text():  # window when text is entered for initial range field or if left blank

    # creating window
    text = Tk()
    text.title("Text Input Error")

    lbl = Label(
        text, text="Please make sure your input is only a number.")
    lbl.pack(padx=20, pady=20)

    # button back to main (root) window
    back = Button(text, text="Back", font=('arial', 14),
                  command=lambda: text.destroy())
    back.pack(pady=(0, 20))


def negative():  # window when a negative number is entered for initial range field

    # creating window
    negative = Tk()
    negative.title("Negative Number Input Error")

    lbl = Label(negative, text="Please enter a number higher than 0.")
    lbl.pack(padx=20, pady=20)

    # button back to main (root) window
    back = Button(negative, text="Back", font=('arial', 14),
                  command=lambda: negative.destroy())
    back.pack(pady=(0, 20))


def gameWindow():  # window when guessing

    # making "game" global
    global game

    # pulling in "guessCount" to reset on new game
    global guessCount
    guessCount = 0

    # creating game window
    game = Tk()
    game.title("Guessing Game")

    # getting random number between 0 and user input, making it global
    global r
    r = random.randint(0, int(topNum.get()))

    lbl = Label(game, text="Enter your guess:", font=('arial', 16))
    lbl.pack(padx=20, pady=(20, 0))

    # getting user guess and making it global
    global uGuess
    uGuess = Entry(game, width=20, font=('arial', 12))
    uGuess.pack(pady=10)

    # button to check user guess
    submit = Button(game, text="Guess", font=('arial', 14),
                    command=guess_check)
    submit.pack(pady=(0, 20))


def input_check():  # Checking user initial input
    try:  # checking to make sure initial input is an int
        int(topNum.get())
    except ValueError:  # if not push back text entry error
        text()
    else:  # Checking to make sure initial input is not negative
        if int(topNum.get()) <= 0:  # push back negative number entry error if it is
            negative()

        else:  # if positive, move on to guessing random number
            gameWindow()


# button to check initial user input
start = Button(root, text="Start", font=('arial', 14), command=input_check)
start.pack(pady=(0, 20))

# pop up asking user if they want to quit when main window is closed with the corner "x"


def on_closing():
    if messagebox.askyesno(title="Quit?", message="Do you really want to quit?"):
        root.destroy()


root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
