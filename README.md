# Jogo da Velha em Python/Django

Este aplicativo faz uso do framework web Django e utiliza Bootstrap 5 para estilização.

## Pré-requisitos

Certifique-se de ter o Python e o Django instalados em sua máquina antes de prosseguir.

- Python: [Download Python](https://www.python.org/downloads/)
- Django: `pip install django`

## Instalação

1. Clone este repositório para o seu ambiente local.

   ```bash
   git clone https://github.com/seu-usuario/seu-aplicativo.git

2. Navegue até o diretório.
 
    ```bash
    cd seu-aplicativo

3. Instale as dependências.

   ```bash
   pip install -r requirements.txt

4. Execute as migrações.
 
    ```bash
    python manage.py migrate


## Uso

1. Clone este repositório para o seu ambiente local.

   ```bash
   python manage.py runserver


## CSS

Este aplicativo utiliza o Bootstrap 5 para estilização. Certifique-se de incluir os CDNs do Bootstrap 5 em seus modelos para garantir o funcionamento correto dos estilos.

    ```html
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0/dist/css/bootstrap.min.css" integrity="...">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0/dist/js/bootstrap.bundle.min.js" integrity="..." defer></script>
