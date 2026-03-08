from fastapi import APIRouter, Form, Request, Depends 
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session 

from .database import SessionLocal
from .models import Autograph

router = APIRouter()
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