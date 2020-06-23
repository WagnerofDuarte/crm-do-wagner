from flask import Blueprint, render_template, request, redirect, url_for
from crm import db
from crm.projetos.models import Projeto
import os

projeto = Blueprint('projeto', __name__, template_folder="templates")

@projeto.route('/especifico/<_id>', methods=['GET'])
def especifico(_id):

    i = 0

    projeto = Projeto.query.get_or_404(_id)

    projeto_comentarios = projeto.comentarios.split('|')
    
    return render_template('especifico_projetos.html', projeto = projeto, projeto_comentarios = projeto_comentarios)