# Boreal Api

Api feita em python com FastAPI
Através dessa API você consegue criar um usuário, gerar um token para o mesmo

## Primeiros Passos

Instalar os requeriments:
```
$ pip install -r requeriments.txt
```

## Iniciar a aplicação

Já no diretório principal da aplicação

```
$ uvicorn main:app
```

## Consumindo API

### Register
Para se registrar, será necessário um POST na rota '/register'

Vamos enviar um MULTIPART FORM com Chave e Valor

```
username: 'seu usuário'
password: 'sua senha'
```

e irá retornar um status code com details informando se a ação foi bem sucedida ou não

### Login

Depois de criar o usuário e receber o status code 200
será necessário um POST na rota '/login'

Seguindo o mesmo modelo acima
```
username: 'seu usuário'
password: 'sua senha'
```

Após ambos estarem confirmados, a API retornará o TOKEN do usuário (algo parecido com o 'acess_token' abaixo)


### Protected

Para verificar o usuário com base no TOKEN
será necessário um POST na rota '/protected'

Dessa vez, você pegará o Token que foi retornado acima e enviará como Auth Bearer
```
  {
    "acess_token":
      "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2MzgzMzg3NDcsImlhdCI6MTYzODMzODY4Nywic3ViIjoicHluayJ9.A2VSzsIuWtZJ6BhVr61WNFPRIIBgzRN6OJQgjIwr8Ms"
  }
```

O token será validado e retornará o nome do usuário

### Order

Depois de estar logado, ainda com o token no auth bearer
Será necessário um POST na rota '/order'

Modelo a ser enviado
```
{
	"user": "seuuser",
	"order": 1.500,
	"previousorder": true
}
```

e retornará um json com responde 200 com os mesmos itens do payload


### Beers

Depois de estar logado, ainda com o token no auth bearer
**Faça um POST na rota '/beers'**

Retornará um dicionário com uma lista de nomes de cervejas obtidos de uma API terceira

### unprotected

A rota '/unprotected' retornará
```{"Hello": "World"}```

Indicando que pode ser acessada sem login

## FERRAMENTAS
* Linguagens: Python 3
* Bibliotecas: FastAPI e SQLite

Feito por: Caio Reis
