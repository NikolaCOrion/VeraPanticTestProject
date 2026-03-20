import logging
from models.models import Project as ProjectModel

def list_projects(db):
    return db.query(ProjectModel).all()

def get_project(db, project_id: int):
    return db.query(ProjectModel).filter(ProjectModel.id == project_id).first()

def create_project(db, project):
    logging.info("Creating project...")
    db_project = ProjectModel(
        name = project.name,
        profile_id = project.profile_id,
        start_date = project.start_date,
        end_date = project.end_date
    )
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project

def update_project(db, project_id: int, project):
    db_project = db.query(ProjectModel).filter(ProjectModel.id == project_id).first()
    if not db_project:
        return None
    
    update_data = project.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_project, key, value)

    db.commit()
    db.refresh(db_project)
    return db_project

def delete_project(db, project_id: int):
    logging.info(f"Deleting project {project_id}...")
    db_project = db.query(ProjectModel).filter(ProjectModel.id == project_id).first()
    if not db_project:
        return None
    db.delete(db_project)
    db.commit()
    return db_project