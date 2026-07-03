from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Project(BaseModel):
    title: str
    description: str
    tech_stack: list[str]
    github_url: str | None = None  # opzionale, può non esserci

@app.get("/projects")
def get_projects():
    projects = [
        Project(
            title="Il mio sito portfolio",
            description="Sito personale full-stack con FastAPI e frontend custom",
            tech_stack=["Python", "FastAPI", "JavaScript"],
            github_url="https://github.com/tuonome/mio-sito"
        ),
        Project(
            title="Altro progetto",
            description="Descrizione di esempio",
            tech_stack=["Python"],
        )
    ]
    return projects

@app.get("/")
def read_root():
    return {"message": "Ciao, sono il backend del mio portfolio!"}