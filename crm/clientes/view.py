from flask import Blueprint, render_template, request, redirect, url_for
from crm import db
from crm.clientes.models import Cliente
import os

cliente = Blueprint('cliente', __name__, template_folder="templates")


@cliente.route('/especifico/<_id>', methods=['GET', 'POST'])
def especifico(_id):

    cliente = Cliente.query.get_or_404(_id)

    if(request.method == 'POST' and 'nome' in request.form):
        nome = request.form['cliente']
        email = request.form['email']
        telefone = request.form['telefone']
        endereco = request.form['endereco']
        status = request.form['status']

        cliente.nome = nome
        cliente.email = email
        cliente.telefone = telefone
        cliente.endereco = endereco
        cliente.status = status

        db.session.commit()

        return redirect(url_for('cliente.especifico', _id = cliente.id))

    i = 0

    cliente_dts_status = cliente.historico_status
    cliente_dts_status = cliente_dts_status.split(',')

    cliente_observacoes = cliente.observacoes.split('|')

    print(url_for('static', filename='css/cliente-especifico.css'))

    while(i < len(cliente_dts_status)):
        cliente_dts_status[i] = cliente_dts_status[i][-2:] + '/' + cliente_dts_status[i][4:-2] + '/' + cliente_dts_status[i][:4]
        i = i + 1
    
    return render_template('especifico_cliente.html', cliente = cliente, cliente_dts_status = cliente_dts_status, cliente_observacoes = cliente_observacoes)

@cliente.route('/excluir/<_id>', methods=['GET', 'POST'])
def excluir(_id):
    cliente = Cliente.query.get_or_404(_id)
    
    if(request.method == 'POST'):
        
        db.session.delete(cliente)
        db.session.commit()

        return redirect(url_for('cliente.index'))

    return render_template('excluir_cliente.html', cliente = cliente)