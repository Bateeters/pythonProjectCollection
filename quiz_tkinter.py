from tkinter import *
from tkinter import messagebox

# Set Riddle Answers
ans1 = "candle"
ans2 = "David"
ans3 = "envelope"
ans4 = "money"

# Create User Answers
name = ""
q1Ans = ""
q2Ans = ""
q3Ans = ""
q4Ans = ""
q5Ans = ""
q6Ans = ""


# Set user Score
score = 0

# Main Home Window
root = Tk()
root.title("Riddle Quiz")

lbl = Label(root, text="Welcome to the Riddle Quiz!", font=('avenir', 18))
lbl.pack(padx=20, pady=10)

lbl2 = Label(root, text="Are you ready to play?", font=('avenir', 14))
lbl2.pack()

# Player Name Entry Window


def player():

    # Creating player for future destroy function
    global player

    # creating name entry window
    player = Tk()
    player.title("Riddle Quiz")

    lbl = Label(player, text="First off, who is playing?", font=('avenir', 14))
    lbl.pack(padx=20, pady=20)

    global nameField
    nameField = Entry(player, width=40, font=('avenir'))
    nameField.pack(padx=20)

    next = Button(player, text="Next", font=('avenir', 12), command=q1)
    next.pack(pady=10)


# Question 1 Window


def q1():

    # Creating q1 for future destroy function
    global q1

    # Checking to make sure name is saved
    global name
    name = nameField.get().capitalize()

    # Closing Player Window
    player.destroy()

    # Opening Question 1 Window
    q1 = Tk()
    q1.title("Question 1")

    lbl = Label(q1, text="Question 1 of 6:", font=('avenir', 12))
    lbl.pack(pady=10)

    lbl2 = Label(
        q1, text="I'm tall when I'm young, and short when I'm old. I am a(n) ___.", font=('avenir', 14))
    lbl2.pack(padx=20)

    global q1Field
    q1Field = Entry(q1, width=40, font=('avenir'))
    q1Field.pack(padx=20, pady=10)

    next = Button(q1, text="Next", font=('avenir', 12), command=q2)
    next.pack(pady=(0, 10))

# Question 2 Window


def q2():
    global q2

    # Pulling in score to update
    global score

    # Checking to make sure q1 answer is saved
    global q1Ans
    q1Ans = q1Field.get().lower()

    # Checking q1 answer and adjusting score
    if q1Ans == ans1:
        score += 1

    # Checking to make sure score is updated and saved
    print(str(score))
    q1.destroy()

    # Creating Question 2 Window
    q2 = Tk()
    q2.title("Question 2")

    lbl = Label(q2, text="Question 2 of 6:", font=('avenir', 12))
    lbl.pack(pady=10)

    lbl2 = Label(
        q2, text="David's parents have three children: Snap, Crackle, and ___.", font=('avenir', 14))
    lbl2.pack(padx=20)

    global q2Field
    q2Field = Entry(q2, width=40, font=('avenir'))
    q2Field.pack(padx=20, pady=10)

    next = Button(q2, text="Next", font=('avenir', 12), command=q3)
    next.pack(pady=(0, 10))


def q3():
    global q3
    global score

    global q2Ans
    q2Ans = q2Field.get().capitalize()

    if q2Field.get().capitalize() == ans2:
        score += 1

    print(str(score))
    q2.destroy()

    q3 = Tk()
    q3.title("Question 3")

    lbl = Label(q3, text="Question 3 of 6:", font=('avenir', 12))
    lbl.pack(pady=10)

    lbl2 = Label(
        q3, text='What begins with an "e" and only contains one letter? A(n) ___.', font=('avenir', 14))
    lbl2.pack(padx=20)

    global q3Field
    q3Field = Entry(q3, width=40, font=('avenir'))
    q3Field.pack(padx=20, pady=10)

    next = Button(q3, text="Next", font=('avenir', 12), command=q4)
    next.pack(pady=(0, 10))


