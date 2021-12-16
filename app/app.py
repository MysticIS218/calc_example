"""A simple flask web app"""
from flask import Flask
from app.controllers.index_controller import IndexController
from app.controllers.calculator_controller import CalculatorController
from app.controllers.index_controller import IndexController
from app.controllers.calculator_controller import CalculatorController
from app.controllers.history_controller import HistoryController
from app.controllers.article_controller import ArtilceController

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

#No longer required recent changes
"""
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Operation = db.Column(db.String(64), index=True)
    value1 = db.Column(db.Integer, index=True)
    value2 = db.Column(db.Integer, index=True)
    result = db.Column(db.String(256))

    def to_dict(self):
        return {
            'operation': self.calculation,
            'value1': self.value1,
            'value2': self.value2,
            'result': self.result,
        }

    if __name__ == '__main__':
        app.run()
"""

@app.route("/", methods=['GET'])
def index_get():
    return IndexController.get()

@app.route("/calculator", methods=['GET'])
def calculator_get():
    return CalculatorController.get()

@app.route("/calculator", methods=['POST'])
def calculator_post():
    return CalculatorController.post()

@app.route("/oop_principles", methods=['GET'])
def oop_principles_get():
    """Get the OOP principles article from the Article Controller"""
    return ArticleController.get_oop_principles()

@app.route("/SOLID_principles", methods=['GET'])
def SOLID_Principles_get():
    """Get the OOP principles article from the Article Controller"""
    return ArticleController.get_SOLID_principles()

@app.route("/glossary", methods=['GET'])
def glossary_get():
    """Get the OOP principles article from the Article Controller"""
    return ArticleController.get_glossary()

@app.route("/AAA-testing", methods=['GET'])
def AAA_testing_get():
    """Get the OOP principles article from the Article Controller"""
    return ArticleController.get_AAAtesting()

