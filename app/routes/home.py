# app/routes/home.py
import app.utils.pages as pages

# Routing: GET
def homepage(_session):
    pages.home_page_main_text_file = open("static/texts/MainPage.md", "r")
    pages.home_page_main_text = pages.home_page_main_text_file.read() # Hot update the markdown (for live editing)
    return pages.home

def forum(_session):
    return pages.forum

def news(_session):
    return pages.news

def rules(_session):
    pages.rules_main_text_file = open("static/texts/OfficialRegulamentation.md", "r")
    pages.rules_main_text = pages.home_page_main_text_file.read()

    return pages.rules