from tkinter import Tk

janela = Tk()
janela.title('Python wins!')

janela.geometry('600x250')
janela.eval('tk::Placewindow . center')
janela.mainloop()