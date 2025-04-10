# Diário Online com Django

Aplicação web desenvolvida com Django durante a **Pystack Week Returnal**, que permite o registro de dias vividos pelo usuário com dados ricos e organizados.

---

## Funcionalidades

- Registro de entradas no diário com:
  - Título do dia
  - Descrição do que aconteceu
  - Nome de uma pessoa que estava presente
  - Upload de uma foto dessa pessoa
  - Tag para classificação (ex: #família, #trabalho, etc)
- Listagem de registros
- Visualização individual dos registros

---

## Tecnologias usadas

- Python 3.10+
- Django 4.x
- SQLite (padrão do Django)

---

## Como rodar localmente

1. Clone o repositório:
  ```bash
  git clone https://github.com/juauviitor02/Projetos-PWR.git
  cd Projetos-PWR/Projeto%202%20-%20Diário%20Online
  ```

2. Crie e ative o ambiente virtual:
  - No Linux:
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```
  - No Windows:
    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

3. Instale as dependências:
  ```bash
  pip install -r requirements.txt
  ```

4. Aplique as migrações do banco de dados:
  ```bash
  python manage.py migrate
  ```

5. Inicie o servidor de desenvolvimento:
  ```bash
  python manage.py runserver
  ```
