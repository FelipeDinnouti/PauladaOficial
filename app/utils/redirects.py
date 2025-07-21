from fasthtml.common import *

# Redirects, 303 prevents POST (fixes 405 error i think)
login_redirect = RedirectResponse('/login', status_code=303)
profile_redirect = RedirectResponse('/perfil', status_code=303)
home_redirect = RedirectResponse('/', status_code=303)