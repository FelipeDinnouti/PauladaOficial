from fasthtml.common import *

from app.routes import home, users
from app.utils.redirects import *

import json
import sys
from functools import wraps

# Before wares
counter_file = Path("visit_count.json")

# Checks if the user is authenticated by checking the session information
def user_auth_before(request, session):
    auth = request.scope['auth'] = session.get('auth', None)
    if not auth: return login_redirect

# Pages allowed to visit without login
whitelisted_pages = ['/login', '/', '/about', '/cadastro', '/regras']

# Runs right before changing pages
beforeware = Beforeware(
    user_auth_before,
    skip=[r'.*\.png',r'/favicon\.ico', r'/static/.*', r'.*\.css', r'.*\.js',] + whitelisted_pages
)

hdrs = (
    MarkdownJS(), 
        Link(
            rel="stylesheet", 
        href="static/css/mystyle.css"
        ),
        Link(
            rel="stylesheet", 
        href="static/css/navigation.css"
        ),
        Link(
            rel="stylesheet", 
        href="static/css/login.css"
        ),
        Link(rel="stylesheet", href="static/css/pico-main/css/pico.css",), 
        Script(src="static/scripts/jquery-3_7_1_min.js"),
        Script(src="static/scripts/visible.js"), 
        # Script(src="static/scripts/title.js"),
    ) 

# FastAPI app
app, rt = fast_app( 
    pico=False,
    debug=True,
    before=beforeware,
    hdrs=hdrs,
    title="Paulada Oficial"
)

# Routing: GET
@rt("/")
def get(session):
    return home.homepage(session)

# @rt("/about")
# def get(session):
#     return pages.about

@rt("/forum")
def get(session):
    return home.forum(session)

@rt("/novidades")
def get(session):
    return home.news(session)

@rt("/regras")
def get(session):
    return home.rules(session)

@rt("/cadastro")
def get(session):   
    return users.register_page(session)

@rt("/cadastro")
def post(name: str, email: str, password: str, gender: str, session): # Variable position must match form input index
    return users.register(name, email, password, gender, session)

@rt("/login")
def get(session):
    return users.login_page(session)

@rt("/login")
def post(email: str, password: str, session):
    return users.login(email, password, session)


@rt("/perfil")
def get(session):
    return users.profile_page(session)

@rt("/perfil")
def post(session):
    return users.logout(session)

serve(port=38001)