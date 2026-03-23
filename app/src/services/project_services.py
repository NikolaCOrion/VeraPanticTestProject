from fastapi import HTTPException, status
from repositories import project_repository
from repositories import profile_repository

def list_projects(db):
    return project_repository.list_projects(db)

def get_project(db, project_id: int):
    project = project_repository.get_project(db, project_id)
    if not project:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Project not found")
    
    return project

def create_project(db, project):
    #provera da li profil postoji
    profile = profile_repository.get_profile(db, project.profile_id)
    if not profile:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Profile not found")
    
    return project_repository.create_project(db, project)

def update_project(db, project_id: int, project):
    db_project = project_repository.get_project(db, project_id)
    if not db_project:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Project not found")
    
    #ako se menja profile_id, proverava da li postoji
    if project.profile_id:
        profile = profile_repository.get_profile(db, project.profile_id)
        if not profile:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Profile not found")
        
    return project_repository.update_project(db, project_id, project)

def delete_project(db, project_id: int):
    db_project = project_repository.get_project(db, project_id)
    if not db_project:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Project not found")
    
    project_repository.delete_project(db, project_id)
    return {"message", "Project deleted"}