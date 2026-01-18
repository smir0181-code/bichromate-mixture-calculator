import customtkinter

customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

app = customtkinter.CTk()
app.geometry("400x580")
app.title("Расчет водо-бихроматной смеси")
def button_callback():
    try:
        val1=int(entry_1.get())
        val2=int(entry_2.get())
        val3=int(entry_3.get())
        a=val1/val2
        v=val3/a
        voda=val3-v
        label_1 = customtkinter.CTkLabel(master=frame_1, text=f'Бихромат  {round(v,2)}  ({round(v/0.061)}cm)         ')
        label_1.place(x=120,y=400)
        label_1 = customtkinter.CTkLabel(master=frame_1, text=f'Вода  {round(voda, 2)}  ({round(voda / 0.061)}cm)    ')
        label_1.place(x=120,y=450)
    except:
        label_1 = customtkinter.CTkLabel(master=frame_1, text='Не верный ввод              ')
        label_1.place(x=120,y=400)
        label_1 = customtkinter.CTkLabel(master=frame_1, text='                                    ')
        label_1.place(x=120,y=450)

frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=20, padx=20, fill="both", expand=True)



entry_1 = customtkinter.CTkEntry(master=frame_1, placeholder_text="Cr2O3-4/1")
entry_1.pack(pady=17, padx=10)


entry_2 = customtkinter.CTkEntry(master=frame_1, placeholder_text="Cr2O3-5/1")
entry_2.pack(pady=17, padx=10)

entry_3 = customtkinter.CTkEntry(master=frame_1, placeholder_text="Кубы")
entry_3.pack(pady=17, padx=1)




button_1 = customtkinter.CTkButton(master=frame_1,text="Расчитать", command=button_callback)
button_1.pack(pady=70)


app.mainloop()