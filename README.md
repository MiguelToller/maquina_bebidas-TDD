# 🥤 Máquina de Bebidas - TDD

[![Python Version](https://img.shields.io/badge/python-3.11%2B-blue.svg)](https://www.python.org/downloads/)
[![TDD](https://img.shields.io/badge/metodologia-TDD-green.svg)](https://en.wikipedia.org/wiki/Test-driven_development)

Este projeto simula o núcleo lógico de uma máquina de bebidas automática.  
O objetivo principal é exercitar o **Desenvolvimento Orientado a Testes (TDD)**.

---

## 🐍 O que é `venv` (ambiente virtual)?

O **venv** é uma ferramenta do Python usada para criar **ambientes virtuais isolados**.

Ele cria uma pasta dentro do projeto contendo:

- Uma cópia do executável do Python  
- Um espaço próprio para instalar bibliotecas  

### ✅ Objetivo principal

Isolar dependências de cada projeto, evitando conflitos entre versões de bibliotecas ou do Python.

---

## 🚀 Vantagens do `venv`

### 🔒 1. Evitar conflitos de dependências
Cada projeto possui suas próprias bibliotecas e versões.

> Exemplo: este projeto utiliza `StrEnum` (Python 3.11+), garantindo compatibilidade.

---

### 📦 2. Facilidade para o time (`requirements.txt`)

Permite compartilhar exatamente as dependências necessárias.

#### 📌 Gerar arquivo de dependências
```bash
pip freeze > requirements.txt
```

#### 📌 Instalar dependências
```bash
pip install -r requirements.txt
```

---

### 🔑 3. Sem necessidade de permissões administrativas

- Não precisa usar `sudo` ou "Executar como administrador"
- As bibliotecas são instaladas localmente no projeto

---

## ⚙️ Comandos básicos do `venv`

### ▶️ Criar ambiente virtual
```bash
python -m venv .venv
```

### ▶️ Ativar ambiente

#### Windows
```bash
.\.venv\Scripts\activate
```

#### Linux / Mac
```bash
source .venv/bin/activate
```

✅ Após ativar, você verá `(.venv)` no terminal → ambiente ativo.

---

## 🧪 TDD — Test-Driven Development

### 🔁 1. Conceito (Ciclo Red-Green-Refactor)

O TDD é uma abordagem onde você:

> Primeiro escreve o teste → depois o código

#### 🔴 RED (Falha)
Criar um teste para uma funcionalidade inexistente.

- Exemplo: validar se a bebida está cadastrada  
- O teste deve falhar  

---

#### 🟢 GREEN (Passa)
Implementar o mínimo necessário para o teste passar.

- Foco: funcionalidade, não perfeição  

---

#### 🔵 REFACTOR (Melhoria)
Melhorar o código sem quebrar os testes.

- Exemplo: substituir mensagens de erro por `Enum`  
- Ajustar arquitetura e organização  

---

## 💡 Por que usar TDD?

### ✔️ Benefícios principais

#### 🧩 Melhor design de código
Código mais modular, desacoplado e seguro.

#### 📖 Documentação viva
Os testes (`test_bebidas.py`) mostram exatamente como o sistema funciona.

#### 🛡️ Segurança para mudanças
Permite refatorar com confiança, evitando regressões.

---

## 📌 Regras de Negócio Implementadas

- ✅ **Validação de Catálogo**  
  Apenas bebidas pré-aprovadas (`Coca-Cola`, `Sprite`, `Guaraná`, `Água`)

- ✅ **Controle de Saldo**  
  Impede retiradas acima do estoque disponível

- ✅ **Integridade Numérica**  
  Bloqueia valores negativos ou zero

- ✅ **Proteção de Dados**  
  Uso de encapsulamento com `@property` e `.copy()`

---

## 🚀 Como Executar os Testes

Com o ambiente virtual ativo:

```bash
python -m unittest
```

---

## 📂 Estrutura do Projeto

```
maquina_bebidas-TDD/
├── maquina_bebidas.py   # Lógica e regras de negócio
├── mensagens_erro.py    # Padronização de erros (StrEnum)
└── test_bebidas.py      # Testes unitários
```

---