def q4():
    global q4
    global score

    global q3Ans
    q3Ans = q3Field.get().lower()

    if q3Ans == ans3:
        score += 1

    print(str(score))
    q3.destroy()

    q4 = Tk()
    q4.title("Question 4")

    lbl = Label(q4, text="Question 4 of 6:", font=('avenir', 12))
    lbl.pack(pady=10)

    lbl2 = Label(
        q4, text="People make me, save me, change me, raise me. What am I?", font=('avenir', 14))
    lbl2.pack(padx=20)

    global q4Field
    q4Field = Entry(q4, width=40, font=('avenir'))
    q4Field.pack(padx=20, pady=10)

    next = Button(q4, text="Next", font=('avenir', 12), command=q5)
    next.pack(pady=(0, 10))


def q5():
    global q5
    global score

    global q4Ans
    q4Ans = q4Field.get().lower()

    if q4Ans == ans4:
        score += 1

    print(str(score))
    q4.destroy()

    q5 = Tk()
    q5.title("Question 5")

    lbl = Label(q5, text="Question 5 of 6:", font=('avenir', 12))
    lbl.pack(pady=10)

    lbl2 = Label(
        q5, text="This one is worth two points. How do you think you are doing on this quiz so far?", font=('avenir', 14))
    lbl2.pack(padx=20)

    global q5Field
    q5Field = Entry(q5, width=40, font=('avenir'))
    q5Field.pack(padx=20, pady=10)

    next = Button(q5, text="Next", font=('avenir', 12), command=q6)
    next.pack(pady=(0, 10))


def q6():
    global q6
    global score

    global q5Ans
    q5Ans = q5Field.get().lower()

    score += 2

    print(str(score))
    q5.destroy()

    q6 = Tk()
    q6.title("Question 6")

    lbl = Label(q6, text="Question 6 of 6:", font=('avenir', 12))
    lbl.pack(pady=10)

    lbl2 = Label(
        q6, text="What is your name?", font=('avenir', 14))
    lbl2.pack(padx=20)

    global q6Field
    q6Field = Entry(q6, width=40, font=('avenir'))
    q6Field.pack(padx=20, pady=10)

    next = Button(q6, text="Next", font=('avenir', 12), command=result)
    next.pack(pady=(0, 10))


def result():
    global result
    global score

    global q5Ans
    q6Ans = q6Field.get().capitalize()

    if q6Ans == name:
        score += 1

    q6.destroy()

    result = Tk()
    result.title("Results")

    lbl = Label(result, text="Quiz Results:", font=('avenir', 12))
    lbl.pack(pady=10)

    lbl2 = Label(result, text="You Scored " +
                 str(score)+"/7", font=('avenir', 14))
    lbl2.pack(padx=20)

    q1result = Label(result, text="1. Your answer: "+q1Ans +
                     "  Correct Answer: "+ans1, font=('avenir', 12))
    q1result.pack(padx=20)

    q2result = Label(result, text="1. Your answer: "+q2Ans +
                     "  Correct Answer: "+ans2, font=('avenir', 12))
    q2result.pack(padx=20)

    q3result = Label(result, text="1. Your answer: "+q3Ans +
                     "  Correct Answer: "+ans3, font=('avenir', 12))
    q3result.pack(padx=20)

    q4result = Label(result, text="1. Your answer: "+q4Ans +
                     "  Correct Answer: "+ans4, font=('avenir', 12))
    q4result.pack(padx=20)

    q5result = Label(result, text="5. Your answer: "+q5Ans +
                     "  Correct Answer: Whatever you put!", font=('avenir', 12))
    q5result.pack(padx=20)

    q6result = Label(result, text="6. Your answer: "+q6Ans +
                     "  Correct Answer: "+name, font=('avenir', 12))
    q6result.pack(padx=20)

    replay = Button(result, text="Replay?", font=(
        'avenir', 12), command=lambda: result.destroy())
    replay.pack(pady=(0, 10))


def on_closing():
    if messagebox.askyesno(title="Quit?", message="Do you really want to quit?"):
        root.destroy()


startBtn = Button(root, text="Start", font=('avenir', 12), command=player)
startBtn.pack(pady=10)

root.protocol("WM_DELETE_WINDOW", on_closing)


root.mainloop()
