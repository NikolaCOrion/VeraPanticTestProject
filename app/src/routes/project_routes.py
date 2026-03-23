from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from misc.database import get_db
from schemas.project_schemas import ProjectCreate, ProjectUpdate
from services import project_services

router = APIRouter(prefix="/api/v1/projects", tags=["Projects"])

@router.get("/")
def list_projects(db: Session = Depends(get_db)):
    return project_services.list_projects(db)

@router.get("/{project_id}")
def get_project(project_id: int, db: Session = Depends(get_db)):
    return project_services.get_project(db, project_id)

@router.post("/", status_code=201)
def create_project(project: ProjectCreate, db: Session = Depends(get_db)):
    return project_services.create_project(db, project)

@router.put("/{project_id}")
def update_project(project_id: int, project: ProjectUpdate, db: Session = Depends(get_db)):
    return project_services.update_project(db, project_id, project)

@router.delete("/{project_id}")
def delete_project(project_id: int, db: Session = Depends(get_db)):
    return project_services.delete_project(db, project_id)