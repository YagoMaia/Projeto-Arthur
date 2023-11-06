import tkinter as tk

def countdown(count):
    # change text in label        
    label['text'] = count

    if count > 0:
        # call countdown again after 1000ms (1s)
        root.after(1000, countdown, count-1)

def mudar_timer(dif):
        atual = label['text']
        label['text'] = atual - dif

root = tk.Tk()

label = tk.Label(root)
label.place(x=35, y=15)

# call countdown first time    
countdown(5)
mudar_timer(2)
# root.after(0, countdown, 5)

root.mainloop()