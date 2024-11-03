import tkinter as tk

class Kalkulacka:
    def __init__(self, master):
        self.master = master
        master.title("CalculatorApp - simple calculator coded by NNW Developer")

        self.entry = tk.Entry(master, width=16, font=('Arial', 24), borderwidth=5)
        self.entry.grid(row=0, column=0, columnspan=4)

        self.create_buttons()

    def create_buttons(self):
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', 'C', '=', '+'
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            b = tk.Button(self.master, text=button, font=('Arial', 18), width=4, height=2)
            b.grid(row=row_val, column=col_val)
            b.bind("<Button-1>", self.on_button_click)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def on_button_click(self, event):
        current = self.entry.get()
        button_text = event.widget.cget("text")

        if button_text == "C":
            self.entry.delete(0, tk.END)
        elif button_text == "=":
            self.calculate_result()
        else:
            self.entry.insert(tk.END, button_text)

    def calculate_result(self):
        try:
            expression = self.entry.get().replace("×", "*").replace("÷", "/")  # Pokud chcete používat jiný zápis
            result = eval(expression)
            self.entry.delete(0, tk.END)
            self.entry.insert(0, str(result))
        except Exception as e:
            self.entry.delete(0, tk.END)
            self.entry.insert(0, "Chyba")

if __name__ == "__main__":
    root = tk.Tk()
    kalkulacka = Kalkulacka(root)
    root.mainloop()
