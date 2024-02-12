import customtkinter

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("green")


def button_callback():
    print("Button clicked")

app = customtkinter.CTk()
app.geometry("400x150")

button = customtkinter.CTkButton(app, text = "My button", command=button_callback)
button.pack(padx=20, pady=20)

app.mainloop()