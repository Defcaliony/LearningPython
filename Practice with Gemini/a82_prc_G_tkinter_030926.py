import random
import tkinter as tk

#Create general window
root = tk.Tk()
root.title("Coin eater")
root.geometry("500x500")
root.resizable(False, False)

#Wall for painting
canvas = tk.Canvas(root, width=500, height=400, bg="#1e1e2e")
canvas.pack()

#Score
score = 0
score_label = tk.Label(
    root, text=f"Score: {score}", font=("Arial", 16, "bold")
)
score_label.pack(pady=10)

#Create player
player = canvas.create_rectangle(235, 235, 265, 265, fill="#50fa7b")

#Create coin
coin = canvas.create_oval(100, 100, 120, 120, fill="#FFF200")

def respawn_coin():
    """To move coin to random places"""
    x = random.randint(20, 470)
    y = random.randint(20, 370)
    canvas.coords(coin, x, y, x + 20, y + 20)

def check_collision():
    """To check collision of coin"""
    global score
    p_pos = canvas.coords(player)
    c_pos = canvas.coords(coin)

    #check two rectangle
    if (
        p_pos[2] >= c_pos[0]
        and p_pos[0] <= c_pos[2]
        and p_pos[3] >= c_pos[1]
        and p_pos[1] <= c_pos[3]
    ):
        score += 1
        score_label.config(text=f"Score: {score}")
        respawn_coin()

def move_player(event):
    """To move"""
    step = 15
    if event.keysym == "Up":
        canvas.move(player, 0, -step)
    elif event.keysym == "Down":
        canvas.move(player, 0, step)
    elif event.keysym == "Left":
        canvas.move(player, -step, 0)
    elif event.keysym == "Right":
        canvas.move(player, step, 0)

    check_collision()

#
root.bind("<Up>", move_player)
root.bind("<Down>", move_player)
root.bind("<Left>", move_player)
root.bind("<Right>", move_player)

root.mainloop()