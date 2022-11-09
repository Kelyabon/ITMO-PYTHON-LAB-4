import random
import string
from tkinter import *
from pygame import mixer


mixer.init()
mixer.music.load('bg_music.mp3')

mixer.music.play(-1)
nums_ratio = 1
letters = string.ascii_uppercase
letters_ratio = 2
value_interval = [12, 18]

window = Tk()
width = 850
height = 395
c_width = round(width / 2)
c_height = round(height / 2)
window.title("Генератор ключа для Cyberpunk 2077")
window.geometry(f'{width}x{height}')
window.resizable(width=False, height=False)
image = PhotoImage(file='bg_image.png')
frame = Frame(window)
canvas = Canvas(frame, bg='black')

frame.pack(fill=BOTH, expand=1)
canvas.pack(fill=BOTH, expand=1, )

bg = canvas.create_image(width / 2, height / 2, image=image)
button = Button(text='Сгенерировать ключ', background='black', foreground='lime', font=('Arial', 15))
button.place(relx=0.38, rely=0.85)


def generate_key():
    letters_amount = random.choice(range(12))
    while letters_amount * letters_ratio + (12 - letters_amount) * nums_ratio not in range(value_interval[0],
                                                                                           value_interval[1]):
        letters_amount = random.choice(range(12))
    nums_amount = 12 - letters_amount
    key_letters_indexes = random.choices(range(len(letters)), k=letters_amount)
    key_symbols = []
    for letter_index in key_letters_indexes:
        key_symbols += letters[letter_index]
    key_symbols += random.choices(range(10), k=nums_amount)
    new_key = ''
    for i in range(0, 12):
        symbol = random.choice(key_symbols)
        key_symbols.remove(symbol)
        new_key += str(symbol)
        if i in [3, 7]:
            new_key += '-'
    return new_key


key = ''
key_label = Label(text='', foreground='lime', font=('Arial', 15))
key_label.place(relx=0.1, rely=0.85)


def button_pressed(event):
    global key
    try:
        button.destroy()
    finally:
        pass
    bg_load = canvas.create_oval(c_width - 50, c_height - 50, c_width + 50, c_height + 50, fill='black')
    ball = canvas.create_oval(c_width - 32, c_height - 7, c_width - 18, c_height + 7, tags='ball',
                              fill='white')
    ball_2, ball_3, ball_4 = None, None, None
    for b in range(1):
        for i in range(100):
            if i < 50:
                x_3 = y_4 = -1
                x_1 = y_2 = 1
                if i < 25:
                    y = x_4 = 1
                    x_2 = y_3 = -1
                else:
                    y = x_4 = -1
                    x_2 = y_3 = 1
            else:
                x_3 = y_4 = 1
                x_1 = y_2 = -1
                if i < 75:
                    y = x_4 = -1
                    x_2 = y_3 = 1
                else:
                    x_2 = y_3 = -1
                    y = x_4 = 1
            if i == 25 and not ball_2:
                ball_2 = canvas.create_oval(c_width - 32, c_height - 7, c_width - 18, c_height + 7, tags='ball',
                                            fill='white')
            if i == 50 and not ball_3:
                ball_3 = canvas.create_oval(c_width - 32, c_height - 7, c_width - 18, c_height + 7, tags='ball',
                                            fill='white')
            if i == 75 and not ball_4:
                ball_4 = canvas.create_oval(c_width - 32, c_height - 7, c_width - 18, c_height + 7, tags='ball',
                                            fill='white')
            canvas.move(ball, x_1, y)
            canvas.update()
            if ball_2:
                canvas.move(ball_2, x_2, y_2)
                canvas.update()
            if ball_3:
                canvas.move(ball_3, x_3, y_3)
                canvas.update()
            if ball_4:
                canvas.move(ball_4, x_4, y_4)
                canvas.update()
            canvas.after(10)
    canvas.after(40)
    canvas.delete(ball, ball_2, ball_3, ball_4, bg_load)
    # canvas.delete(bg)
    new_key = generate_key()
    while new_key == key:
        new_key = generate_key()
    key = new_key
    key_label.config(text=f'Новый ключ: {key}')
    key_label.place(relx=0.1, rely=0.85)
    button_2.place(relx=0.7, rely=0.85)


button.bind('<Button-1>', button_pressed)

button_2 = Button(text='Сгенерировать новый ключ', background='black', foreground='lime', font=('Arial', 10))


def new_button_pressed(event):
    button_2.place_forget()
    button_pressed(event)


button_2.bind('<Button-1>', new_button_pressed)

window.mainloop()
