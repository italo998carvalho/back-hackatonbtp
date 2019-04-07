# HACKATON BTP

## API da equipe OnTarget
Solução da equipe OnTarget desenvolvido em Python utilizando o microframework Flask
___
## Configuração
#### Dependências
É necessário ter instalado o interpretador da linguagem [Python](https://www.python.org/downloads/) e um banco de dados relacional (preferencialmente PostgreSQL). Caso sua máquina seja um MacOS ou alguma distro de Linux, provavelmente já terá o Python instalado.

#### Execução
1. Clone este repositorio e acesse a pasta raíz via terminal
2. Crie um ambiente virtual para isolar as dependências (comando Linux: python3 -m venv venv)
3. Execute o ambiente virtual (comando Linux: source venv/bin/activate)
4. Instale as dependências (Comando Linux: pip install -r requirements.txt)
5. Altere a string de conexão do banco em /BTPIntegra/app.py, [neste link](http://flask-sqlalchemy.pocoo.org/2.3/config/) é possível encontrar um exemplo de string de conexão da ORM utilizada neste trabalho (que foi a SQLAlchemy) para diversos bancos relacionais.
6. Execute a aplicação (comando Linux: python3 run.py)

___
## Rotas

#### Autenticação

###### /login - POST
###### Login do usuário 
```bash
{
	"registro": "123456", 
	"senha": "123"
}
```

#### Usuário
###### /usuario - POST
###### Cadastro do usuário
```bash
{
	"nome": "Nome Do Usuário", 
	"registro": "123456", 
	"senha": "123", 
	"funcao": "Desenvolvedor", 
	"categoria": "ti", 
	"dataNascimento": "2019-04-05", 
	"sexo": "M", 
	"fotoPerfil": "base64poklçoonoioimoifw"
}
```

###### /usuario - GET
###### Retorna todos os usuários
```bash
{
    "body": [
        {
            "categoria": "ti",
            "dataNascimento": "Thu, 17 Dec 1998 00:00:00 GMT",
            "fotoPerfil": "base64poklçoonoioimoifw",
            "funcao": "Desenvolvedor",
            "id": 1,
            "nome": "Italo",
            "registro": 123456,
            "sexo": "M"
        }
    ],
    "code": 200
}
```

###### /usuario/<id> - GET
###### Retorna um usuário
```bash
{
    "body": {
        "categoria": "ti",
        "dataNascimento": "Thu, 17 Dec 1998 00:00:00 GMT",
        "fotoPerfil": "base64poklçoonoioimoifw",
        "funcao": "Desenvolvedor",
        "id": 1,
        "nome": "Italo",
        "registro": 123456,
        "sexo": "M"
    },
    "code": 200
}
```

#### Conteúdo

###### /conteudo - POST
###### Cadastra um conteúdo
```bash
{
    "titulo": "Como proceder em caso de queda de sistema", 
    "descricao": "Em caso de queda de energia, ...", 
    "categoria": "ti", 
    "arquivos": [
        "base64ajsdhlakhsdlkahlksdhalsdhjlak", 
        "base64qiuoweoiquwoeiquoewiqweqoui"
    ]
}
```

###### /conteudo - GET
###### Retorna um dicionario com todos os conteúdos
```bash
{
    "body": [
        {
            "arquivos": [
                {
                    "midia": "base64ajsdhlakhsdlkahlksdhalsdhjlak"
                }
            ],
            "avaliacaoMedia": 5,
            "descricao": "tira o velho e põe o novo",
            "id": 5,
            "idUsuario": 2,
            "numeroDeAvaliacoes": 1,
            "titulo": "como trocar um step"
        },
        {
            "arquivos": [
                {
                    "midia": "base64ajsdhlakhsdlkahlksdhalsdhjlak"
                },
                {
                    "midia": "base64qiuoweoiquwoeiquoewiqweqoui"
                }
            ],
            "avaliacaoMedia": null,
            "descricao": "Em caso de queda de energia, ...",
            "id": 6,
            "idUsuario": 1,
            "numeroDeAvaliacoes": 0,
            "titulo": "Como proceder em caso de queda de sistema"
        }
    ],
    "code": 200
}
```

###### /conteudo/<id> - GET
###### Retorna um dicionario de um conteúdo específico
```bash
{
    "body": {
        "arquivos": [
            {
                "midia": "base64ajsdhlakhsdlkahlksdhalsdhjlak"
            }
        ],
        "avaliacaoMedia": 5,
        "descricao": "tira o velho e põe o novo",
        "idUsuario": 2,
        "numeroDeAvaliacoes": 1,
        "titulo": "como trocar um step"
    },
    "code": 200
}
```

###### /conteudo/<id>/visto - POST
###### Confirma o consumo de um conteúdo
```bash
{
    "nota": 4.5
}
```

###### /conteudosConsumidos - GET
###### Retorna um dicionario com os conteúdos já consumidos pelo usuário
```bash
{
    "body": [
        {
            "arquivos": [
                {
                    "midia": "base64ajsdhlakhsdlkahlksdhalsdhjlak"
                }
            ],
            "descricao": "tira o velho e põe o novo",
            "id": 5,
            "titulo": "como trocar um step"
        }
    ],
    "code": 200
}
```