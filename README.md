
# TechService - Diogo Dias

## Sistema de Gestão de Assistência Técnica

O **TechService** é um projeto didático em Python para a gestão de uma pequena empresa de assistência técnica.

A versão **V0** estabelece o modelo inicial que será usado como referência pelos alunos para criar novas tabelas, classes e operações CRUD.

## Objetivo da V0

Nesta versão são definidos:

- estrutura padrão do projeto;
- ligação Python → MySQL;
- classe `Cliente`;
- repositório com CRUD de clientes;
- padrão de controlo dos registos;
- preparação para Git/GitHub;
- execução no PyCharm e no VS Code.

## Estrutura

```text
TechService_V0/
├── main.py
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md
├── sql/
│   └── 001_criar_bd.sql
└── src/
    ├── database/
    │   └── conexao.py
    ├── models/
    │   └── cliente.py
    └── repositories/
        └── cliente_repository.py
```

## Modelo adotado

Cada entidade deverá possuir uma classe em `models` e um repositório em `repositories`.

```text
Cliente
├── models/cliente.py
└── repositories/cliente_repository.py
```

O CRUD segue quatro operações:

```text
inserir()
listar()
atualizar()
excluir()
```

`excluir()` realiza exclusão lógica. O registo permanece na base de dados.

## Padrão de controlo

As tabelas principais utilizam:

```text
status
created_at
updated_at
deleted_at
```

Regras:

```text
INSERT  → status = 1 e created_at automático
UPDATE  → updated_at = NOW()
DELETE  → status = 0 e deleted_at = NOW()
SELECT  → normalmente WHERE status = 1
```

## Preparação

### 1. Criar o ambiente virtual

```bat
python -m venv .venv
.venv\Scripts\activate
```

### 2. Instalar dependências

```bat
pip install -r requirements.txt
```

### 3. Criar a base de dados

Executar:

```text
sql/001_criar_bd.sql
```

Será criada:

```text
techservice_db
└── clientes
```

### 4. Configurar o MySQL

Copiar `.env.example` para `.env` e ajustar:

```text
DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASSWORD=
DB_NAME=techservice_db
```

O `.env` é local e não deve ser enviado ao GitHub.

### 5. Executar

```bat
python main.py
```

O programa insere um cliente diretamente no MySQL e lista os clientes ativos.

## Git e ambientes de desenvolvimento

O GitHub será o repositório central:

```text
PC principal / PyCharm
          ↕
        GitHub
       ↙      ↘
VM / VS Code   VM / PyCharm
```

Depois de clonar em outra máquina, não se copia `.venv` nem `.env`.

Em cada máquina:

```bat
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

Depois deve ser criado o `.env` local e executado o script SQL no MySQL local.

## Modelo para os alunos

`Cliente` é a entidade de referência.

Para uma nova entidade, repetir o padrão:

```text
models/
    nova_entidade.py

repositories/
    nova_entidade_repository.py
```

e implementar progressivamente:

```text
INSERT
SELECT
UPDATE
DELETE lógico
```

mantendo:

```text
status
created_at
updated_at
deleted_at
```
