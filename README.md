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
9. [Deploy](#deploy)
10. [Considerações Finais](#consideracoes-finais)

---

## 1. Introdução <a name="introducao"></a>

Este projeto é o backend da aplicação **Desafio Clarke Energia**, desenvolvido em Django, que fornece uma API REST para gerenciar fornecedores de energia e realizar filtros com base no consumo energético do cliente.

## 2. Requisitos <a name="requisitos"></a>

- Python 3.8 ou superior
- Django 3.x ou superior
- PostgreSQL (ou outro banco de dados compatível)
- [Pip](https://pip.pypa.io/en/stable/) para gerenciar pacotes Python

## 3. Instalação e Configuração <a name="instalacao-e-configuracao"></a>

### Passo 1: Clonar o Repositório

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
