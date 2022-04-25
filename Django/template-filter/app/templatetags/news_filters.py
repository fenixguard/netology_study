from django import template
from datetime import datetime as dt

register = template.Library()


@register.filter
def format_date(value):
    today = dt.timestamp(dt.today())
    delta = today - value
    if delta < 600:
        return 'только что'
    elif 600 <= delta < 86400:
        hours = round(delta / 3600)
        if hours in [1, 21]:
            ending = ''
        elif hours in [2, 3, 4, 22, 23, 24]:
            ending = 'а'
        else:
            ending = 'ов'
        return f'{hours} час{ending} назад'
    elif delta >= 86400:
        post_date = dt.utcfromtimestamp(value).date()
        return post_date.strftime('%Y-%m-%d')
    return value


@register.filter
def format_score(value):
    if value:
        if value < -5:
            return 'все плохо'
        elif -5 <= value <= 5:
            return 'нейтрально'
        elif value > 5:
            return "хорошо"
    else:
        return 'нет рейтинга'


@register.filter
def format_num_comments(value):
    if 0 < value <= 50:
        return value
    else:
        return '50+'


@register.filter
def format_selftext(value, count):
    if value:
        value = value.split()
        value = value[:count] + ['...'] + value[-count:]
        value = ' '.join(value)
        return value
    else:
        return ''
