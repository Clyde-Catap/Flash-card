from tkinter import *
import pandas
import random


BACKGROUND_COLOR = "#B1DDC6"

french_data = pandas.read_csv("data/french_words.csv")
french_dict = french_data.to_dict()
# print(french_dict["French"])
# print(french_dict)
# print(french_dict["French"][0])
# print(french_dict["English"][0])


lister = []

for x in french_dict["French"]:
    lister.append(x)

value = []

for g in lister:
    gg = french_dict["French"][g]
    value.append(gg)


new_french_word = {}



def random_french_word():
    global new_french_word, flip_timer, french_dict
    window.after_cancel(flip_timer)
    new_french_word = random.choice(french_dict["French"])
    card_front_frame.itemconfig(first_word, text="French", fill="black")
    card_front_frame.itemconfig(word, text=f"{new_french_word}", fill="black" )
    card_front.config(file="images/card_front.png")
    flip_timer = window.after(3000, func=flip_card)









def flip_card():
    english_index = value.index(new_french_word)
    english_correspondent = french_dict["English"][english_index]
    card_front.config(file="images/card_back.png")
    card_front_frame.itemconfig(first_word, text= "English", fill= "white")
    card_front_frame.itemconfig(word, text= english_correspondent, fill="white")



# UI BOI

window = Tk()
window.title("FLASH CARDOOO")
window.config(bg=BACKGROUND_COLOR)
window.config(padx=50, pady=30)
window.geometry("900x680")


flip_timer = window.after(3000, func=flip_card)




card_front = PhotoImage(file="images/card_front.png")
card_front_frame = Canvas(width=826, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_frame.create_image(10, 0, image = card_front, anchor= "nw")
first_word = card_front_frame.create_text(410, 150, text="French", anchor="center", font=("Ariel", 40, "italic"))
word = card_front_frame.create_text(410, 263, text="START", anchor="center", font=("Ariel", 60, "bold"))
card_front_frame.grid(column=0, row=0, columnspan=2)


check_img = PhotoImage(file="images/right.png")
check_button = Button(image=check_img, bg=BACKGROUND_COLOR, highlightthickness=0, command=random_french_word, bd=0)
check_button.grid(column=1, row=1)


cross_img = PhotoImage(file="images/wrong.png")
cross_button = Button(image=cross_img, highlightthickness=0, command=random_french_word, bd=0)
cross_button.grid(column=0, row=1)







random_french_word()







window.mainloop()
