"""Send paths for the artilces based on index_controller"""
from app.controllers.controller import ControllerBase
from flask import render_template

class ArticleController(ControllerBase):

    @staticmethod
    def get_SOLID():
        """renders AAA_Testing page"""
        return render_template('SOLID.html')


    @staticmethod
    def get_AAAtesting():
        """renders AAA_Testing page"""
        return render_template('AAA_Testing.html')

    
    @staticmethod
    def get_glossary():
        """renders AAA_Testing page"""
        return render_template('OOP_glossary.html')

    
    @staticmethod
    def get_OOP_Principles():
        """renders AAA_Testing page"""
        return render_template('OOP_principles.html')
