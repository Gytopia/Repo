import tkinter as tk
from typing import Any, Optional, Tuple, Union
import customtkinter

class FrameForMoneyEntered(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.fontlabel = customtkinter.CTkFont(family="Times New Roman", size=30, weight="bold")
        self.fontforentry = customtkinter.CTkFont(family="Times New Roman", size=16, weight="bold")

        self.labels = []
        self.entries = []
        self.result_labels = []

        denominations = [1000, 500, 200, 100, 50, 20, 10, 5, 2, 1, 0.5, 0.10]

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
        denominations = [1000, 500, 200, 100, 50, 20, 10, 5, 2, 1, 0.5, 0.10]

        total_amount = 0

        for label, entry, result_label, denomination in zip(self.labels, self.entries, self.result_labels, denominations):
            try:
                value = int(entry.get())
            except ValueError:
                value = 0
            result_label.configure(text=f"Номіналом в {denomination} - {value}")
            total_amount += denomination * value

        total_label_text = f"Загальна сума: {total_amount}"
        total_label = customtkinter.CTkLabel(self, text=total_label_text, font=self.fontlabel)
        total_label.grid(row=len(denominations) + 1, column=0, columnspan=3, pady=10)


class Change(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.fontlabel = customtkinter.CTkFont(family="Times New Roman", size=30, weight="bold")
        self.fontforentry = customtkinter.CTkFont(family="Times New Roman", size=16, weight="bold")
        
        self.labelzdacha = customtkinter.CTkLabel(self, text="Кількість здачі: ")
        self.labelzdacha.grid(row = 2, column = 0)
        
        self.labelresult = customtkinter.CTkLabel(self, text = "")
        self.labelresult.grid(row = 2, column = 1)
        
        self.labelcost = customtkinter.CTkLabel(self, text = "Ціна покупки:")
        self.labelcost.grid(row = 0, column = 0)
        
        self.price = customtkinter.CTkEntry(self, placeholder_text= "Ціна з копійками")
        self.price.grid(column = 1, row = 0)
        
        self.customer = customtkinter.CTkLabel(self, text = "Покупець дав:")
        self.customer.grid(row = 1, column = 0)
        
        self.entrycustomer = customtkinter.CTkEntry(self, placeholder_text = "Кількість грошей")
        self.entrycustomer.grid(row = 1, column = 1)
        
        self.buttoneva = customtkinter.CTkButton(self, text = "Розрахунок", command=self.CalculateExchange)
        self.buttoneva.grid(row = 3, column = 0)
        
    def CalculateExchange(self):
        self.total_change = float(self.entrycustomer.get()) - float(self.price.get())
        self.labelresult.configure(text = f"{str(self.total_change)}")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1200x900")
        self.title("Здачо калькулятор")

        self.fontlabel = customtkinter.CTkFont(family="Times New Roman", size=30, weight="bold")
        self.fontforentry = customtkinter.CTkFont(family="Times New Roman", size=16, weight="bold")

        self.labelfont = FrameForMoneyEntered(master=self, width=1200)
        self.labelfont.grid(row=0, column=0)
        
        self.framezdacha = Change(master=self, width = 300)
        self.framezdacha.grid(row = 0, column = 2, padx = 50)


app = App()
app.mainloop()
