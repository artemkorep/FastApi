from typing import Optional

from fastapi import FastAPI
import wikipedia
from pydantic import BaseModel

app = FastAPI(
    title = 'Wikipedia'
)


class Articles(BaseModel):
    article: list[str]


@app.get('/article/{article}', response_model=Articles) # list of article titles
def get_article(article: str, cnt_articles: int):
    """Название статей"""
    return Articles(article=wikipedia.search(article, results=cnt_articles))


class Sentences(BaseModel):
    title: str


@app.get('/sentence',response_model=Sentences) # returns the correct text
def get_sentence(sentence: str):
    """Возвращает правильный текст"""
    return Sentences(title=wikipedia.suggest(sentence))


class Pagesname(BaseModel):
    input: str
    cnt: int



class Description(BaseModel):
    title: list[str]


@app.post('/page', response_model=Description)
def get_page(name_page: Pagesname):
    """Название статей с передачей параметров в теле"""
    return Description(title=wikipedia.search(name_page.input, results=name_page.cnt))

# class Inputbody(BaseModel):
#     stroka: str
#
# class BodyPage(BaseModel):
#     title: str
#     original_title: str
#     pageid: int
#     url: int
#
#
# @app.post('/pagetest', response_model=BodyPage)
# def page_test(test: Inputbody):
#     return BodyPage(title=wikipedia.page(test.stroka))


# {
#   "title": "WJXT",
#   "original_title": "WJXT",
#   "pageid": "1453424",
#   "url": "https://en.wikipedia.org/wiki/WJXT"
# }
# @app.post('/page/{name_page}')
# def get_page(name_page: str):
#     return wikipedia.page(name_page)