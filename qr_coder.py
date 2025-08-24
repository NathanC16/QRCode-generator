import tkinter as tk
from tkinter import messagebox, filedialog
import qrcode
from PIL import Image, ImageTk

# Variável global para armazenar a imagem do QR Code e evitar garbage collection
qr_image_pil = None
qr_photo_tk = None

def gerar_qr_code():
    """Gera o QR Code com base no texto e opções selecionadas e o exibe na interface."""
    global qr_image_pil, qr_photo_tk

    data = entry_texto.get()
    if not data:
        messagebox.showwarning("Aviso", "Por favor, insira o texto ou URL para gerar o QR Code.")
        return

    try:
        # Pega as opções de cor e tamanho
        fill_color = var_cor.get()
        back_color = var_fundo.get()
        box_size = int(var_tamanho.get())

        # Cria o objeto QR Code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=box_size,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)

        # Cria a imagem do QR Code com as cores selecionadas
        qr_image_pil = qr.make_image(fill_color=fill_color, back_color=back_color)

        # Redimensiona a imagem para exibição, mantendo a proporção
        # Se a imagem for muito grande, o tkinter pode ter problemas
        max_size = 400
        if qr_image_pil.size[0] > max_size or qr_image_pil.size[1] > max_size:
            qr_image_pil = qr_image_pil.resize((max_size, max_size), Image.Resampling.LANCZOS)

        # Converte a imagem PIL para um formato que o Tkinter pode usar
        qr_photo_tk = ImageTk.PhotoImage(qr_image_pil)
        
        # Exibe a imagem no rótulo de pré-visualização
        label_preview.config(image=qr_photo_tk)
        label_preview.image = qr_photo_tk # Mantém a referência para evitar garbage collection
        label_preview.pack(pady=10) # Garante que o rótulo é visível
        
        messagebox.showinfo("Sucesso", "QR Code gerado com sucesso!")
        
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro ao gerar o QR Code: {e}")

def salvar_qr_code():
    """Salva a imagem do QR Code em um arquivo."""
    global qr_image_pil

    if qr_image_pil is None:
        messagebox.showwarning("Aviso", "Nenhum QR Code gerado para salvar.")
        return

    # Abre a caixa de diálogo para salvar o arquivo
    file_path = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG files", "*.png"), ("All files", "*.*")],
        title="Salvar QR Code como..."
    )

    if file_path:
        try:
            qr_image_pil.save(file_path)
            messagebox.showinfo("Sucesso", f"QR Code salvo em: {file_path}")
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro ao salvar o arquivo: {e}")

# Configurações da janela principal
root = tk.Tk()
root.title("Gerador de QR Code Leve")
root.geometry("500x700")
root.resizable(False, False)

# Cores e fontes para uma interface agradável
root.configure(bg="#f0f0f0")
fonte_label = ("Arial", 12, "bold")
fonte_btn = ("Arial", 10, "bold")

# Criação de widgets
frame_principal = tk.Frame(root, bg="#f0f0f0", padx=20, pady=20)
frame_principal.pack(expand=True, fill="both")

# Título
label_titulo = tk.Label(frame_principal, text="Gerador de QR Code", font=("Arial", 18, "bold"), bg="#f0f0f0")
label_titulo.pack(pady=(0, 20))

# Campo de texto
label_texto = tk.Label(frame_principal, text="Digite o texto ou URL:", font=fonte_label, bg="#f0f0f0")
label_texto.pack(anchor="w")
entry_texto = tk.Entry(frame_principal, width=50, font=("Arial", 10), bd=2, relief="groove")
entry_texto.pack(pady=(5, 10))

# Opções de personalização
frame_opcoes = tk.Frame(frame_principal, bg="#f0f0f0")
frame_opcoes.pack(pady=10)

# Opção de Cor de Preenchimento
label_cor = tk.Label(frame_opcoes, text="Cor do QR Code:", font=fonte_label, bg="#f0f0f0")
label_cor.pack(side="left", padx=(0, 5))
cores = ["black", "blue", "red", "green", "purple"]
var_cor = tk.StringVar(root)
var_cor.set(cores[0]) # Valor padrão
menu_cor = tk.OptionMenu(frame_opcoes, var_cor, *cores)
menu_cor.config(font=("Arial", 9), relief="flat")
menu_cor.pack(side="left")

# Opção de Cor de Fundo
label_fundo = tk.Label(frame_opcoes, text="Cor de Fundo:", font=fonte_label, bg="#f0f0f0")
label_fundo.pack(side="left", padx=(15, 5))
fundos = ["white", "yellow", "cyan", "lightgray"]
var_fundo = tk.StringVar(root)
var_fundo.set(fundos[0]) # Valor padrão
menu_fundo = tk.OptionMenu(frame_opcoes, var_fundo, *fundos)
menu_fundo.config(font=("Arial", 9), relief="flat")
menu_fundo.pack(side="left")

# Opção de Tamanho
label_tamanho = tk.Label(frame_opcoes, text="Tamanho:", font=fonte_label, bg="#f0f0f0")
label_tamanho.pack(side="left", padx=(15, 5))
tamanhos = ["5", "10", "15", "20"]
var_tamanho = tk.StringVar(root)
var_tamanho.set(tamanhos[1]) # Valor padrão
menu_tamanho = tk.OptionMenu(frame_opcoes, var_tamanho, *tamanhos)
menu_tamanho.config(font=("Arial", 9), relief="flat")
menu_tamanho.pack(side="left")


# Botões
frame_botoes = tk.Frame(frame_principal, bg="#f0f0f0")
frame_botoes.pack(pady=10)

btn_gerar = tk.Button(frame_botoes, text="Gerar QR Code", command=gerar_qr_code, bg="#4CAF50", fg="white", font=fonte_btn, bd=0, relief="raised", padx=15, pady=8)
btn_gerar.pack(side="left", padx=5)

btn_salvar = tk.Button(frame_botoes, text="Salvar QR Code", command=salvar_qr_code, bg="#008CBA", fg="white", font=fonte_btn, bd=0, relief="raised", padx=15, pady=8)
btn_salvar.pack(side="left", padx=5)

# Pré-visualização do QR Code
label_preview = tk.Label(frame_principal, bg="#f0f0f0")
label_preview.pack(pady=20)
# Placeholder
placeholder_image = Image.new('RGB', (200, 200), 'white')
placeholder_tk = ImageTk.PhotoImage(placeholder_image)
label_preview.config(image=placeholder_tk)

# Inicia o loop principal da aplicação
root.mainloop()
