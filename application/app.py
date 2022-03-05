from flask import Flask, render_template

from db import DBEngine
from models import Base
from config import ApplicationConfig
from views import transactions


def get_application() -> Flask:
    """Method to create an application to manage currency payments"""

    config = ApplicationConfig()
    app = Flask(__name__)
    app.config.update(**config.dict())

    return app


app = get_application()

app.register_blueprint(transactions, url_prefix="/")


@app.errorhandler(404)
def page_not_found(error):
    """Method to handle 404 error"""

    return render_template("404.html")


if __name__ == '__main__':
    app.run(host="localhost")
