from app.main import main


@main.route('/')
def home():
    return "Salutare tuturor!"