import tkinter as tk
import random

class CoresApp:
    def __init__(self,raiz):
        self.raiz = raiz
        self.cores = ['red', 'blue', 'green', 'purple', 'pink', 'black', 'white']
        raiz.title('Janela divertida')
        raiz.geometry('330x200')
        tk.Label(raiz, text='Janela Sobre!', font=('Arial', 14))
        tk.Button(raiz, text='Mudar cor', command=self.mudar_cor).pack(pady=10)

    def mudar_cor(self):
        self.raiz.config(bg=random.choice(self.cores))

if __name__ == '__main__':
    raiz = tk.Tk()
    CoresApp(raiz)
    raiz.mainloop()        