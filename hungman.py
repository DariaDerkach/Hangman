'''Игра виселица.Берется словоб его нужно отгадать за 6 попыток или тебя повесят'''
from tkinter import *
import random

# Constants
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800
MARGIN = 100
BACKGROUND_COLOR = '#073B4C'
LINES_COLOR = 'orange'
BTN_COLOR = 'white'
TXT_COLOR = 'black'
SPEC_COLOR = 'red'
HEAD_COLOR = '#6153CC'
HAND_COLOR = '#66101F'
FOOT_COLOR = '#417B5A'
FG_COLOR = '#FFD400'
label_word = []
btn_alfa = []


def start_post_man():
    line_1 = canvas.create_line(MARGIN, WINDOW_HEIGHT - MARGIN, MARGIN, MARGIN, width=4, fill=LINES_COLOR)
    line_2 = canvas.create_line(MARGIN, MARGIN, WINDOW_WIDTH // 3, MARGIN, width=4, fill=LINES_COLOR)
    line_3 = canvas.create_line(WINDOW_WIDTH // 3, MARGIN, WINDOW_WIDTH // 3, MARGIN * 2, width=4, fill=LINES_COLOR)


def start_post_alphabet():
    shift_x = shift_y = 0
    count = 0

    for c in range(ord('А'), ord('Я') + 1):
        btn = Button(text=chr(c), bg=BTN_COLOR, foreground=TXT_COLOR, font=('Arial', 19), relief=SOLID)
        btn.place(x=WINDOW_HEIGHT - MARGIN * 2 + shift_x, y=MARGIN * 4.5 - shift_y)
        btn.bind('<Button-1>', lambda event: check_alfa(event, word))
        btn_alfa.append(btn)
        shift_x += 65
        count += 1

        if count == 8:
            shift_x = count = 0
            shift_y -= 65


def start_word():
    f = open('hungman_word')
    count = 0

    for s in f:
        count += 1
    num_word = random.randint(1, count)
    word = ''
    count = 0

    f = open('hungman_word', encoding='utf-8')

    for s in f:
        count += 1

        if count == num_word:
            word = s[:len(s):]
    word = word.upper()

    return word


def start_pos_word(word):
    shift = 0
    for i in range(len(word) - 1):
        label_under = Label(window, text='_', font=('Arial 24'), bg=BACKGROUND_COLOR, fg=FG_COLOR)
        label_under.place(x=WINDOW_HEIGHT - MARGIN * 2 + shift, y=MARGIN * 3.5)
        shift += 50
        label_word.append(label_under)


def draw(lifes):
    if lifes == 5:
        head = canvas.create_oval(WINDOW_WIDTH // 3 - 60, MARGIN * 1.5, WINDOW_WIDTH // 3 + 60, MARGIN * 2.5,
                                  fill=HEAD_COLOR)
    elif lifes == 4:
        body = canvas.create_oval(WINDOW_WIDTH // 3 - 25, MARGIN * 2.5, WINDOW_WIDTH // 3 + 25, MARGIN * 5,
                                  fill=HEAD_COLOR)
    elif lifes == 3:
        l_hand = canvas.create_line(WINDOW_WIDTH // 3 - 15, MARGIN * 3.5, WINDOW_WIDTH // 3 - 105, MARGIN * 2.4,
                                    width=6, fill=HAND_COLOR)

    elif lifes == 2:
        r_hand = canvas.create_line(WINDOW_WIDTH // 3 + 15, MARGIN * 3.5, WINDOW_WIDTH // 3 + 105, MARGIN * 2.4,
                                    width=6, fill=HAND_COLOR)

    elif lifes == 1:
        l_foot = canvas.create_line(WINDOW_WIDTH // 3 - 15, MARGIN * 4.5, WINDOW_WIDTH // 3 - 110, MARGIN * 7,
                                    width=7, fill=FOOT_COLOR)
    elif lifes == 0:
        r_foot = canvas.create_line(WINDOW_WIDTH // 3 + 15, MARGIN * 4.5, WINDOW_WIDTH // 3 + 110, MARGIN * 7, width=7,
                                    fill=FOOT_COLOR)
        game_over('lose')


def check_alfa(event, word):
    alpha = event.widget['text']
    pos = []

    for i in range(len(word)):
        if word[i] == alpha:
            pos.append(i)
    if pos:
        for i in pos:
            label_word[i].config(text='{}'.format(word[i]))
        count_alpha = 0
        for i in label_word:
            if i['text'].isalpha():
                count_alpha += 1
        if count_alpha == len(word) - 1:
            game_over('win')
    else:
        lifes = int(label_life.cget('text')) - 1
        if lifes != 0:
            label_life.config(text='  {}'.format(lifes))
        if lifes == 0:
            label_life.config(text='  {}'.format(lifes))

        draw(lifes)


def game_over(status):
    for btn in btn_alfa:
        btn.destroy()
    if status == "win":
        canvas.create_text(canvas.winfo_width() / 2 + 200, canvas.winfo_height() / 2, font=('Futura PT Heave', 50),
                           text='Ты выжил!\n', fill=SPEC_COLOR)
    else:
        canvas.create_text(canvas.winfo_width() / 2 + 200, canvas.winfo_height() / 2, font=('Futura PT Heave', 50),
                           text='Ты отбыл в мир иной!\n', fill=SPEC_COLOR)


if __name__ == '__main__':

    window = Tk()
    window.title('Hangman')
    window.resizable(False, False)

    lifes = 6

    label_text = Label(window, text='Жизни:', font=('Futura PT Heave', 40), foreground=TXT_COLOR)
    label_text.place(x=930, y=10)
    label_life = Label(window, text=' {}'.format(lifes), font=('Futura PT Heave', 40), foreground=TXT_COLOR)
    label_life.place(x=1110, y=10)

    canvas = Canvas(window, bg=BACKGROUND_COLOR, height=WINDOW_HEIGHT,
                    width=WINDOW_WIDTH)
    canvas.place(x=0, y=70)

    window.geometry('1200x880')

    start_post_man()
    start_post_alphabet()
    word = start_word()
    start_pos_word(word)
    window.mainloop()

    print(word)
