from app.items import items
from flask import render_template

@items.route('/show_items')
def items_offering():
    return render_template("show_items.html")

@items.route('/show_layout')
def layout_offering():
    return render_template("show_layout.html")


@items.route('/events_list')
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
