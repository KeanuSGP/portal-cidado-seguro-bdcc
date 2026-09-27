# 🛡️ Portal Cidadão Seguro — API

API REST desenvolvida para o **Portal Cidadão Seguro**, projeto acadêmico da disciplina de Banco de Dados e Cloud Computing.

O sistema tem como objetivo disponibilizar uma API para gerenciamento de **usuários, categorias e solicitações de zeladoria urbana**, permitindo que cidadãos registrem problemas encontrados na cidade e acompanhem suas solicitações.

Link: <a href="http://portalcidadaoseguro-env.eba-crnmfmse.us-east-1.elasticbeanstalk.com/api/">Portal Cidadão Seguro API</a>

---

## 📋 Sumário

* [Sobre o projeto](#-sobre-o-projeto)
* [Tecnologias utilizadas](#-tecnologias-utilizadas)
* [Estrutura do projeto](#-estrutura-do-projeto)
* [Pré-requisitos](#-pré-requisitos)
* [Execução local](#-execução-local)
* [Banco de dados](#-banco-de-dados)
* [Principais funcionalidades](#-principais-funcionalidades)
* [Endpoints](#-endpoints)
* [Alterações e implementação](#-alterações-e-implementação)
* [Deploy na AWS](#-deploy-na-aws)
* [Processo de deploy](#-processo-de-deploy)
* [Validação após o deploy](#-validação-após-o-deploy)
* [Considerações](#-considerações)

---

# 📌 Sobre o projeto

O **Portal Cidadão Seguro** é uma aplicação voltada para a comunicação entre cidadãos e o poder público.

A API disponibiliza recursos para:

* gerenciamento de usuários;
* cadastro e gerenciamento de categorias;
* criação de solicitações de zeladoria urbana;
* consulta das solicitações cadastradas;
* atualização do status das solicitações;
* associação de solicitações aos usuários;
* envio de imagens relacionadas às solicitações.

A aplicação foi desenvolvida utilizando **Django** e **Django REST Framework**, seguindo o padrão de APIs REST.

---

# 🛠️ Tecnologias utilizadas

| Tecnologia                   | Utilização                  |
| ---------------------------- | --------------------------- |
| Python 3.12                  | Linguagem de programação    |
| Django 6.1.1                 | Framework web               |
| Django REST Framework 3.18.1 | Desenvolvimento da API REST |
| SQLite                       | Banco de dados              |
| Pillow                       | Processamento de imagens    |
| Git/GitHub                   | Versionamento do código     |
| AWS Elastic Beanstalk        | Deploy da aplicação         |

As dependências utilizadas pelo projeto estão registradas no arquivo `requirements.txt`.

---

# 📁 Estrutura do projeto

A estrutura principal da aplicação é organizada da seguinte maneira:

```text
portal-cidado-seguro-bdcc/
│
├── .ebextensions/
│   └── configurações do Elastic Beanstalk
│
├── .elasticbeanstalk/
│   └── config.yml
│
├── media/
│   └── solicitacoes/
│
├── portal_cidadao_seguro/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── ...
│
├── user/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── ...
│
├── zeladoria/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── ...
│
├── db.sqlite3
├── manage.py
├── requirements.txt
├── app.zip
└── README.md
```

O arquivo `manage.py` utiliza `portal_cidadao_seguro.settings` como configuração principal do projeto Django.

---

# 💻 Pré-requisitos

Para executar a API localmente, é necessário possuir:

* **Python 3.12 ou superior**
* **pip**
* **Git**

Recomenda-se também utilizar um ambiente virtual Python para evitar conflitos entre as dependências do projeto e outras instalações existentes na máquina.

---

# 🚀 Execução local

## 1. Clonar o repositório

```bash
git clone https://github.com/KeanuSGP/portal-cidado-seguro-bdcc.git
```

Entrar no diretório:

```bash
cd portal-cidado-seguro-bdcc
```

---

## 2. Criar o ambiente virtual

### Windows

```bash
python -m venv venv
```

Ativar:

```bash
venv\Scripts\activate
```

### Linux/macOS

```bash
python3 -m venv venv
```

Ativar:

```bash
source venv/bin/activate
```

Após a ativação, o terminal deverá indicar que o ambiente virtual está ativo.

---

## 3. Instalar as dependências

Com o ambiente virtual ativado:

```bash
pip install -r requirements.txt
```

As principais dependências são:

```text
Django==6.1.1
djangorestframework==3.18.1
pillow==12.3.0
```

---

## 4. Aplicar as migrações

Execute:

```bash
python manage.py migrate
```

Esse comando cria/aplica as estruturas necessárias no banco de dados SQLite.

O projeto atualmente utiliza o arquivo:

```text
db.sqlite3
```

como banco de dados padrão.

---

## 5. Criar um usuário administrador

Para acessar o painel administrativo do Django:

```bash
python manage.py createsuperuser
```

Informe:

```text
Username:
Email:
Password:
```

O usuário criado poderá acessar:

```text
http://127.0.0.1:8000/admin/
```

---

## 6. Executar a aplicação

Execute:

```bash
python manage.py runserver
```

A API ficará disponível em:

```text
http://127.0.0.1:8000/
```

A raiz da aplicação redireciona para:

```text
/api/
```

conforme definido no roteamento principal do projeto.

---

# 🗄️ Banco de dados

Durante o desenvolvimento local, a aplicação utiliza **SQLite**.

A configuração está definida em:

```text
portal_cidadao_seguro/settings.py
```

Atualmente:

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
```

O banco pode ser atualizado utilizando as ferramentas de migração do Django:

```bash
python manage.py makemigrations
python manage.py migrate
```

---

# 🧩 Principais funcionalidades

## 👤 Usuários

O módulo `user` é responsável pelo gerenciamento dos usuários da aplicação.

A API utiliza um `UserViewSet`, baseado em `ModelViewSet`, permitindo operações de criação, consulta, atualização e exclusão dos usuários.

---

## 🏙️ Categorias

As categorias representam os tipos de problemas que podem ser registrados pelos cidadãos.

Exemplos:

```text
Iluminação pública
Buracos
Limpeza urbana
Sinalização
Áreas públicas
```

A entidade `Categoria` possui:

```text
id
nome
descricao
```

---

## 📝 Solicitações

O módulo `zeladoria` contém as solicitações realizadas pelos cidadãos.

Uma solicitação possui:

```text
id
titulo
descricao
data_criacao
status
imagem
categoria
usuario
```

O status possui as seguintes opções:

```text
pendente
em andamento
concluída
```

As solicitações também podem possuir uma imagem associada, armazenada no diretório:

```text
media/solicitacoes/
```

---

# 🔌 Endpoints

A aplicação disponibiliza suas rotas através do prefixo:

```text
/api/
```

O roteamento principal da aplicação inclui as URLs da API através de:

```python
path("api/", include("portal_cidadao_seguro.api.urls"))
```

Os recursos principais da API são:

| Recurso      | Operações                             |
| ------------ | ------------------------------------- |
| Usuários     | Criar, consultar, atualizar e excluir |
| Categorias   | Criar, consultar, atualizar e excluir |
| Solicitações | Criar, consultar, atualizar e excluir |

Os `ViewSets` utilizados pelo projeto são baseados no `ModelViewSet` do Django REST Framework.

---

# 🔨 Alterações e implementação

A implementação do projeto foi realizada seguindo as etapas abaixo.

## 1. Criação do projeto Django

Inicialmente foi criado o projeto utilizando Django:

```text
portal_cidadao_seguro
```

O projeto possui sua configuração centralizada em:

```text
portal_cidadao_seguro/settings.py
```

e seu roteamento principal em:

```text
portal_cidadao_seguro/urls.py
```

---

## 2. Configuração do Django REST Framework

O Django REST Framework foi adicionado às aplicações instaladas:

```python
INSTALLED_APPS = [
    ...
    "rest_framework",
    "user",
    "zeladoria",
]
```

Isso possibilitou a implementação dos endpoints utilizando `ViewSets` e serializers.

---

## 3. Implementação do módulo de usuários

Foi criado o aplicativo:

```text
user/
```

responsável pelo gerenciamento dos usuários.

Foi implementado um `UserViewSet`, permitindo utilizar os métodos HTTP convencionais da API REST para manipulação dos registros.

---

## 4. Implementação do módulo de zeladoria

Foi criado o aplicativo:

```text
zeladoria/
```

responsável pelas funcionalidades relacionadas às solicitações de zeladoria urbana.

Foram criados os modelos:

```text
Solicitacao
Categoria
```

A entidade `Solicitacao` possui relacionamentos com `Categoria` e `User`, além do campo destinado ao armazenamento de imagens.

---

## 5. Implementação dos ViewSets

Foram implementados `ModelViewSet` para os recursos da aplicação.

Exemplo:

```python
class SolicitacaoViewSet(ModelViewSet):
    queryset = Solicitacao.objects.all()
    serializer_class = SolicitacaoSerializer
```

e:

```python
class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
```

Essa abordagem disponibiliza automaticamente operações como:

```text
GET
POST
PUT
PATCH
DELETE
```

para os recursos configurados.

---

## 6. Configuração de arquivos de mídia

A aplicação foi configurada para trabalhar com arquivos enviados nas solicitações.

As configurações utilizadas são:

```python
MEDIA_ROOT = BASE_DIR / "media"
MEDIA_URL = "/media/"
```

As imagens das solicitações são armazenadas em:

```text
media/solicitacoes/
```

---

# ☁️ Deploy na AWS

O projeto foi preparado para execução utilizando o **AWS Elastic Beanstalk**.

A configuração do Elastic Beanstalk está presente no diretório:

```text
.elasticbeanstalk/
```

e o arquivo:

```text
.elasticbeanstalk/config.yml
```

define:

```yaml
application_name: portal_cidadao_seguro
default_platform: Python 3.12
default_region: us-east-1
deploy:
  artifact: app.zip
```

Portanto, o processo de deploy utiliza um pacote da aplicação chamado:

```text
app.zip
```

---

# 📦 Processo de deploy

## 1. Preparação da aplicação

Antes do deploy, foram verificadas as dependências necessárias para execução da aplicação.

Elas estão centralizadas no arquivo:

```text
requirements.txt
```

O Elastic Beanstalk utiliza essas dependências para preparar o ambiente Python da aplicação.

---

## 2. Configuração do Elastic Beanstalk

O ambiente do Elastic Beanstalk foi configurado utilizando:

```text
Python 3.12
```

e a região:

```text
us-east-1
```

A configuração é mantida no arquivo:

```text
.elasticbeanstalk/config.yml
```

---

## 3. Geração do pacote de deploy

A aplicação é empacotada no arquivo:

```text
app.zip
```

Esse arquivo contém os arquivos necessários para execução da aplicação no ambiente da AWS.

O Elastic Beanstalk está configurado para utilizar esse arquivo como artefato de deploy:

```yaml
deploy:
  artifact: app.zip
```

---

## 4. Envio da aplicação para o Elastic Beanstalk

Com o ambiente configurado, o artefato:

```text
app.zip
```

é enviado para o ambiente do Elastic Beanstalk.

O serviço então realiza o processo de provisionamento/atualização da aplicação utilizando a plataforma Python configurada.

---

## 5. Inicialização da aplicação

Após o deploy, o Elastic Beanstalk disponibiliza a aplicação através da URL fornecida pelo ambiente.

A aplicação Django utiliza o arquivo WSGI do projeto para inicializar o servidor:

```text
portal_cidadao_seguro/wsgi.py
```

---

# ✅ Validação após o deploy

Após a publicação, devem ser realizados testes para verificar se a API está funcionando corretamente.

### 1. Verificar a aplicação

Acessar a URL fornecida pelo Elastic Beanstalk:

```text
https://<URL-DO-AMBIENTE>/
```

A aplicação deverá redirecionar para:

```text
/api/
```

---

### 2. Testar os endpoints

Realizar requisições aos endpoints disponíveis utilizando ferramentas como:

* Postman;
* Insomnia;
* navegador, quando aplicável;
* ferramentas de linha de comando.

Exemplo:

```http
GET /api/
```

Também devem ser testadas operações de:

```text
GET
POST
PUT/PATCH
DELETE
```

para os recursos implementados.

---

### 3. Testar envio de imagens

Como as solicitações possuem suporte a imagens, deve ser realizado um teste de criação/atualização de uma solicitação contendo um arquivo.

A imagem deve ser processada pelo campo:

```text
imagem
```

e armazenada no diretório configurado para mídia.

---

# 🔄 Fluxo resumido de implementação e deploy

```text
┌─────────────────────┐
│ Desenvolvimento     │
│ local                │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Implementação        │
│ Django + DRF         │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Modelos              │
│ User / Categoria /   │
│ Solicitação          │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Testes locais        │
│ runserver + API      │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Geração              │
│ app.zip              │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ AWS Elastic          │
│ Beanstalk             │
│ Python 3.12          │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Validação da API     │
│ em produção          │
└─────────────────────┘
```

---

# ⚙️ Comandos principais

### Criar ambiente virtual

```bash
python -m venv venv
```

### Ativar ambiente — Windows

```bash
venv\Scripts\activate
```

### Instalar dependências

```bash
pip install -r requirements.txt
```

### Criar migrações

```bash
python manage.py makemigrations
```

### Aplicar migrações

```bash
python manage.py migrate
```

### Criar administrador

```bash
python manage.py createsuperuser
```

### Executar localmente

```bash
python manage.py runserver
```

---

# 📌 Considerações

O projeto atualmente utiliza **SQLite** como banco de dados padrão e está configurado com `DEBUG = True` e uma `SECRET_KEY` definida diretamente no arquivo de configurações. Essas configurações são adequadas para o contexto de desenvolvimento acadêmico, mas devem ser revistas antes de uma utilização em produção real.

Para uma implantação produtiva, recomenda-se posteriormente:

* utilizar variáveis de ambiente para informações sensíveis;
* desativar `DEBUG`;
* restringir `ALLOWED_HOSTS`;
* utilizar um banco de dados gerenciado;
* configurar adequadamente o armazenamento de arquivos de mídia;
* configurar HTTPS;
* revisar as permissões de acesso da aplicação;
* configurar mecanismos de monitoramento e logs.

---

## 👥 Projeto

**Portal Cidadão Seguro**

Repositório:

https://github.com/KeanuSGP/portal-cidado-seguro-bdcc

---
