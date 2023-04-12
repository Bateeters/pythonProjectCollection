import tkinter as tk
from PIL import Image, ImageTk

"""
This program uses a dropdown menu to let the user select a Greek God/Goddess. 
Based on the selection it will open a page with a brief summary of them.
There is a button on each page to return to the selection list.
"""

# Gets selection for Search Button
def getSelection(dropdown):
    selection = dropdown.get(dropdown.curselection())

    # Aphrodite Page
    if selection == 'Aphrodite':
        aphrodite = tk.Toplevel(bg='lightpink')  # Sets new window and adds color
        aphrodite.geometry("500x600")  # Sets window size
        aphrodite.title("Aphrodite")  # Sets window title

        # Photo above text
        image1 = Image.open("GreekGodBanners/Aphrodite.png")  # Sets photo to be used
        resized_image = image1.resize((125, 175), Image.ANTIALIAS)  # Resizing photo
        test = ImageTk.PhotoImage(resized_image)  # Defines photo for use in label
        label1 = tk.Label(aphrodite, image=test, bg='lightpink')  # Label for photo
        label1.image = test  # Placing photo in label
        label1.place(relx=0.33, rely=0.05, relwidth=0.33, relheight=0.33)  # Label location placement

        # Frame for text and buttons
        lower_frame = tk.Frame(aphrodite, bg='mistyrose', bd=5)  # Frame for text and button
        lower_frame.place(relx=0.5, rely=0.40, relwidth=0.75, relheight=0.5, anchor='n')  # Frame location placement

        # Page text
        text = tk.Message(lower_frame,
                          text="Goddess of Love and Beauty\n\nCan change her appearance to become whatever "
                               "is thought to be most beautiful. She is responsible for starting the Trojan War.\n\n"
                               "Symbol: the Dove\n\nRoman name: Venus",
                          bg='mistyrose')  # Placing text in frame
        text.place(relx=0.05, rely=0.05, relwidth=.9, relheight=0.7)  # Formatting space for text placement

        # Previous button
        # previous = tk.Button(lower_frame, text="<", fg='black', font=40)  # Button for previous page
        # previous.place(relx=0, rely=0.8, relwidth=0.25, relheight=0.2)  # Previous button placement

        # Search Again button
        mainscreen = tk.Button(lower_frame, text="Search Another God/Goddess", fg='black', font=40,
                               command=lambda: aphrodite.destroy())  # Button for home page, closes current page
        mainscreen.place(relx=0.25, rely=0.8, relwidth=0.5, relheight=0.2)  # Home button placement

        # Next button
        # next = tk.Button(lower_frame, text=">", fg='black', font=40)  # Button for next page
        # next.place(relx=0.75, rely=0.8, relwidth=0.25, relheight=0.2)  # Next button placement

    # Apollo Page (code serves same purpose as previous pages)
    elif selection == 'Apollo':
        apollo = tk.Toplevel(bg='beige')
        apollo.geometry("500x600")
        apollo.title("Apollo")

        image1 = Image.open("GreekGodBanners/Apollo.png")
        resized_image = image1.resize((125, 175), Image.ANTIALIAS)
        test = ImageTk.PhotoImage(resized_image)
        label1 = tk.Label(apollo, image=test, bg='beige')
        label1.image = test
        label1.place(relx=0.33, rely=0.05, relwidth=0.33, relheight=0.33)

        lower_frame = tk.Frame(apollo, bg='white', bd=5)
        lower_frame.place(relx=0.5, rely=0.40, relwidth=0.75, relheight=0.5, anchor='n')

        text = tk.Message(lower_frame,
                          text="God of Poetry and Music\n\nOne of, if not the most, attractive male Olympians,"
                               " loves to be the center of attention. He gave king Midas donkey ears because the king"
                               " decided Pan played better music.\n\nSymbol: the Lyre\n\nRoman name: Apollo",
                          bg='white')
        text.place(relx=0.05, rely=0.05, relwidth=.9, relheight=0.7)

        # previous = tk.Button(lower_frame, text="<", fg='black', font=40)
        # previous.place(relx=0, rely=0.8, relwidth=0.25, relheight=0.2)

        mainscreen = tk.Button(lower_frame, text="Search Another God/Goddess", fg='black', font=40,
                               command=lambda: apollo.destroy())
        mainscreen.place(relx=0.25, rely=0.8, relwidth=0.5, relheight=0.2)

        # next = tk.Button(lower_frame, text=">", fg='black', font=40)
        # next.place(relx=0.75, rely=0.8, relwidth=0.25, relheight=0.2)

    # Ares Page (code serves same purpose as previous pages)
    elif selection == 'Ares':
        ares = tk.Toplevel(bg='darkred')
        ares.geometry("500x600")
        ares.title("Ares")

        image1 = Image.open("GreekGodBanners/Ares.png")
        resized_image = image1.resize((125, 175), Image.ANTIALIAS)
        test = ImageTk.PhotoImage(resized_image)
        label1 = tk.Label(ares, image=test, bg='darkred')
        label1.image = test
        label1.place(relx=0.33, rely=0.05, relwidth=0.33, relheight=0.33)

        lower_frame = tk.Frame(ares, bg='grey', bd=5)
        lower_frame.place(relx=0.5, rely=0.40, relwidth=0.75, relheight=0.5, anchor='n')

        text = tk.Message(lower_frame, text="God of War\n\nSon of Zeus and Hera, said to be involved in every argument"
                                            " from a small disagreement, to wars. Loves to fight. He fought on the side"
                                            " of the Trojans in the Trojan War.\n\nSymbols: A Spear and "
                                            "the Wild Boar\n\nRoman name: Mars",
                          bg='grey', fg='white')
        text.place(relx=0.05, rely=0.05, relwidth=.9, relheight=0.7)

        # previous = tk.Button(lower_frame, text="<", fg='black', font=40)
        # previous.place(relx=0, rely=0.8, relwidth=0.25, relheight=0.2)

        mainscreen = tk.Button(lower_frame, text="Search Another God/Goddess", fg='black', font=40,
                               command=lambda: ares.destroy())
        mainscreen.place(relx=0.25, rely=0.8, relwidth=0.5, relheight=0.2)

        # next = tk.Button(lower_frame, text=">", fg='black', font=40)
        # next.place(relx=0.75, rely=0.8, relwidth=0.25, relheight=0.2)

    # Artemis Page (code serves same purpose as previous pages)
    elif selection == 'Artemis':
        artemis = tk.Toplevel(bg='gainsboro')
        artemis.geometry("500x600")
        artemis.title("Artemis")

        image1 = Image.open("GreekGodBanners/Artemis.png")
        resized_image = image1.resize((125, 175), Image.ANTIALIAS)
        test = ImageTk.PhotoImage(resized_image)
        label1 = tk.Label(artemis, image=test, bg='gainsboro')
        label1.image = test
        label1.place(relx=0.33, rely=0.05, relwidth=0.33, relheight=0.33)

        lower_frame = tk.Frame(artemis, bg='azure', bd=5)
        lower_frame.place(relx=0.5, rely=0.40, relwidth=0.75, relheight=0.5, anchor='n')

        text = tk.Message(lower_frame,
                          text="Goddess of the Moon, Hunt, and Young Maidens\n\nShe is deadly with her bow."
                               " She does not entertain foolish individuals, especially males. She usually "
                               "appears as a young girl and dresses all in white and silver to match her "
                               "eyes and the moon.\n\n"
                               "Symbols: the Moon and the Deer\n\nRoman name: Diana",
                          bg='azure')
        text.place(relx=0.05, rely=0.05, relwidth=.9, relheight=0.7)

        # previous = tk.Button(lower_frame, text="<", fg='black', font=40)
        # previous.place(relx=0, rely=0.8, relwidth=0.25, relheight=0.2)

        mainscreen = tk.Button(lower_frame, text="Search Another God/Goddess", fg='black', font=40,
                               command=lambda: artemis.destroy())
        mainscreen.place(relx=0.25, rely=0.8, relwidth=0.5, relheight=0.2)

        # next = tk.Button(lower_frame, text=">", fg='black', font=40)
        # next.place(relx=0.75, rely=0.8, relwidth=0.25, relheight=0.2)

    # Athena Page (code serves same purpose as previous pages)
    elif selection == 'Athena':
        athena = tk.Toplevel(bg='slategrey')
        athena.geometry("500x600")
        athena.title("Athena")

        image1 = Image.open("GreekGodBanners/Athena.png")
        resized_image = image1.resize((125, 175), Image.ANTIALIAS)
        test = ImageTk.PhotoImage(resized_image)
        label1 = tk.Label(athena, image=test, bg='slategrey')
        label1.image = test
        label1.place(relx=0.33, rely=0.05, relwidth=0.33, relheight=0.33)

        lower_frame = tk.Frame(athena, bg='lightsteelblue', bd=5)
        lower_frame.place(relx=0.5, rely=0.40, relwidth=0.75, relheight=0.5, anchor='n')

        text = tk.Message(lower_frame,
                          text="Goddess of Wisdom\n\nDaughter of Zeus and Hera. She and Ares argue frequently and have "
                               "been known to start wars. She is the most active goddess in human affairs. She is very"
                               " prideful and has a temper to go with it. She sided with the Greeks in the Trojan War."
                               "\n\nSymbols: the Owl\n\nRoman name: Minerva",
                          bg='lightsteelblue')
        text.place(relx=0.05, rely=0.05, relwidth=.9, relheight=0.7)

        # previous = tk.Button(lower_frame, text="<", fg='black', font=40)
        # previous.place(relx=0, rely=0.8, relwidth=0.25, relheight=0.2)

        mainscreen = tk.Button(lower_frame, text="Search Another God/Goddess", fg='black', font=40,
                               command=lambda: athena.destroy())
        mainscreen.place(relx=0.25, rely=0.8, relwidth=0.5, relheight=0.2)

        # next = tk.Button(lower_frame, text=">", fg='black', font=40)
        # next.place(relx=0.75, rely=0.8, relwidth=0.25, relheight=0.2)

    # Demeter Page (code serves same purpose as previous pages)
    elif selection == 'Demeter':
        demeter = tk.Toplevel(bg='darkkhaki')
        demeter.geometry("500x600")
        demeter.title("Demeter")

        image1 = Image.open("GreekGodBanners/Demeter.png")
        resized_image = image1.resize((125, 175), Image.ANTIALIAS)
        test = ImageTk.PhotoImage(resized_image)
        label1 = tk.Label(demeter, image=test, bg='darkkhaki')
        label1.image = test
        label1.place(relx=0.33, rely=0.05, relwidth=0.33, relheight=0.33)

        lower_frame = tk.Frame(demeter, bg='darkgreen', bd=5)
        lower_frame.place(relx=0.5, rely=0.40, relwidth=0.75, relheight=0.5, anchor='n')

        text = tk.Message(lower_frame,
                          text="Goddess of Agriculture\n\nQuiet and simple goddess. If she was happy the crops would grow."
                               " Hades kidnapped her daughter, Persephone. Winter is said to be when she leaves to vist "
                               "her in the underworld.\n\nSymbols: Torch and the Corn Plant\n\nRoman name: Ceres",
                          bg='darkgreen', fg='white')
        text.place(relx=0.05, rely=0.05, relwidth=.9, relheight=0.7)

        # previous = tk.Button(lower_frame, text="<", fg='black', font=40)
        # previous.place(relx=0, rely=0.8, relwidth=0.25, relheight=0.2)

        mainscreen = tk.Button(lower_frame, text="Search Another God/Goddess", fg='black', font=40,
                               command=lambda: demeter.destroy())
        mainscreen.place(relx=0.25, rely=0.8, relwidth=0.5, relheight=0.2)

        # next = tk.Button(lower_frame, text=">", fg='black', font=40)
        # next.place(relx=0.75, rely=0.8, relwidth=0.25, relheight=0.2)

    # Dionysus Page (code serves same purpose as previous pages)
    elif selection == 'Dionysus':
        dionysus = tk.Toplevel(bg='maroon')
        dionysus.geometry("500x600")
        dionysus.title("Dionysus")

        image1 = Image.open("GreekGodBanners/Dionysus.png")
        resized_image = image1.resize((125, 175), Image.ANTIALIAS)
        test = ImageTk.PhotoImage(resized_image)
        label1 = tk.Label(dionysus, image=test, bg='maroon')
        label1.image = test
        label1.place(relx=0.33, rely=0.05, relwidth=0.33, relheight=0.33)

        lower_frame = tk.Frame(dionysus, bg='lemonchiffon', bd=5)
        lower_frame.place(relx=0.5, rely=0.40, relwidth=0.75, relheight=0.5, anchor='n')

        text = tk.Message(lower_frame,
                          text="God of Wine\n\nInvented wine which impressed Zeus, his father, and got him promoted "
                               "to a god. Loves to party and drink. Known to be both a fun and angry drunk.\n\n"
                               "Symbols: the Leopard, the Grape Vine\n\nRoman name: Bacchus",
                          bg='lemonchiffon')
        text.place(relx=0.05, rely=0.05, relwidth=.9, relheight=0.7)

        # previous = tk.Button(lower_frame, text="<", fg='black', font=40)
        # previous.place(relx=0, rely=0.8, relwidth=0.25, relheight=0.2)

        mainscreen = tk.Button(lower_frame, text="Search Another God/Goddess", fg='black', font=40,
                               command=lambda: dionysus.destroy())
        mainscreen.place(relx=0.25, rely=0.8, relwidth=0.5, relheight=0.2)

        # next = tk.Button(lower_frame, text=">", fg='black', font=40)
        # next.place(relx=0.75, rely=0.8, relwidth=0.25, relheight=0.2)

    # Hades Page (code serves same purpose as previous pages)
    elif selection == 'Hades':
        hades = tk.Toplevel(bg='indigo')
        hades.geometry("500x600")
        hades.title("Hades")

        image1 = Image.open("GreekGodBanners/Hades.png")
        resized_image = image1.resize((125, 175), Image.ANTIALIAS)
        test = ImageTk.PhotoImage(resized_image)
        label1 = tk.Label(hades, image=test, bg='indigo')
        label1.image = test
        label1.place(relx=0.33, rely=0.05, relwidth=0.33, relheight=0.33)

        lower_frame = tk.Frame(hades, bg='paleturquoise', bd=5)
        lower_frame.place(relx=0.5, rely=0.40, relwidth=0.75, relheight=0.5, anchor='n')

        text = tk.Message(lower_frame,
                          text="God of The Underworld\n\nHe was given the helm of darkenss which grants invisibility. "
                               "The eldest of the three brothers. He does not reside in Olympus but in his palace in the "
                               "underworld. Kidnapped his wife, Persephone (daughter of Demeter) and took her to the "
                               "underworld to marry.\n\n"
                               "Symbols: the Helm of Darkness, the Bident\n\nRoman name: Pluto",
                          bg='paleturquoise')
        text.place(relx=0.05, rely=0.05, relwidth=.9, relheight=0.7)

        # previous = tk.Button(lower_frame, text="<", fg='black', font=40)
        # previous.place(relx=0, rely=0.8, relwidth=0.25, relheight=0.2)

        mainscreen = tk.Button(lower_frame, text="Search Another God/Goddess", fg='black', font=40,
                               command=lambda: hades.destroy())
        mainscreen.place(relx=0.25, rely=0.8, relwidth=0.5, relheight=0.2)

        # next = tk.Button(lower_frame, text=">", fg='black', font=40)
        # next.place(relx=0.75, rely=0.8, relwidth=0.25, relheight=0.2)

    # Hephaestus Page (code serves same purpose as previous pages)
    elif selection == 'Hephaestus':
        hephaestus = tk.Toplevel(bg='dimgray')
        hephaestus.geometry("500x600")
        hephaestus.title("Hephaestus")

        image1 = Image.open("GreekGodBanners/Hephaestus.png")
        resized_image = image1.resize((125, 175), Image.ANTIALIAS)
        test = ImageTk.PhotoImage(resized_image)
        label1 = tk.Label(hephaestus, image=test, bg='dimgray')
        label1.image = test
        label1.place(relx=0.33, rely=0.05, relwidth=0.33, relheight=0.33)

        lower_frame = tk.Frame(hephaestus, bg='orangered', bd=5)
        lower_frame.place(relx=0.5, rely=0.40, relwidth=0.75, relheight=0.5, anchor='n')

        text = tk.Message(lower_frame,
                          text="God of The Forge\n\nAlways described to be ugly with a scraggly beard. He was thrown down"
                               " the side of Mount Olympus at birth making him a cripple. Extremely clever with his hands"
                               " and can make just about anything with his engineering, forging and mechanical skills.\n\n"
                               "Symbols: the Anvil and Hammer\n\nRoman name: Vulcan",
                          bg='orangered', fg='white')
        text.place(relx=0.05, rely=0.05, relwidth=.9, relheight=0.7)

        # previous = tk.Button(lower_frame, text="<", fg='black', font=40)
        # previous.place(relx=0, rely=0.8, relwidth=0.25, relheight=0.2)

        mainscreen = tk.Button(lower_frame, text="Search Another God/Goddess", fg='black', font=40,
                               command=lambda: hephaestus.destroy())
        mainscreen.place(relx=0.25, rely=0.8, relwidth=0.5, relheight=0.2)

        # next = tk.Button(lower_frame, text=">", fg='black', font=40)
        # next.place(relx=0.75, rely=0.8, relwidth=0.25, relheight=0.2)

    # Hera Page (code serves same purpose as previous pages)
    elif selection == 'Hera':
        hera = tk.Toplevel(bg='silver')
        hera.geometry("500x600")
        hera.title("Hera")

        image1 = Image.open("GreekGodBanners/Hera.png")
        resized_image = image1.resize((125, 175), Image.ANTIALIAS)
        test = ImageTk.PhotoImage(resized_image)
        label1 = tk.Label(hera, image=test, bg='silver')
        label1.image = test
        label1.place(relx=0.33, rely=0.05, relwidth=0.33, relheight=0.33)

        lower_frame = tk.Frame(hera, bg='thistle', bd=5)
        lower_frame.place(relx=0.5, rely=0.40, relwidth=0.75, relheight=0.5, anchor='n')

        text = tk.Message(lower_frame,
                          text="Goddess of Marriage, Mothers and Families\n\nWife of Zeus. Prefers dressing simple with "
                               "a modest silver crown. She usually appears as an older woman or as a bird when hiding or "
                               "spying. She does not care for demigods, children of both divine and mortal nature, as they"
                               " usually are the product of adultery/infidelity.\n\n"
                               "Symbols: the Pomegranate, the Cow, the Peacock\n\nRoman name: Juno",
                          bg='thistle')
        text.place(relx=0.05, rely=0.05, relwidth=.9, relheight=0.7)

        # previous = tk.Button(lower_frame, text="<", fg='black', font=40)
        # previous.place(relx=0, rely=0.8, relwidth=0.25, relheight=0.2)

        mainscreen = tk.Button(lower_frame, text="Search Another God/Goddess", fg='black', font=40,
                               command=lambda: hera.destroy())
        mainscreen.place(relx=0.25, rely=0.8, relwidth=0.5, relheight=0.2)

        # next = tk.Button(lower_frame, text=">", fg='black', font=40)
        # next.place(relx=0.75, rely=0.8, relwidth=0.25, relheight=0.2)

    # Hermes Page (code serves same purpose as previous pages)
    elif selection == 'Hermes':
        hermes = tk.Toplevel(bg='orange')
        hermes.geometry("500x600")
        hermes.title("Hermes")

        image1 = Image.open("GreekGodBanners/Hermes.png")
        resized_image = image1.resize((125, 175), Image.ANTIALIAS)
        test = ImageTk.PhotoImage(resized_image)
        label1 = tk.Label(hermes, image=test, bg='orange')
        label1.image = test
        label1.place(relx=0.33, rely=0.05, relwidth=0.33, relheight=0.33)

        lower_frame = tk.Frame(hermes, bg='lightsteelblue', bd=5)
        lower_frame.place(relx=0.5, rely=0.40, relwidth=0.75, relheight=0.5, anchor='n')

        text = tk.Message(lower_frame,
                          text="God of Travelers, Merchants and Thieves\n\nHe is also known to me the Messenger of the"
                               " Gods. He holds the caduceus, a winged staff with two snakes circling it. Hermes is known"
                               " to be a troublemaker. He also gave Apollo his lyre to distract him from one of his tricks."
                               "\n\nSymbols: the Caduceus\n\nRoman name: Mercury",
                          bg='lightsteelblue')
        text.place(relx=0.05, rely=0.05, relwidth=.9, relheight=0.7)

        # previous = tk.Button(lower_frame, text="<", fg='black', font=40)
        # previous.place(relx=0, rely=0.8, relwidth=0.25, relheight=0.2)

        mainscreen = tk.Button(lower_frame, text="Search Another God/Goddess", fg='black', font=40,
                               command=lambda: hermes.destroy())
        mainscreen.place(relx=0.25, rely=0.8, relwidth=0.5, relheight=0.2)

        # next = tk.Button(lower_frame, text=">", fg='black', font=40)
        # next.place(relx=0.75, rely=0.8, relwidth=0.25, relheight=0.2)

    # Poseidon Page (code serves same purpose as previous pages)
    elif selection == 'Poseidon':
        poseidon = tk.Toplevel(bg='midnightblue')
        poseidon.geometry("500x600")
        poseidon.title("Poseidon")

        image1 = Image.open("GreekGodBanners/Poseidon.png")
        resized_image = image1.resize((125, 175), Image.ANTIALIAS)
        test = ImageTk.PhotoImage(resized_image)
        label1 = tk.Label(poseidon, image=test, bg='midnightblue')
        label1.image = test
        label1.place(relx=0.33, rely=0.05, relwidth=0.33, relheight=0.33)

        lower_frame = tk.Frame(poseidon, bg='skyblue', bd=5)
        lower_frame.place(relx=0.5, rely=0.40, relwidth=0.75, relheight=0.5, anchor='n')

        text = tk.Message(lower_frame,
                          text="God of the Sea\n\nThe middle of the three brothers. He was believed to have rapid"
                               " mood swings. He created the horse out of sea foam to impress Demeter. He can "
                               "destroy cities with earthquakes or sink entire fleets in a blink of an eye before"
                               " calming down to perfect stillness as if nothing happened.\n\n"
                               "Symbols: the Trident, the Horse\n\nRoman name: Neptune",
                          bg='skyblue')
        text.place(relx=0.05, rely=0.05, relwidth=.9, relheight=0.7)

        # previous = tk.Button(lower_frame, text="<", fg='black', font=40)
        # previous.place(relx=0, rely=0.8, relwidth=0.25, relheight=0.2)

        mainscreen = tk.Button(lower_frame, text="Search Another God/Goddess", fg='black', font=40,
                               command=lambda: poseidon.destroy())
        mainscreen.place(relx=0.25, rely=0.8, relwidth=0.5, relheight=0.2)

        # next = tk.Button(lower_frame, text=">", fg='black', font=40)
        # next.place(relx=0.75, rely=0.8, relwidth=0.25, relheight=0.2)

    # Zeus Page (code serves same purpose as previous pages)
    elif selection == 'Zeus':
        zeus = tk.Toplevel(bg='darkgoldenrod')
        zeus.geometry("500x600")
        zeus.title("Zeus")

        image1 = Image.open("GreekGodBanners/Zeus.png")
        resized_image = image1.resize((125, 175), Image.ANTIALIAS)
        test = ImageTk.PhotoImage(resized_image)
        label1 = tk.Label(zeus, image=test, bg='darkgoldenrod')
        label1.image = test
        label1.place(relx=0.33, rely=0.05, relwidth=0.33, relheight=0.33)

        lower_frame = tk.Frame(zeus, bg='deepskyblue', bd=5)
        lower_frame.place(relx=0.5, rely=0.40, relwidth=0.75, relheight=0.5, anchor='n')

        text = tk.Message(lower_frame,
                          text="God of the Sky\n\nThe youngest of the three brothers. Zeus rules over the unruly lot of"
                               " the gods. Rules don't concern him. He was known to be unfaithful to Hera, "
                               "resulting in many demigods. He threw Hephaestus off Mt. Olympus due to his looks. He"
                               " killed his father, Cronus, to free his siblings after Cronus ate them.\n\n"
                               "Symbols: the Lightning Bolt, the Eagle\n\nRoman name: Jupiter",
                          bg='deepskyblue')
        text.place(relx=0.05, rely=0.05, relwidth=.9, relheight=0.7)

        # previous = tk.Button(lower_frame, text="<", fg='black', font=40)
        # previous.place(relx=0, rely=0.8, relwidth=0.25, relheight=0.2)

        mainscreen = tk.Button(lower_frame, text="Search Another God/Goddess", fg='black', font=40,
                               command=lambda: zeus.destroy())
        mainscreen.place(relx=0.25, rely=0.8, relwidth=0.5, relheight=0.2)

        # next = tk.Button(lower_frame, text=">", fg='black', font=40)
        # next.place(relx=0.75, rely=0.8, relwidth=0.25, relheight=0.2)


