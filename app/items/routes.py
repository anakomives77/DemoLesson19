from app.items import items
from flask import render_template

@items.route('/show_items_many_xxx2')
def items_offering():
    return render_template("show_items.html")

@items.route('/show_layout')
def layout_offering():
    return render_template("show_layout.html")



