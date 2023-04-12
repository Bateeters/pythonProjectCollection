from tkinter import *
from tkinter import messagebox
import random

user_score = 0
ai_score = 0

root = Tk()
root.title("Rock, Paper, Scissors")

label = Label(
    root, text="Rock, Paper, Scissors", font=('Arial', 18))
label.pack(padx=20, pady=20)

# label2 = Label(root, text="Score - You: " +
#              str(user_score)+"  Computer: "+str(ai_score), font=('Arial', 14))
#label2.pack(pady=(0, 10))

MODES = [
    # text    Mode
    ("Rock", "Rock"),
    ("Paper", "Paper"),
    ("Scissors", "Scissors")
]

choice = StringVar()
choice.set("Rock")

for text, mode in MODES:
    Radiobutton(root, text=text, variable=choice,
                value=mode).pack(padx=90, anchor=W)


def show_message():
    result = Tk()
    result.title("Results")
    global ai_score
    global user_score

    ai_choice = random.randint(0, 2)

    if choice.get() == "Rock" and ai_choice == 0:

        label = Label(result, text="I picked Rock too, looks like we tied.")
        label.pack(padx=20, pady=10)

        score = Label(result, text="Score - You: " +
                      str(user_score)+"  Computer: "+str(ai_score), font=('Arial', 14))
        score.pack()

        okBtn = Button(result, text="Again", command=lambda: result.destroy())
        okBtn.pack(pady=(10, 20))

    elif choice.get() == "Paper" and ai_choice == 0:

        label = Label(result, text="I picked Rock, looks like you won.")
        label.pack(padx=20, pady=10)

        user_score += 1

        score = Label(result, text="Score - You: " +
                      str(user_score)+"  Computer: "+str(ai_score), font=('Arial', 14))
        score.pack()

        okBtn = Button(result, text="Again", command=lambda: result.destroy())
        okBtn.pack(pady=(10, 20))

    elif choice.get() == "Scissors" and ai_choice == 0:

        label = Label(result, text="I picked Rock, looks like I won.")
        label.pack(padx=20, pady=10)

        ai_score += 1

        score = Label(result, text="Score - You: " +
                      str(user_score)+"  Computer: "+str(ai_score), font=('Arial', 14))
        score.pack()

        okBtn = Button(result, text="Again", command=lambda: result.destroy())
        okBtn.pack(pady=(10, 20))

    elif choice.get() == "Rock" and ai_choice == 1:

        label = Label(result, text="I picked Paper, looks like I won.")
        label.pack(padx=20, pady=10)

        ai_score += 1

        score = Label(result, text="Score - You: " +
                      str(user_score)+"  Computer: "+str(ai_score), font=('Arial', 14))
        score.pack()

        okBtn = Button(result, text="Again", command=lambda: result.destroy())
        okBtn.pack(pady=(10, 20))

    elif choice.get() == "Paper" and ai_choice == 1:

        label = Label(result, text="I picked Paper too, looks like we tied.")
        label.pack(padx=20, pady=10)

        score = Label(result, text="Score - You: " +
                      str(user_score)+"  Computer: "+str(ai_score), font=('Arial', 14))
        score.pack()

        okBtn = Button(result, text="Again", command=lambda: result.destroy())
        okBtn.pack(pady=(10, 20))

    elif choice.get() == "Scissors" and ai_choice == 1:

        label = Label(result, text="I picked Paper, looks like you won.")
        label.pack(padx=20, pady=10)

        score = Label(result, text="Score - You: " +
                      str(user_score)+"  Computer: "+str(ai_score), font=('Arial', 14))
        score.pack()

        okBtn = Button(result, text="Again", command=lambda: result.destroy())
        okBtn.pack(pady=(10, 20))

    elif choice.get() == "Rock" and ai_choice == 2:

        label = Label(result, text="I picked Scissors, looks like you won.")
        label.pack(padx=20, pady=10)

        user_score += 1

        score = Label(result, text="Score - You: " +
                      str(user_score)+"  Computer: "+str(ai_score), font=('Arial', 14))
        score.pack()

        okBtn = Button(result, text="Again", command=lambda: result.destroy())
        okBtn.pack(pady=(10, 20))

    elif choice.get() == "Paper" and ai_choice == 2:

        label = Label(result, text="I picked Scissors, looks like I won.")
        label.pack(padx=20, pady=10)

        ai_score += 1

        score = Label(result, text="Score - You: " +
                      str(user_score)+"  Computer: "+str(ai_score), font=('Arial', 14))
        score.pack()

        okBtn = Button(result, text="Again", command=lambda: result.destroy())
        okBtn.pack(pady=(10, 20))

    else:

        label = Label(
            result, text="I picked Scissors too, looks like we tied.")
        label.pack(padx=20, pady=10)

        score = Label(result, text="Score - You: " +
                      str(user_score)+"  Computer: "+str(ai_score), font=('Arial', 14))
        score.pack()

        okBtn = Button(result, text="Again", command=lambda: result.destroy())
        okBtn.pack(pady=(0, 10))


goBtn = Button(root, text="Shoot!",
               command=show_message)
goBtn.pack(pady=20)

root.mainloop()
