# Pystack Week Returnal - Projetos em Python e Django

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-4.x-green.svg)](https://www.djangoproject.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Este repositório reúne os projetos desenvolvidos durante a **Pystack Week Returnal**, um evento online promovido pela equipe **Pythonando**, com foco no desenvolvimento de aplicações web utilizando **Python** e **Django**.

---

##  Projetos incluídos

### 1. Gerenciador de Assinaturas (Python puro)
Um sistema simples de linha de comando onde o usuário pode:
- Cadastrar assinaturas pagas
- Consultar as assinaturas existentes
- Marcar uma assinatura como paga ou não paga
- Remover assinaturas
- Listar todas as informações salvas

### 2. Diário Online (Python + Django)
Uma aplicação web onde o usuário pode registrar o seu dia com:
- Título
- Descrição
- Nome e foto de uma pessoa presente
- Uma tag associada à entrada

### 3. Encurtador de Links (Django REST API)
Uma API RESTful que permite:
- Adicionar um link original com token personalizado
- Definir número de cliques únicos e tempo de expiração
- Gerar um link de redirecionamento e QRCode
- Acessar estatísticas de cliques

**Observação:** A função `update_link`, responsável por atualizar os dados do link, está retornando erro `405 Method Not Allowed`. O problema ainda não foi resolvido e está aberto a contribuições.

---

## Como rodar os projetos

Cada pasta contém seu próprio `README.md` com instruções detalhadas de instalação e uso. Recomendado usar ambientes virtuais separados para cada um.

---

## Contribuições

Fique à vontade para sugerir melhorias, corrigir bugs ou apenas explorar os códigos!

---

## Licença

Este repositório está licenciado sob os termos da licença MIT.
