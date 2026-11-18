# Oliveira Conta

Landing page de um escritório fictício de contabilidade, voltado
a MEIs e pequenas empresas.

Projeto desenvolvido por Alann Oliveira para praticar desenvolvimento
web e compor seu portfólio. Não oferece serviços contábeis reais.

## Funcionalidades

- Apresentação dos serviços.
- Layout responsivo.
- Formulário de contato integrado ao Flask.
- Validação dos dados no servidor.
- Preservação dos campos após erros de validação.
- Armazenamento de contatos no SQLite.
- Mensagens de erro e sucesso.
- Redirecionamento após cadastro para evitar reenvio ao atualizar.

## Tecnologias

- HTML
- CSS
- JavaScript — utilizado na demonstração inicial do formulário
- Python
- Flask e Jinja
- SQLite
- email-validator
- Git e GitHub

## Como executar no Windows

É necessário ter Python e Git instalados.

### 1. Clonar o repositório

```powershell
git clone https://github.com/AlannCristian/oliveira-conta.git
cd oliveira-conta
```

### 2. Criar o ambiente virtual

```powershell
py -m venv .venv
```

### 3. Instalar as dependências

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

### 4. Preparar o banco

```powershell
.\.venv\Scripts\python.exe banco.py
```

### 5. Iniciar o servidor de desenvolvimento

```powershell
.\.venv\Scripts\python.exe -m flask --app app run
```

Acesse http://127.0.0.1:5000/ no navegador.

Para encerrar o servidor, pressione Ctrl + C no terminal.

## Organização do projeto

| Caminho                | Responsabilidade                                      |
| ---------------------- | ----------------------------------------------------- |
| `app.py`               | Rotas, validação e respostas da aplicação             |
| `banco.py`             | Criação da tabela e gravação dos contatos             |
| `templates/index.html` | Estrutura da página e templates Jinja                 |
| `static/style.css`     | Estilos e adaptação para diferentes telas             |
| `static/script.js`     | Arquivo da demonstração inicial; envio atual via HTML |
| `static/img/`          | Imagens e assinatura visual do desenvolvedor          |
| `requirements.txt`     | Dependências Python e suas versões                    |
| `.gitignore`           | Arquivos que não devem ser versionados                |

## Dados de demonstração

Use somente dados fictícios nos testes.

O arquivo `contatos.db` é criado localmente e não é enviado ao GitHub.
Para preservar seus registros, é necessário um backup separado do banco.

## Estado do projeto

Primeira versão funcional para execução local.

A publicação ainda depende de preparação para produção, incluindo
tratamento de falhas de gravação e proteção do formulário.

## Aprendizados

- Estruturação de páginas com HTML semântico.
- Estilização com CSS, Flexbox e Grid.
- Integração entre formulário HTML e Python.
- Uso dos métodos HTTP GET e POST.
- Validação de dados no navegador e no servidor.
- Consultas SQL parametrizadas.
- Fluxo POST → redirecionamento → GET.
- Versionamento com Git e envio ao GitHub.

## Autor

Alann Oliveira — AO Dev

https://github.com/AlannCristian
