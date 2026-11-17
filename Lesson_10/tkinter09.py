import tkinter as tk

class PackFillApp:
    def __init__(self, raiz):
        faixas = [(100, 'red'), (50, 'green'), (25, 'blue')]
        for altura, cor in faixas:
            frame = tk.Frame(raiz, height=altura, bg=cor)
            frame.pack()

if __name__ == '__main__':
    raiz = tk.Tk()
    PackFillApp(raiz)
    raiz.mainloop()