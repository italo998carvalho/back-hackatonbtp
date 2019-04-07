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
	"senha": "123"
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

###### /conteudo/<id>
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