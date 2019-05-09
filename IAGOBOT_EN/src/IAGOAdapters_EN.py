# -*- coding: utf-8 -*-
# from chatterbot import ChatBot
from chatterbot.logic import LogicAdapter
from datetime import datetime


def englishMonths(month):
    result = ""
    if month == 1:
        result = "January"
    elif month == 2:
        result = "February"
    elif month == 3:
        result = "March"
    elif month == 4:
        result = "April"
    elif month == 5:
        result = "May"
    elif month == 6:
        result = "June"
    elif month == 7:
        result = "July"
    elif month == 8:
        result = "August"
    elif month == 9:
        result = "September"
    elif month == 10:
        result = "October"
    elif month == 11:
        result = "November"
    elif month == 12:
        result = "Décember"
    else:
        result = "Unknown date"
    return result


class HourAdapter(LogicAdapter):

    def __init__(self, **kwargs):
        super(HourAdapter, self).__init__(**kwargs)
    
    def can_process(self, statement):
        words = ['hour', 'date', 'now']
        if any(x in statement.text.split() for x in words):
            return True
        else:
            return False

    def process(self, statement):
        from chatterbot.conversation import Statement
        # import random
        confidence = 1
        t1 = datetime.now()
        selected_statement = Statement("Today is %s %s %s, time is %s hours and %s minutes" % (englishMonths(t1.month),t1.day,t1.year, t1.hour, t1.minute))
        selected_statement.confidence = confidence
        
        return selected_statement
