from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Pet
from . import db
import json

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        pet = request.form.get('pet')
        new_pet = Pet(data=pet, user_id=current_user.id)
        db.session.add(new_pet)
        db.session.commit()
        flash('Pet added!')

    return render_template("home.html", user=current_user)

@views.route('/delete-pet', methods=['POST'])
def delete_pet():
    pet = json.loads(request.data)
    petId = pet['petId']
    pet = Pet.query.get(petId)
    if pet:
        if pet.user_id == current_user.id:
            db.session.delete(pet)
            db.session.commit()
            flash('Pet removed.')
        else:
            flash('You are not authorized to remove this pet.')