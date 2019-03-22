from bottle import (
    route, run, template, request, redirect
)
import string
from scraputils import get_news
from db import News, session
from bayes import NaiveBayesClassifier


@route("/news")
def news_list():
    s = session()
    rows = s.query(News).filter(News.label == None).all()
    return template('news_template', rows=rows)


@route("/add_label/")
def add_label():
    news_id = request.query.id
    label = request.query.label
    s = session()
    qurent = s.query(News).filter(News.id == news_id).one()
    qurent.label = label
    s.commit()
    redirect("/news")


@route("/update")
def update_news():
    news_update = get_news('https://news.ycombinator.com/newest', 1)
    authors = []
    titles = []
    s = session()
    for news in news_update:
        authors = authors.append(news['author'])
        titles = titles.append(news['title'])
    existing_news = s.query(News).filter((News.author.in_(authors))and(News.title.in_(titles))).all()
    for curent in news_update:
        if not existing_news or curent not in existing_news:
            s.add(News(**curent))
    s.commit()
    redirect("/news")


@route("/classify")
def classify_news():
    s = session()
    labeled_news = s.query(News).filter(News.label != None).all()
    x_train = [clean(news.title) for news in labeled_news]
    y_train = [news.label for news in labeled_news]
    classifier = NaiveBayesClassifier(1)
    classifier.fit(x_train, y_train)

    rows = s.query(News).filter(News.label == None).all()
    good, maybe, never = [], [], []
    for row in rows:
        prediction = classifier.predict([clean(row.title)])
        if prediction == 'good':
            good.append(row)
        elif prediction == 'maybe':
            maybe.append(row)
        else:
            never.append(row)

    return template('news_recommendations', good=good, maybe=maybe, never=never)


def clean(s):
    translator = str.maketrans("", "", string.punctuation)
    return s.translate(translator).lower()


if __name__ == "__main__":
    run(host="localhost", port=8080)