from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from .database import Base, engine
from .routes import router

app = FastAPI(title="college autograph App")

Base.metadata.create_all(bind=engine)

app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.include_router(router)


def main():
    print("Hello from my-autograph!")


if __name__ == "__main__":
    main()
