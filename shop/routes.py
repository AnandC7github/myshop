# shop/routes.py
from flask import render_template, session, request, redirect, url_for, flash
from shop import app, db , bcrypt
from shop.admin.models import User, db_session

from shop.admin.forms import RegistrationForm
import os

@app.route('/')
def home():
    return "Home page of your shop"

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        hash_password = bcrypt.generate_password_hash(form.password.data)
        user = User(name=form.name.data,username= form.username.data, email = form.email.data,
                    password = hash_password)
        db_session.add(user)
        flash('Thanks for registering')
        return redirect(url_for('login'))
    return render_template('admin/register.html', form=form, title='Registeration Page')
