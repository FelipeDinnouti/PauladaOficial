# app/routes/home.py
import utils.pages as pages

# Routing: GET
def homepage():
    pages.home_page_main_text_file = open("static/texts/MainPage.md", "r")
    pages.home_page_main_text = pages.home_page_main_text_file.read() # Hot update the markdown (for live editing)
    return pages.home

def forum():
    return pages.forum

def news():
    return pages.news

def rules():
    pages.rules_main_text_file = open("static/texts/OfficialRegulamentation.md", "r")
    pages.rules_main_text = pages.home_page_main_text_file.read()

    return pages.rules