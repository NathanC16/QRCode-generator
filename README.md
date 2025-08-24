# Gerador de QR Code Responsivo

![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![Tkinter](https://img.shields.io/badge/UI-Tkinter-orange.svg)
![Licença](https://img.shields.io/badge/License-GPLv3-blue.svg)

Uma aplicação de desktop leve e amigável para gerar e salvar QR Codes personalizados, desenvolvida em Python com a interface gráfica Tkinter. Esta versão possui uma interface totalmente responsiva, que se adapta ao tamanho da janela.

![Pré-visualização do Gerador de QR Code](https://i.imgur.com/link-para-sua-imagem.png)
*(Sugestão: tire um print da aplicação e hospede em um site como o [Imgur](https://imgur.com/) para colocar o link aqui)*

## ✨ Funcionalidades

* **Interface Totalmente Responsiva:** A janela, botões, campos de texto e fontes se ajustam de forma fluida ao redimensionamento.
* **Geração Instantânea:** Insira um texto ou URL e gere o QR Code com um clique.
* **Pré-visualização:** Veja o resultado do QR Code diretamente na aplicação antes de salvar, sem sobreposição de elementos.
* **Personalização:**
    * Escolha a **cor** do QR Code.
    * Selecione a **cor de fundo**.
    * Ajuste o **tamanho** (resolução) do QR Code de forma interativa.
* **Salvar em PNG:** Exporte o QR Code gerado como um arquivo de imagem `.png`.

## 🛡️ Licença de Código Aberto (GNU GPLv3)

Este projeto está licenciado sob a **GNU General Public License v3.0**.

Isso significa que o código é livre para uso, estudo, compartilhamento e modificação. No entanto, qualquer trabalho derivado ou modificado que você distribuir também deve ser licenciado sob os termos da GPL. O objetivo é garantir que o software e seus derivados permaneçam livres para todos. Para mais detalhes, consulte o arquivo [LICENSE](LICENSE) no repositório.

## 🚀 Como Executar o Projeto

Para rodar este projeto, você precisa ter o Python 3 instalado em sua máquina.

**1. Clone o repositório:**

```bash
git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/seu-usuario/seu-repositorio.git)
cd seu-repositorio
```

**2. Verifique a Instalação do Tkinter:**

O Tkinter é uma biblioteca padrão do Python, mas pode exigir a instalação de pacotes adicionais em alguns sistemas operacionais, especialmente no Linux.

* **No Linux (Debian/Ubuntu):**
  ```bash
  sudo apt-get update
  sudo apt-get install python3-tk
  ```
* **No Linux (Fedora/CentOS/RHEL):**
  ```bash
  sudo dnf install python3-tkinter
  ```
* **No Windows e macOS:** Geralmente já vem instalado com o Python.

**3. Crie um ambiente virtual (recomendado):**

```bash
python3 -m venv venv
```

* No Windows, ative com:
    ```bash
    .\venv\Scripts\activate
    ```
* No Linux/macOS, ative com:
    ```bash
    source venv/bin/activate
    ```

**4. Instale as dependências:**

Todas as bibliotecas necessárias estão listadas no arquivo `requirements.txt`. Instale-as com o seguinte comando:

```bash
pip install -r requirements.txt
```

**5. Execute a aplicação:**

```bash
python3 qr_coder.py
```

## 🛠️ Tecnologias Utilizadas

* **[Python](https://www.python.org/)** - A linguagem de programação principal.
* **[Tkinter](https://docs.python.org/3/library/tkinter.html)** - Biblioteca padrão do Python para a criação da interface gráfica.
* **[qrcode](https://pypi.org/project/qrcode/)** - Biblioteca para a geração dos QR Codes.
* **[Pillow (PIL Fork)](https://pypi.org/project/Pillow/)** - Utilizada para manipular e exibir as imagens na interface.
