from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.user import User

@app.route('/')
def all_users():
    users = User.get_all()
    return render_template('readall.html', all_users = users)

@app.route('/users/new')
def add_user():
    return render_template('create.html')

@app.route('/add_users', methods = ['POST'])
def add_users():
    User.save(request.form)
    return redirect('/')

#show
@app.route('/users/<int:id>')
def show(id):
    data = {
        'id' : id
    }
    return render_template('show_user.html', user = User.get_one(data))

#edit
@app.route('/users/<int:id>/edit')
def edit_user(id):
    data = {
        'id' : id
    }
    return render_template('edit_user.html',  user = User.get_one(data))

@app.route('/update', methods = ['POST'])
def update():
    User.update(request.form)
    return redirect('/')

#delete user
@app.route('/users/<int:id>/destroy')
def delete_user(id):
    data = {
        'id' : id
    }
    User.delete(data)
    return redirect('/')


