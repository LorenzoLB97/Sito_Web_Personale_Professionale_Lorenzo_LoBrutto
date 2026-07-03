from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import projects

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # in sviluppo va bene, in produzione andrà ristretto
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(projects.router)

@app.get("/")
def read_root():
    return {"message": "Ciao, sono il backend del mio portfolio!"}