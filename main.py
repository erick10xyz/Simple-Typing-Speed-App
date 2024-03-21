from tkinter import *
import math


GREEN = "#9bdeac"
FONT_NAME = "Courier"
timer = None

# Resetting Timer
def reset_timer():
    window.after_cancel(timer)
    timer_label.config(text="00:00")
    typing_label.config(text='Type a paragraph below for 1 minute: ')
    window_text.delete(1.0, END)


def start_timer():
    count_down(60)

# 1  minute countdown
def count_down(count):
    count_min = math.floor(count/ 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    timer_label.config(text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)

    elif count == 0:
        typing_label.config(text='Stop Typing, 1 minute is done!')
        count_word()

# Count the word you type within 1 minute marker.
def count_word():
    words_typed = window_text.get('1.0', END)
    word_list = words_typed.split()
    count_words = len(word_list)
    typing_label.config(text=f'You type {count_words} words in 1 minute')


# Simple user interface of speed typing test
window = Tk()
window.title("Typing Speed Test")
window.config(padx=50, pady=50, bg=GREEN)

timer_label = Label(window, text='00:00', font=(FONT_NAME, 35, "bold"))
timer_label.grid(column=1, row=3, pady=10)
# timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
# canvas.grid(column=1, row=0)

start_button = Button(window, text='Start', command=start_timer).grid(column=0, row=1)
reset_button = Button(window, text='Reset', command=reset_timer).grid(column=3, row=1)

typing_label = Label(window, text='Type a paragraph below for 1 minute: ')
typing_label.config(font =("Courier", 14))
typing_label.grid(column=1, row=0)

window_text = Text(window, height = 20, width = 75)
window_text.grid(column=1, row=1)


window.mainloop()

