from flask import Blueprint, render_template, request, redirect, url_for
from crm import db
from crm.projetos.models import Projeto
import os

projeto = Blueprint('projeto', __name__, template_folder="templates")

@projeto.route('/', methods=['POST', 'GET'])
def index():

    projetos = Projeto.query.all()
    
    if(request.method == 'POST'):
        nome = request.form['pesquisa']
        search = "%{}%".format(nome)
        projetos = Projeto.query.filter(Projeto.nome.like(search)).all()
        for i in projetos:
            print(i.nome)

    return render_template('teste.html', projetos = projetos)

@projeto.route('/especifico/<_id>', methods=['GET'])
def especifico(_id):

    i = 0

    projeto = Projeto.query.get_or_404(_id)
    projeto_comentarios = projeto.comentarios.split('|')
    
    return render_template('especifico_projetos.html', projeto = projeto, projeto_comentarios = projeto_comentarios)