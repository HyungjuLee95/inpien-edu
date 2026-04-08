from fastapi import FastAPI

from .db import Base, engine
from .routers import auth, inventory, items, locations

app = FastAPI(title="Inpien Edu API", version="0.1.0")

Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(items.router)
app.include_router(locations.router)
app.include_router(inventory.router)


@app.get("/health")
def health_check():
    return {"status": "ok"}
