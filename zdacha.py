import tkinter as tk
import customtkinter

class FrameForMoney(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.fontlabel = customtkinter.CTkFont(family="Times New Roman", size=30, weight="bold")
        self.fontforentry = customtkinter.CTkFont(family="Times New Roman", size=16, weight="bold")

        self.labels = []
        self.entries = []
        self.result_labels = []

        denominations = [1000, 500, 200, 100, 50, 20, 10, 5, 2, 1]

        for row, denomination in enumerate(denominations):
            label = customtkinter. CTkLabel(self, text=str(denomination), font=self.fontlabel)
            label.grid(row=row, column=0, padx=5, pady=5)
            entry = customtkinter.CTkEntry(self, placeholder_text=f"Введіть кількість купюр з цим номіналом {denomination}",
                                           font=self.fontforentry, width=350)
            entry.grid(row=row, column=1, padx=5, pady=5)
            result_label = customtkinter.CTkLabel(self, text="", font=self.fontlabel)
            result_label.grid(row=row, column=2, padx=5, pady=5)

            self.labels.append(label)
            self.entries.append(entry)
            self.result_labels.append(result_label)

        self.ButtonForShowing = customtkinter.CTkButton(self, text="Розрахувати кількість", hover_color="white",
                                                        text_color="black", height=70, width=90,
                                                        command=self.ResultMoney)
        self.ButtonForShowing.grid(row=row + 1, column=0, columnspan=3, pady=10)

    def ResultMoney(self):
        denominations = [1000, 500, 200, 100, 50, 20, 10, 5, 2, 1]

        for label, entry, result_label, denomination in zip(self.labels, self.entries, self.result_labels, denominations):
            value = int(entry.get())
            result_label.configure(text=f"Номіналом в {denomination} - {value}")



class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1200x900")
        self.title("Здачо калькулятор")

        self.fontlabel = customtkinter.CTkFont(family="Times New Roman", size=30, weight="bold")
        self.fontforentry = customtkinter.CTkFont(family="Times New Roman", size=16, weight="bold")

        self.labelfont = FrameForMoney(master=self, width=1200)
        self.labelfont.grid(row=0, column=0)


app = App()
app.mainloop()
