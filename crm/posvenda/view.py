from flask import Blueprint, render_template, request, redirect, url_for
from crm import db

pos_venda = Blueprint('pos_venda', __name__, template_folder="templates")

@pos_venda.route('/')
def index():
    return render_template('posvenda.html')