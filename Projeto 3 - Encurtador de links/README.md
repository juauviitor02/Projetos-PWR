# Encurtador de Links - API com Django REST

API RESTful criada com **Python e Django**, durante a **Pystack Week Returnal**, com foco em manipulação de URLs e geração de estatísticas.

---

##  Funcionalidades

- Adicionar um link original com token
- Definir número de cliques únicos e tempo de expiração
- Obter link encurtado com redirecionamento
- Gerar QRCode do link
- Acessar estatísticas de cliques

---

## Erro conhecido

A função `update_link`, que deveria permitir a edição dos dados do link encurtado, está retornando o erro `405 Method Not Allowed`. Ainda não consegui resolver e deixei aberto para futuras contribuições.

---

##  Como executar

1. Clone o repositório:
    ```bash
    git clone https://github.com/juauviitor02/Projetos-PWR.git
    ```

2. Navegue até o diretório do projeto:
    ```bash
    cd Projetos-PWR/Projeto%203%20-%20Encurtador%20de%29links
    ```

3. Crie e ative o ambiente virtual:
    - Linux/MacOS:
      ```bash
      python -m venv venv
      source venv/bin/activate
      ```
    - Windows:
      ```bash
      python -m venv venv
      venv\Scripts\activate
      ```

4. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

5. Aplique as migrações do banco de dados:
    ```bash
    python manage.py migrate
    ```

6. Inicie o servidor de desenvolvimento:
    ```bash
    python manage.py runserver
    ```

