from app import create_app

app=create_app()

@app.route('/hello/world/diana')
def home():
    return "Salutare tuturor!"

if __name__ == "__main__":
    app.run(debug=True)

