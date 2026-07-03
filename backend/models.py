from pydantic import BaseModel

class Project(BaseModel):
    title: str
    description: str
    tech_stack: list[str]
    github_url: str | None = None  # opzionale, può non esserci