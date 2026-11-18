import tkinter as tk
from tkinter import ttk, messagebox, Frame, filedialog
import csv
import database

class SupriDesk():
    def __init__(self, root):
        self.root = root
        self.root.title('SUPRIDESK') 
        self.root.configure(background = 'snow')
        self.root.minsize(1000,750)
        
        database.criar_tabela()
        
        self.frame_tela()
        self.criando_widgets()
        
        self.atualizar_tabela()

    def frame_tela(self):
        self.frame_1 = Frame(self.root, bd=2, bg='light grey', highlightbackground='black', highlightthickness=3)
        self.frame_1.place(relx=0.025, rely=0.02, relwidth=0.95, relheight=0.46)

        self.frame_2 = Frame(self.root, bd=2, bg='light grey', highlightbackground='black', highlightthickness=3)
        self.frame_2.place(relx=0.025, rely=0.5, relwidth=0.95, relheight=0.46)

    def criando_widgets(self):
        # FRAME SUPERIOR
        label_cadastro = tk.Label(self.frame_1, text='CADASTRO', font=('impact', 15 , 'bold'), bg='light grey')
        label_cadastro.place(x=15, y=0)

        label_setor = tk.Label(self.frame_1, text='SETOR', font=('times new roman', 10, 'bold'), bg='light grey')
        label_setor.place(x=15, y=40)
        self.entry_setor = ttk.Entry(self.frame_1, width=25)
        self.entry_setor.place(x=120, y=40)

        label_material = tk.Label(self.frame_1, text='MATERIAL', font=('times new roman', 10, 'bold'), bg='light grey')
        label_material.place(x=15, y=80)
        self.entry_material = ttk.Entry(self.frame_1, width=25) 
        self.entry_material.place(x=120, y=80)

        label_quantidade = tk.Label(self.frame_1, text='QUANTIDADE', font=('times new roman', 10, 'bold'), bg='light grey')
        label_quantidade.place(x=15, y=120)
        self.entry_quantidade = ttk.Entry(self.frame_1, width=25)
        self.entry_quantidade.place(x=120, y=120)

        label_prioridade = tk.Label(self.frame_1, text="PRIORIDADE:", font=('times new roman', 10, 'bold'), bg='light grey')
        label_prioridade.place(x=15, y=160)
        self.combo_prioridade = ttk.Combobox(self.frame_1, values=["Normal", "Alta"], width=23, state="readonly")
        self.combo_prioridade.place(x=120, y=160)
        self.combo_prioridade.set("Normal")

        btn_cadastro = tk.Button(self.frame_1, text="CADASTRAR PEDIDOS", bg='SteelBlue1', fg='white', font=('Arial', 10, 'bold'), command=self.cadastro_pedido)
        btn_cadastro.place(x=100, y=210, width=170, height=35)

        separador = tk.Frame(self.frame_1, bg='dark gray', width=3)
        separador.place(x=350, y=40, height=240)

        label_pesquisar_titulo = tk.Label(self.frame_1, text="PESQUISA", font=('impact', 15, 'bold'), bg='light grey')
        label_pesquisar_titulo.place(x=380, y=0)

        label_busca = tk.Label(self.frame_1, text="BUSCAR (SETOR/MATERIAL):", bg='light grey', font=('times new roman', 10))
        label_busca.place(x=380, y=40)
        self.entry_busca = ttk.Entry(self.frame_1, width=25)
        self.entry_busca.place(x=580, y=40)

        label_filtro_status = tk.Label(self.frame_1, text="FILTRAR POR STATUS:", bg='light grey', font=('Arial', 10))
        label_filtro_status.place(x=380, y=100)
        self.combo_status_filtro = ttk.Combobox(self.frame_1, values=["Todos", "Pendente", "Em atendimento", "Atendida"], width=23, state="readonly")
        self.combo_status_filtro.place(x=580, y=100)
        self.combo_status_filtro.set("Todos")

        btn_buscar = tk.Button(self.frame_1, text=" PESQUISAR ", bg='SteelBlue1', fg='white', font=('Arial', 10, 'bold'), command=self.executar_pesquisa)
        btn_buscar.place(x=540, y=170, width=160, height=30)

        btn_limpar = tk.Button(self.frame_1, text="LIMPAR PESQUISA", bg='SteelBlue1', fg='white', font=('Arial', 10, 'bold'), command=self.limpar_filtros)
        btn_limpar.place(x=715, y=170, width=150, height=30)

        # FRAME INFERIOR
        lbl_tabela_titulo = tk.Label(self.frame_2, text="HISTÓRICO DE PEDIDOS", font=('impact', 15, 'bold'), bg='light grey')
        lbl_tabela_titulo.place(x=15, y=10)

        colunas = ("id", "setor", "quantidade", "material", "prioridade", "status", "data_hora")
        self.tree = ttk.Treeview(self.frame_2, columns=colunas, show="headings", selectmode="browse")

        self.tree.heading("id", text="ID")
        self.tree.heading("setor", text="Setor")
        self.tree.heading("quantidade", text="Qtd")
        self.tree.heading("material", text="Material")
        self.tree.heading("prioridade", text="Prioridade")
        self.tree.heading("status", text="Status")
        self.tree.heading("data_hora", text="Data/Hora")

        self.tree.column("id", width=40, anchor="center")
        self.tree.column("setor", width=120, anchor="w")
        self.tree.column("quantidade", width=60, anchor="center")
        self.tree.column("material", width=180, anchor="w")
        self.tree.column("prioridade", width=90, anchor="center")
        self.tree.column("status", width=120, anchor="center")
        self.tree.column("data_hora", width=150, anchor="center")

        scrollbar = ttk.Scrollbar(self.frame_2, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        self.tree.place(x=15, y=45, width=900, height=215)
        scrollbar.place(x=915, y=45, height=215)

        btn_atender = tk.Button(self.frame_2, text="Iniciar Atendimento\n(Pendente -> Em atendimento)", bg='green', fg='white', font=('Arial', 9, 'bold'), command=lambda: self.mudar_status("Em atendimento"))
        btn_atender.place(x=15, y=275, width=220, height=40)
        
        btn_concluir = tk.Button(self.frame_2, text="Finalizar Atendimento\n(Em atendimento -> Atendida)", bg='green', fg='white', font=('Arial', 9, 'bold'), command=lambda: self.mudar_status("Atendida"))
        btn_concluir.place(x=375, y=275, width=220, height=40)

        btn_csv = tk.Button(self.frame_2, text="Exportar CSV", bg='red', fg='white', font=('Arial', 9, 'bold'), command=self.exportar_csv)
        btn_csv.place(x=735, y=275, width=180, height=40)

    def cadastro_pedido(self):
        setor = self.entry_setor.get().strip()
        material = self.entry_material.get().strip()
        quantidade_str = self.entry_quantidade.get().strip()
        prioridade = self.combo_prioridade.get()

        if not setor or not material or not quantidade_str:
            messagebox.showerror("Erro de Validação", "Todos os campos devem ser preenchidos!", parent=self.root)
            return

        try:
            quantidade = int(quantidade_str)
            if quantidade <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Erro de Validação", "A quantidade deve ser um número inteiro positivo diferente de 0!", parent=self.root)
            return

        database.cadastrar(setor, quantidade, material, prioridade)
        messagebox.showinfo("Sucesso", "Solicitação cadastrada com sucesso!", parent=self.root)
        
        self.entry_setor.delete(0, tk.END)
        self.entry_material.delete(0, tk.END)
        self.entry_quantidade.delete(0, tk.END)
        self.combo_prioridade.set("Normal")
        
        self.atualizar_tabela()

    def atualizar_tabela(self, registros=None):
        for item in self.tree.get_children():
            self.tree.delete(item)
            
        if registros is None:
            registros = database.cobsultar_bdd()
            
        for reg in registros:
            self.tree.insert("", "end", values=reg)

    def executar_pesquisa(self):        
        termo = self.entry_busca.get().strip()
        status = self.combo_status_filtro.get()
        registros = database.pesquisar_filtrar(termo, status)
        self.atualizar_tabela(registros)

    def limpar_filtros(self):
        self.entry_busca.delete(0, tk.END)
        self.combo_status_filtro.set("Todos")
        self.atualizar_tabela()

    def mudar_status(self, novo_status):
        selecionado = self.tree.selection()
        if not selecionado:
            messagebox.showwarning("Seleção", "Selecione uma solicitação na tabela!", parent=self.root)
            return
        item = self.tree.item(selecionado[0])
        valores = item['values']
        id_pedido = valores[0]
        status_atual = valores[5]

        if status_atual == "Pendente" and novo_status == "Em atendimento":
            database.atualizar_status(id_pedido, "Em atendimento")
            messagebox.showinfo("Sucesso", f"Solicitação {id_pedido} alterada para 'Em atendimento'.", parent=self.root)
        elif status_atual == "Em atendimento" and novo_status == "Atendida":
            database.atualizar_status(id_pedido, "Atendida")
            messagebox.showinfo("Sucesso", f"Solicitação {id_pedido} concluída ('Atendida').", parent=self.root)
        elif status_atual == "Atendida":
            messagebox.showerror("Erro de Fluxo", "Esta solicitação já foi concluída ('Atendida') e não pode ser alterada ou repetida.", parent=self.root)
            return
        elif status_atual == "Pendente" and novo_status == "Atendida":
            messagebox.showerror("Erro de Fluxo", "Transição inválida! Uma solicitação 'Pendente' deve ir para 'Em atendimento' antes de ser 'Atendida'.", parent=self.root)
            return
        elif status_atual == novo_status:
            messagebox.showwarning("Aviso", f"A solicitação já está com o status '{status_atual}'.", parent=self.root)
            return
        else:
            messagebox.showerror("Erro de Fluxo", f"Transição de '{status_atual}' para '{novo_status}' não permitida.", parent=self.root)
            return
        
        self.executar_pesquisa() if self.entry_busca.get().strip() or self.combo_status_filtro.get() != "Todos" else self.atualizar_tabela()

    def exportar_csv(self):
        arquivo = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("Arquivos CSV", "*.csv")], title="Salvar Histórico CSV")
        if not arquivo:
            return

        try:
            registros = database.cobsultar_bdd()
            with open(arquivo, mode='w', newline='', encoding='utf-8-sig') as f:
                writer = csv.writer(f)
                writer.writerow(["ID", "Setor", "Quantidade", "Material", "Prioridade", "Status", "Data/Hora"])
                for reg in registros:
                    writer.writerow(reg)
            messagebox.showinfo("Sucesso", f"Histórico exportado com sucesso para:\n{arquivo}", parent=self.root)
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao exportar CSV: {e}", parent=self.root)
            
if __name__ == '__main__':
    janela = tk.Tk()
    SupriDesk(janela)    
    janela.mainloop()
