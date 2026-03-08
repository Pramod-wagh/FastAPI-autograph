import secrets
from fastapi import APIRouter, Depends, Form, HTTPException, Request, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session 

from .database import SessionLocal
from .models import Autograph

router = APIRouter()
security = HTTPBasic()

ADMIN_USERNAME = "pramod"
ADMIN_PASSWORD = "autograph123"

def require_admin(credentials: HTTPBasicCredentials = Depends(security)):
    ok_user = secrets.compare_digest(credentials.username, ADMIN_USERNAME)
    ok_pass = secrets.compare_digest(credentials.password, ADMIN_PASSWORD)
    if not (ok_user and ok_pass):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect credentials",
            headers={"WWW-Authenticate": "Basic"},
        )
templates= Jinja2Templates(directory="app/templates")

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def home(request: Request):
    return templates.TemplateResponse("Index.html.jinja",{"request":request})

@router.get("/entries")
def view_entries(request: Request, db: Session = Depends(get_db), _: None = Depends(require_admin)):
    entries = db.query(Autograph).all()
    return templates.TemplateResponse("entries.html.jinja", {"request": request, "entries": entries})

@router.get("/autograph")
def autograph_form(request: Request):
    return templates.TemplateResponse("autograph.html.jinja", {"request": request})

@router.post("/autograph")
def submit_autograph(
    request: Request,
    full_name: str = Form(...),
    contact: str = Form(...),
    email: str = Form(...),
    hometown: str = Form(...),
    note: str = Form(""),
    db: Session = Depends(get_db)
):
    entry = Autograph(
        full_name=full_name,
        contact=contact,
        email=email,
        hometown=hometown,
        note=note
    )

    db.add(entry)
    db.commit()

    return templates.TemplateResponse(
        "thanks.html.jinja",
        {"request": request, "name": full_name}
    )