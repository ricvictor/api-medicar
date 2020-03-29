
# API Medicar - Gerenciamento de uma Clínica
API com a funcionalidade de gerenciar agendamentos de consultas em uma clínica.

## Funções do usuário (API)
* O cliente da clínica pode criar uma conta no sistema
* O cliente da clínica pode se autenticar no sistema
* O cliente pode marcar uma consulta
  * Não deve ser possível marcar consultas para um dia e horário não disponível ou já alocado para outro cliente
  * Não deve ser possível marcar consultas para dia e horário passados
  * Não deve ser possível marcar consultas para um dia horário na qual o paciente já tem uma consulta marcada
* O cliente pode desmarcar uma consulta
  * Não deve ser possível desmarcar uma consulta que já aconteceu
* O cliente pode visualizar as suas consultas marcadas que ainda não aconteceram

## Funções do gestor da clínica (Interface administrativa Django)
* O gestor da clínica pode cadastrar especialidades médicas
* O gestor da clínica pode cadastrar médicos
* O gestor da clínica pode alocar médicos em horários específicos de um dia

## Instalação
 Para subir localmente a aplicação, criar um ambiente virtual através do comando:
```python
python -m venv venv
``` 
 Após a criação do ambiente fazer a instalação dos pacotes específicos do arquivo `requirements.txt` utilizando o seguinte comando:
```python
pip install -r requirements.txt
```
### Rodando a aplicação
Aplicando as migrations:
```python
python manage.py makemigrations
python manage.py migrate
```
Rodar a aplicação:
```python
python manage.py runserver
```
Após subir a aplicação, a API estará disponibilizada através do endereço [http://127.0.0.1:8000](http://127.0.0.1:8000) .

## API
A API possui os seguintes endpoints:

### Autenticação
Todos os endpoints, exceto os de login, logout e registro de usuário, possuem autenticação  por Token. Exemplo de requisição:
```
GET /especialidades/
Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b
```

* Endpoint de login:
```
POST /account/login
{
    "username": "",
    "email": "",
    "password": ""
}
```

* Endpoint de logout:
```
GET /account/logout
```

* Endpoint de troca de senha:
```
POST /account/password/change/
{
    "new_password1": "",
    "new_password2": ""
}
```

* Endpoint de troca de senha:
```
POST /account/password/change/
{
    "new_password1": "",
    "new_password2": ""
}
```
* Endpoint de reset de senha (necessário email):
```
POST /account/password/reset/
{
    "email": ""
}
```
* Endpoint de confirmação do reset de senha (necessário email):
```
POST /account/password/reset/confirm/
{
    "new_password1": "",
    "new_password2": "",
    "uid": "",
    "token": ""
}
```

* Endpoint de informação do usuário logado:
```
GET, PUT, PATCH /account/user/
{
    "username": "",
    "first_name": "",
    "last_name": ""
}
```

* Endpoint de registro de usuário:
```
POST /account/registration/
{
    "username": "",
    "password1": "",
    "password2": "",
    "email": ""
}
```

* Endpoint de confirmação de email do novo registro de usuário:
```
POST /account/registration/verify-email/
{
    "key": ""
}
```
### Endpoints de listagem e agendamento de consultas.
Todas as especificações dos endpoints de listagem e agendamento seguem o seguinte modelo [Especificações técnicas (Desafio Medicar)](https://github.com/Intmed-Software/vagas/blob/master/backend/README.md)
