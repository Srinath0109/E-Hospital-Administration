from flask import Blueprint, jsonify, request
from models import db, Patient, Doctor, Appointment

hospital_routes = Blueprint("hospital_routes", __name__)

# Register a patient
@hospital_routes.route("/patients", methods=["POST"])
def register_patient():
    data = request.json
    new_patient = Patient(name=data["name"], age=data["age"], disease=data["disease"])
    db.session.add(new_patient)
    db.session.commit()
    return jsonify({"message": "Patient registered successfully"}), 201

# Get all patients
@hospital_routes.route("/patients", methods=["GET"])
def get_patients():
    patients = Patient.query.all()
    return jsonify([{"id": p.id, "name": p.name, "age": p.age, "disease": p.disease} for p in patients])

# Assign a doctor
@hospital_routes.route("/doctors", methods=["POST"])
def assign_doctor():
    data = request.json
    new_doctor = Doctor(name=data["name"], specialty=data["specialty"])
    db.session.add(new_doctor)
    db.session.commit()
    return jsonify({"message": "Doctor added successfully"}), 201

# Book an appointment
@hospital_routes.route("/appointments", methods=["POST"])
def book_appointment():
    data = request.json
    new_appointment = Appointment(patient_id=data["patient_id"], doctor_id=data["doctor_id"], date=data["date"])
    db.session.add(new_appointment)
    db.session.commit()
    return jsonify({"message": "Appointment booked successfully"}), 201
