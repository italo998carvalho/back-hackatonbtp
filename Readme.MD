# HACKATON BTP

## API da equipe On Target

___
## Rotas

#### Autenticação

###### /login - POST
###### Login do usuário 
```bash
{
	"usuario": "usuario", 
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
	"funcao": "operador de RTG", 
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
            "id": 1,
            "nome": "Italo",
            "registro": 123456
        }
    ],
    "code": 200
}
```

###### /usuario/<id> - GET
###### Retorna um usuário
```bash
{
	"nome": "Nome Do Usuário", 
	"email": "usuario@email.com", 
}
```

#### Conteúdo

###### /conteudo - POST
###### Cadastra um conteúdo
```bash
{
	"titulo": "como trocar um pneu", 
	"descricao": "tira o velho e põe o novo", 
	"categoria": "ti", 
	"arquivos": [
		"base64ajsdhlakhsdlkahlksdhalsdhjlak", 
		"base64qiuoweoiquwoeiquoewiqweqoui", 
		"base64znxbcnvmnvmnzxmczmbxcbnzvxcbn"
	]
}
```

###### /conteudo - GET
###### Retorna um dicionario com todos os conteúdos
```bash
{
	{
		id: 1, 
		tipo: "Artigo", 
		titulo: "Como trocar tal peça do caminhão", 
		descricao: "É explicado como trocar tal peça do caminhão", 
		midia: File
	}, 
	{
		id: 2, 
		tipo: "Artigo", 
		titulo: "Como prender o container", 
		descricao: "É explicado como trocar prender o container", 
		midia: File
	}
}
```

###### /conteudo/<id> - GET
###### Retorna um dicionario de um conteúdo específico
```bash
{
	id: 1, 
	tipo: "Artigo", 
	titulo: "Como trocar tal peça do caminhão", 
	descricao: "É explicado como trocar tal peça do caminhão", 
	midia: File
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
                },
                {
                    "midia": "base64qiuoweoiquwoeiquoewiqweqoui"
                },
                {
                    "midia": "base64znxbcnvmnvmnzxmczmbxcbnzvxcbn"
                }
            ],
            "descricao": "tira o velho e põe o novo",
            "id": 1,
            "titulo": "como trocar um pneu"
        }
    ],
    "code": 200
}
```