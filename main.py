import tkinter as tk
from tkinter import messagebox

def adicionar_contato():
    nome = entry_nome.get()
    telefone = entry_telefone.get()

if nome and telefone:
    lista_contatos.insert(tk.END, f'{nome}:{telefone}')
    entry_nome.delete(0, tk.END)
    entry_telefone.delete(0, tk.END)

else:
    messagebox.showwarning("AVISO", "Preencha os campos corretamente")

    def remove_contato():
        try:
            select_contato = lista_contato.get(lista_contatos.curselection())
            lista_contatos.delete(lista_contatos.curselection())

        except:
            messagebox.showwarning('AVISO', 'Selecione para remover')

            janela = tk.Tk()
            janela.title('TELA DE CADASTRO')

            label_nome = tk.Label(janela, text='nome:')
            label_nome.pack()

            entry_nome = tk.Entry(janela)
            entry_nome.pack()

            label_telefone = tk.Entry(janela, text= 'TELEFONE:' , font= 'Verdana' , fg='green')
            label_telefone.pack()
            entry_telefone = tk.Entry(janela)
            entry_telefone.pack()

            btn = tk.Button(janela, text= 'CADASTRAR' , command= adicionar_contato)
            btn.pack()

            lista_contatos = tk.Listbox(janela)
            lista_contatos.pack()

            btn_remove = tk.Button(janela, text= 'DELETE' , command=remove_contato)
            btn_remove.pack()

            janela.mainloop()

