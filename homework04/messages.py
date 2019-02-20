from collections import Counter
import datetime
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
from typing import List, Tuple

from api import messages_get_history
from api_models import Message
from homework05 import config

Dates = List[datetime.date]
Frequencies = List[int]


plotly.tools.set_credentials_file(
    username=config.PLOTLY_CONFIG['username'],
    api_key=config.PLOTLY_CONFIG['api_key']
)


def fromtimestamp(ts: int) -> datetime.date:
    return datetime.datetime.fromtimestamp(ts).date()


def count_dates_from_messages(messages: List[Message]) -> Tuple[Dates, Frequencies]:
    """ Получить список дат и их частот
    :param messages: список сообщений
    """
    dates = []
    for message in messages:
        date = message.date
        date = fromtimestamp(date)
        dates.append(date)

    frequencies = Counter(dates)

    return list(frequencies.keys()), list(frequencies.values())


def plotly_messages_freq(dates: Dates, freq: Frequencies) -> None:
    """ Построение графика с помощью Plot.ly
    :param date: список дат
    :param freq: число сообщений в соответствующую дату
    """
    data = [go.Scatter(x=dates, y=freq)]
    py.iplot(data)


if __name__ == '__main__':
    a = messages_get_history(103854)
    for i in range(len(a)):
        a[i]=Message(**a[i])
    a = count_dates_from_messages(a)
    plotly_messages_freq(a[0],a[1])