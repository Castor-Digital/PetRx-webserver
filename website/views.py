from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note, Pet
from . import db
import json

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(str(note)) > 0:
            new_note = Note(note=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')

        else:
            flash('Note must be greater than 0 characters.', category='error')

        pet = request.form.get('pet')
        if len(str(pet)) > 0:
            new_pet = Pet(data=pet, user_id=current_user.id)
            db.session.add(new_pet)
            db.session.commit()
            flash('Pet added!', category='success')

        else:
            flash('Pet must be greater than 0 characters.', category='error')

    return render_template("home.html", user=current_user)


@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})

@views.route('/delete-pet', methods=['POST'])
def delete_pet():
    pet = json.loads(request.data)
    petId = pet['petId']
    pet = Pet.query.get(petId)
    if pet:
        if pet.user_id == current_user.id:
            db.session.delete(pet)
            db.session.commit()

    return jsonify({})