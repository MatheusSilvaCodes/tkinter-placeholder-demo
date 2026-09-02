import tkinter as tk

TEXTO_PADRAO = "Digite seu nome aqui..."


class AplicacaoSaudacao:

    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Saudação com Placeholder Automático")
        self.root.geometry("320x200")

        self._criar_widgets()

    def _criar_widgets(self):
        # Campo de entrada com estilo inicial (cinza)
        self.entry_nome = tk.Entry(self.root, width=28, fg="gray")
        self.entry_nome.pack(pady=15)

        # Insere a dica visual e vincula os eventos
        self.entry_nome.insert(0, TEXTO_PADRAO)
        self.entry_nome.bind("<FocusIn>", self._ao_ganhar_foco)
        self.entry_nome.bind("<FocusOut>", self._ao_perder_foco)

        # Botão de envio
        self.botao = tk.Button(
            self.root, text="Enviar", command=self._saudar_usuario
        )
        self.botao.pack(pady=5)

        # Rótulo de mensagem
        self.label_boas_vindas = tk.Label(
            self.root, text="", font=("Arial", 10, "bold")
        )
        self.label_boas_vindas.pack(pady=15)

    def _ao_ganhar_foco(self, event):
        if self.entry_nome.get() == TEXTO_PADRAO:
            self.entry_nome.delete(0, tk.END)
            self.entry_nome.config(fg="black")

    def _ao_perder_foco(self, event):
        if self.entry_nome.get().strip() == "":
            self.entry_nome.insert(0, TEXTO_PADRAO)
            self.entry_nome.config(fg="gray")

    def _saudar_usuario(self):
        nome = self.entry_nome.get().strip()
        if nome and nome != TEXTO_PADRAO:
            self.label_boas_vindas.config(text=f"Olá, {nome}!", fg="green")
        else:
            self.label_boas_vindas.config(
                text="Por favor, digite seu nome.", fg="red"
            )


if __name__ == "__main__":
    janela = tk.Tk()
    app = AplicacaoSaudacao(janela)
    janela.mainloop()