# main page window
root = tk.Tk()  # Sets home page window
root.title("Greek Knowledge Finder")  # Sets title for home page

canvas = tk.Canvas(root, height=250, width=600)  # Defines canvas and size
canvas.pack()  # Places canvas

# Frame for photo
large = tk.Frame(root, bg='gray')  # Frame for background photo
large.place(relx=0, rely=0, relwidth=1, relheight=1)  # Frame location placement

# main page photo
photo = tk.PhotoImage(file="building1.png")  # Sets photo for home page
photolabel = tk.Label(large, image=photo)  # Label for photo
photolabel.place(relwidth=1, relheight=1)  # Label location placement

# frame for search bar
frame = tk.Frame(large, bg='black', bd=5)  # Sets frame for menu
frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.5, anchor='n')  # Menu frame placement

# Text above list
label = tk.Label(frame, text="Learn About the Greek God or Goddess:", bg='black', fg='white', font=100)  # Adds text above list
label.place(relx=0, rely=0, relwidth=1, relheight=0.5)  # Text above list placement

# Selection list
gods = tk.StringVar()  # Setting up string variable list for dropdown
gods.set(('Aphrodite', 'Apollo', 'Ares', 'Artemis', 'Athena', 'Demeter', 'Dionysus', 'Hades',
          'Hephaestus', 'Hera', 'Hermes', 'Poseidon', 'Zeus'))
dropdown = tk.Listbox(frame, listvariable=gods, bg='white', fg='black',
                      height=13, highlightcolor='gray', selectmode='single', font=40)  # Formatting list with defined options and styling
dropdown.place(relx=0, rely=0.5, relwidth=0.65, relheight=0.5)  # List location placement

# search button
search = tk.Button(frame, text="Search", fg='blue', font=40, command=lambda: [getSelection(dropdown)])  # Search button function
search.place(relx=0.7, rely=0.5, relwidth=0.3, relheight=0.5)  # Search button placement

root.mainloop()
