from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import User, Pets
from . import db
import json

views = Blueprint("views", __name__)


@views.route("/", methods=["GET", "POST"])
@login_required
def home():
    return render_template("home.html", user=current_user)


@views.route("/add-pet", methods=["GET", "POST"])
@login_required
def add_pet():
    if request.method == "POST":
        name = request.form.get("name")
        species = request.form.get("species")
        breed = request.form.get("breed")
        age = request.form.get("age")
        new_pet = Pets(
            user_id=current_user.id, name=name, species=species, breed=breed, age=age
        )
        db.session.add(new_pet)
        db.session.commit()
        flash("Pet added!", category="success")
    return render_template("add-pet.html", user=current_user)


@views.route("/delete-pet/<int:id>")
@login_required
def delete_pet(id):
    pet_to_delete = Pets.query.filter_by(id=id).first()
    if pet_to_delete:
        db.session.delete(pet_to_delete)
        db.session.commit()
        flash("Pet deleted.", category="success")
    return render_template("home.html", user=current_user)


@views.route("/edit-pet/<int:id>", methods=["GET", "POST"])
@login_required
def edit_pet(id):
    pet_to_edit = Pets.query.filter_by(id=id).first()
    if request.method == "POST":
        pet_to_edit.name = request.form.get("name")
        pet_to_edit.species = request.form.get("species")
        pet_to_edit.breed = request.form.get("breed")
        pet_to_edit.age = request.form.get("age")
        db.session.commit()
        flash("Pet updated.", category="success")
        return render_template("home.html", user=current_user)
    return render_template("edit-pet.html", pet=pet_to_edit, user=current_user)
