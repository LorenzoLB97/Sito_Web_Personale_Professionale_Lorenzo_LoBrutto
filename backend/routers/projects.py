from fastapi import APIRouter
from models import Project

router = APIRouter(prefix="/projects", tags=["projects"])

@router.get("/projects")
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