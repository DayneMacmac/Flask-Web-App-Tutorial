# Flask Web App – REST API Enhancement

## Project Overview

This project is based on the Flask Web Application Tutorial by Tech With Tim.  
The original application is a web-based note-taking system with user authentication.

This project enhances the original application by adding a **REST API feature** that allows full CRUD operations on notes using JSON.

---

## Original Application Features

- User registration and login system
- Create, view, and delete notes through a web interface
- SQLite database integration
- Flask-Login authentication system

---

## Added Feature: REST API for Notes

A RESTful API was implemented to manage notes without using the frontend.

### API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST   | /api/notes | Create a new note |
| GET    | /api/notes | Retrieve all notes |
| GET    | /api/notes/<id> | Retrieve a single note |
| PUT    | /api/notes/<id> | Update a note |
| DELETE | /api/notes/<id> | Delete a note |

---

## Request / Response Format

### Example: Create Note

**Request:**
```json
{
  "data": "My first API note"
}