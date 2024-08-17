# Documentação do Backend - Desafio Clarke Energia

## Índice

1. [Introdução](#introducao)
2. [Requisitos](#requisitos)
3. [Instalação e Configuração](#instalacao-e-configuracao)
4. [Variáveis de Ambiente](#variaveis-de-ambiente)
5. [Comandos Principais](#comandos-principais)
6. [Estrutura de URLs](#estrutura-de-urls)
7. [Endpoints Disponíveis](#endpoints-disponiveis)
    - [Criar Fornecedor](#criar-fornecedor)
    - [Filtrar Fornecedores](#filtrar-fornecedores)
8. [Testes](#testes)
9. [Considerações Finais](#consideracoes-finais)

---

## 1. Introdução <a name="introducao"></a>

Este projeto é o backend da aplicação **Desafio Clarke Energia**, desenvolvido em Django, que fornece uma API para gerenciar fornecedores de energia e realizar filtros com base no consumo do cliente.

## 2. Requisitos <a name="requisitos"></a>

- Python 3.11 ou superior
- Django 5.1 ou superior
- PostgreSQL (ou outro banco de dados compatível)
- [Pip](https://pip.pypa.io/en/stable/) para gerenciar pacotes Python

## 3. Instalação e Configuração <a name="instalacao-e-configuracao"></a>

### Passo 1: Clonar o Repositório

```bash
git clone https://github.com/willianvmelo/clarke-energia-backend.git
cd clarke-energia-backend
```

### Passo 2: Criar e Ativar um Ambiente Virtual

```
python3 -m venv venv
source venv/bin/activate  
# No Windows:
venv\Scripts\activate
```

### Passo 3: Instalar as Dependências

```
pip install -r requirements.txt
```

### Passo 4: Configurar as Variáveis de Ambiente

Crie um arquivo .env na raiz do projeto com as seguintes variáveis:
```
SECRET_KEY=your_secret_key
DEBUG=True
DATABASE_URL=postgres://user:password@localhost:5432/your_db_name
ALLOWED_HOSTS=localhost,127.0.0.1
```

### Passo 5: Executar Migrações

```
python3 manage.py migrate
```

### Passo 6: Executar Servidor de Desenvolvimento

```
python3 manage.py runserver
```

### Usando Docker

- Crie um arquivo .env como mostrado no passo 4. 
- Construa e inicie o projeto com:
```
docker-compose up --build
```
- Uma vez que os containers estejam em execução, você pode acessar o projeto em http://localhost:8000.

## 4. Variáveis de Ambiente <a name="variaveis-de-ambiente"></a>

- SECRET_KEY: Chave secreta do Django.
- DEBUG: Ativa ou desativa o modo de depuração.
- DATABASE_URL: URL de conexão ao banco de dados.
- ALLOWED_HOSTS: Lista de hosts permitidos para servir a aplicação.

## 5. Comandos Principais <a name="comandos-principais"></a>

- python3 manage.py runserver: Inicia o servidor de desenvolvimento.
- python3 manage.py migrate: Aplica as migrações do banco de dados.
- python3 manage.py createsuperuser: Cria um usuário administrador.

## 6. Estrutura de URLs <a name="estrutura-de-urls"></a>

- /suppliers/create/: Endpoint para criar novos fornecedores.
- /suppliers/filter/: Endpoint para filtrar fornecedores com base no consumo.

## 7. Endpoints Disponíveis <a name="endpoints-disponiveis"></a>

### Criar Fornecedor <a name="criar-fornecedor"></a>

URL: api/suppliers/create/

Método: POST

Descrição: Cria um novo fornecedor com os dados fornecidos.

Parâmetros:

```
{
  "name": "Fornecedor Exemplo",
  "logo": "http://example.com/logo.png",
  "state": "São Paulo",
  "cost_per_kwh": 0.45,
  "min_kwh_limit": 30000,
  "total_clients": 150,
  "average_rating": 4.5
}
```

Resposta de Sucesso:
```
{
  "id": 1,
  "name": "Fornecedor Exemplo",
  "logo": "http://example.com/logo.png",
  "state": "São Paulo",
  "cost_per_kwh": 0.45,
  "min_kwh_limit": 30000,
  "total_clients": 150,
  "average_rating": 4.5
}
```
Resposta de Erro: Código HTTP com os detalhes do erro.

### Filtrar Fornecedores <a name="filtrar-fornecedores"></a>

URL: api/suppliers/filter/

Método: POST

Descrição: Filtra fornecedores com base no consumo mensal de energia informado.

Parâmetros:

```
{
  "consumption": 35000
}
```

Resposta de Sucesso:

```
[
  {
    "id": 2,
    "name": "Fornecedor B",
    "logo": "http://example.com/logo_b.png",
    "state": "Bahia",
    "cost_per_kwh": 0.40,
    "min_kwh_limit": 30000,
    "total_clients": 200,
    "average_rating": 4.8
  }
]
```

Resposta de Erro: Código HTTP 404 se nenhum fornecedor for encontrado ou 400 se o consumo não for informado.

## 8. Testes <a name="testes"></a>

Para executar os testes automatizados:

```
python3 manage.py test
```

## 9. Considerações Finais <a name="consideracoes-finais"></a>

Essa documentação fornece uma visão geral. Para maiores detalhes sobre funcionalidades específicas, consulte o código-fonte e entre em contato.