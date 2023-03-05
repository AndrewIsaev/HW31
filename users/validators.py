import datetime

from dateutil.relativedelta import relativedelta
from django.core.exceptions import ValidationError


def check_domain(value: str):
    if "rambler.ru" in value.split("@")[-1]:
        raise ValidationError("Can`t use rambler email")


def check_age(value):
    age = relativedelta(datetime.date.today(), value).years
    if age < 9:
        raise ValidationError("Age less than 9 years")
