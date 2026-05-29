from flask import Blueprint, jsonify, request
from .models import Note
from . import db

api = Blueprint('api', __name__)


# CREATE NOTE
@api.route('/api/notes', methods=['POST'])
def create_note():
    data = request.get_json()

    if not data or 'data' not in data:
        return jsonify({
            "error": "Note content is required"
        }), 400

    new_note = Note(
        data=data['data'],
        user_id=1
    )

    db.session.add(new_note)
    db.session.commit()

    return jsonify({
        "message": "Note created successfully",
        "id": new_note.id,
        "data": new_note.data
    }), 201


# READ ALL NOTES
@api.route('/api/notes', methods=['GET'])
def get_notes():
    notes = Note.query.all()

    output = []

    for note in notes:
        output.append({
            "id": note.id,
            "data": note.data,
            "date": str(note.date)
        })

    return jsonify(output), 200


# READ SINGLENOTE
@api.route('/api/notes/<int:id>', methods=['GET'])
def get_note(id):
    note = Note.query.get(id)

    if not note:
        return jsonify({
            "error": "Note not found"
        }), 404

    return jsonify({
        "id": note.id,
        "data": note.data,
        "date": str(note.date)
    }), 200


# UPDATE NOTE
@api.route('/api/notes/<int:id>', methods=['PUT'])
def update_note(id):
    note = Note.query.get(id)

    if not note:
        return jsonify({
            "error": "Note not found"
        }), 404

    data = request.get_json()

    if not data or 'data' not in data:
        return jsonify({
            "error": "Missing note content"
        }), 400

    note.data = data['data']
    db.session.commit()

    return jsonify({
        "message": "Note updated successfully",
        "id": note.id,
        "data": note.data
    }), 200

# DELETE NOTE
@api.route('/api/notes/<int:id>', methods=['DELETE'])
def delete_note(id):
    note = Note.query.get(id)

    if not note:
        return jsonify({
            "error": "Note not found"
        }), 404

    db.session.delete(note)
    db.session.commit()

    return jsonify({
        "message": "Note deleted successfully",
        "id": id
    }), 200