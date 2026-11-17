import tkinter as tk

janela = tk.Tk()
label = tk.Label(
    text = 'Brincando com tkinter',
    foreground='red',
    background='black'
)

botao = tk.Button(
    text = 'Botão',
    width=25,
    height=5,
    bg='blue',
    fg='yellow'
)

label.pack()
botao.pack()
janela.mainloop()