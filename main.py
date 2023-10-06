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