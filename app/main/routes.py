from app.main import main
from flask import render_template

"""
@main.route('/')
def home():
   return "Salutare tuturor!"
"""

@main.route('/')
def main_page():
    return render_template("main_view.html")

@main.route('/add_event')
def add_event():
    return render_template("add_event.html")


@main.route('/delete_event')
def delete_event():
    return render_template("delete_event.html")


@main.route('/show_event')
def show_event():
    return render_template("show_event.html")


@main.route('/events')
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