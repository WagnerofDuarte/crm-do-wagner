from flask import Blueprint, render_template, request, redirect, url_for
from crm import db

home = Blueprint('home', __name__, template_folder="templates")

@home.route('/')
def index():
    return render_template('index.html')