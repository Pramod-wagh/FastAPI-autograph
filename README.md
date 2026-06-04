# FastAPI Autograph Book

A simple FastAPI web app that lets friends leave messages and signatures in a digital college autograph book. The project uses Jinja2 templates, SQLAlchemy with SQLite, and a basic HTTP auth page to view saved entries.

## Overview

This application has three main user-facing flows:

1. Home page: displays the college memory page and a button to add an autograph.
2. Autograph form: collects a visitor’s name, contact number, email, hometown, and optional note.
3. Entries page: shows all saved autograph entries, protected with simple Basic Auth.

## Features

- FastAPI backend with route-based page rendering
- Jinja2 templates for HTML views
- SQLite database for persistent storage
- Static file serving for CSS and images
- Admin-protected view of all entries using HTTP Basic Authentication
- Auto-creation of database tables on startup

## Tech Stack

- Python 3.13
- FastAPI
- Uvicorn
- SQLAlchemy
- Jinja2
- SQLite

## Project Structure

- app/main.py: application startup, DB initialization, static files mount
- app/routes.py: all API and page routes
- app/models.py: SQLAlchemy model for autograph entries
- app/database.py: SQLite engine, session factory, and base model
- app/templates/: Jinja2 HTML pages
- app/static/: CSS and image assets
- autograph.db: SQLite database file created at runtime

## Workflow

1. Start the app with Uvicorn.
2. Open the home page at `/`.
3. Click “Give Your Autograph” to open the form at `/autograph`.
4. Submit the form; the data is saved into the `autograph` table in SQLite.
5. The user is redirected to a thank-you page.
6. To view all entries, open `/entries` and sign in with:
   - Username: `pramod`
   - Password: `autograph123`

## Routes

- GET `/` → Home page
- GET `/autograph` → Autograph form page
- POST `/autograph` → Save a new autograph entry
- GET `/entries` → View all saved entries (admin protected)

## Database

The app uses SQLite with the following table:

- `autograph`

Fields in the table:

- `id` (primary key)
- `full_name`
- `contact`
- `email`
- `hometown`
- `note`

## Setup

1. Install dependencies:

   ```bash
   uv sync
   ```

2. Run the server:

   ```bash
   uv run python -m uvicorn app.main:app --reload
   ```

3. Open the app in your browser:

   ```text
   http://127.0.0.1:8000/
   ```

## Useful Commands

Start the app:

```bash
uv run python -m uvicorn app.main:app --reload
```

View the database:

```bash
sqlite3 autograph.db
```

Useful SQLite queries:

```sql
.tables
.schema
SELECT * FROM autograph;
```

## Notes

- The database file is created automatically when the application starts.
- Static assets are served from `app/static/`.
- This project is ideal for learning FastAPI routing, Jinja templates, SQLAlchemy models, and basic authentication.
