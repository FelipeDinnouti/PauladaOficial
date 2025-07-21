from fasthtml.common import *
from utils.redirects import *

import utils.pages as pages
import db.user as db_users

MAX_NAME_LENGTH = 254
MAX_PASSWORD_LENGTH = 32
MAX_EMAIL_LENGTH = 254

## Routing: GET

def register_page():
    return pages.register

def login_page():
    return pages.login

def profile_page(session):
    email, password = session.get("auth")

    user = db_users.fetch(email, password)

    if type(user) == int: # Any error
        return home_redirect

    gender_string = ""
    gender_string = "Mulher" if user.gender == db_users.GENDER_WOMAN else "Homem"
    

    return Div(
        pages.navigation_header,
        pages.Spacer(4, "em"),
        Div(
        H2(f"Perfil de {user.name}"),
        Br(),
        P(f"Gênero: {gender_string}"),
        P(f"E-mail: {user.email}"),
        pages.logout_form,
        id="main_section",
        ),
        cls="container",
    )

### --- POST

# Receives the login information and sets the auth variable in the session
def login(email: str, password: str, session):
    user = db_users.fetch(email, password)
    if user == -1:
        return Titled("Senha errada irmao")
    if user == -2:
        return Titled("Esse email nao foi cadastrado nao")

    session["auth"] = (email, password)
    return profile_redirect

def logout(session):
    session["auth"] = None
    return home_redirect

# Receives the register information and checks each field  
def register(name: str, email: str, password: str, gender: str, session):
    if len(name) > MAX_NAME_LENGTH:
        return Titled("Nome grande demais") 
    
    if len(email) > MAX_EMAIL_LENGTH:
        return Titled("Ninguém tem um email desse tamanho")
    
    if len(password) > MAX_PASSWORD_LENGTH:
        return Titled("Você não precisa de mais de 32 caracteres na sua senha")
    
    user = db_users.fetch(email, password)
    if user != -2: # User DOES exist
        return Titled("Já existe esse usuário ai meu")

    print(f"REGISTERING: email: {email}\npassword: {password}\ngender: {gender}")


    # Creates an entry in the database
    db_users.register(name, email, password, gender)
    session["auth"] = (email, password)

    return profile_redirect