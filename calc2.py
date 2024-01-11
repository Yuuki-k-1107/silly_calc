import tkinter as tk
from tkinter import StringVar
import pygame

# 音声ファイルの初期化とロード
pygame.mixer.init()
pygame.mixer.music.load("ac.wav")

def on_click(ch):
    if ch == 'AC':
        pygame.mixer.music.play()  # ACボタンを押すと音が鳴る
        display.set("")
    elif ch == 'C':
        display.set(display.get()[:-1])
    elif ch == '=':
        try:
            display.set(eval(display.get()))
        except Exception as e:
            display.set("Error")
    else:
        display.set(display.get() + ch)

# Tkinterウィンドウの作成
root = tk.Tk()
root.title("Calculator")

display = StringVar()

# ディスプレイ
entry = tk.Entry(root, textvariable=display, justify='right', font=('Arial', 20))
entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

# ボタン
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('AC', 5, 0), ('C', 5, 1)
]

for (text, row, col) in buttons:
    button = tk.Button(root, text=text, command=lambda ch=text: on_click(ch), width=5, height=2)
    button.grid(row=row, column=col, padx=5, pady=5)

root.mainloop()
