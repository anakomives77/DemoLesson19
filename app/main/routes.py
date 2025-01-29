from app.main import main
from flask import render_template

"""
@main.route('/')
def home():
   return "Salutare tuturor!"
"""

@main.route('/')
def events_list_display():
    list_of_events = [
        {
            "name": "cina cu Elena",
            "date": "2025-01-21",
            "time": "11:50",
            "description": "in Bucuresti, la restaurant Vatra"
        },
    {
        "name": "pranz cu Andrei",
        "date": "2025-01-25",
        "time": "13:30",
        "description": "la restaurant Casa Verona"
    },
    {
        "name": "intalnire de afaceri",
        "date": "2025-01-30",
        "time": "10:00",
        "description": "in Bucuresti, biroul principal"
    }
    ]

    return render_template("events_list.html",  events=list_of_events)