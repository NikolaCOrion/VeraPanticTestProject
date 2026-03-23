from datetime import datetime

from sqlalchemy.orm import Session

from misc.database import SessionLocal

from models.models import Project as ProjectModel
from models.models import Profile as ProfileModel

from repositories.project_repository import create_project
from repositories.profile_repository import create_profile

from tests.conf import client


route = "/api/v1/projects"


def create_profiles(number_of_profiles: int, db: Session) -> list[ProfileModel]:
    profiles: list[ProfileModel] = []

    for i in range(number_of_profiles):
        profile = ProfileModel(name=f"Profile {i + 1}", age=25)
        created_profile = create_profile(db, profile)
        profiles.append(created_profile)

    return profiles


def create_projects(
    number_of_projects: int,
    db: Session,
    profiles: list[ProfileModel]
) -> list[ProjectModel]:
    projects: list[ProjectModel] = []

    for i in range(number_of_projects):
        project = ProjectModel(
            name=f"Project {i + 1}",
            profile_id=profiles[i % len(profiles)].id,
            start_date=datetime(2024, 1, 1),
            end_date=datetime(2024, 12, 31),
        )
        created_project = create_project(db, project)
        projects.append(created_project)

    return projects


class TestProjects:

    def setup_method(self) -> None:
        self.number_of_profiles = 3
        self.number_of_projects = 5

        self.db = SessionLocal()

        self.profiles = create_profiles(self.number_of_profiles, self.db)
        self.projects = create_projects(
            self.number_of_projects,
            self.db,
            self.profiles
        )

    def teardown_method(self) -> None:
        self.db.query(ProjectModel).delete()
        self.db.query(ProfileModel).delete()
        self.db.commit()

    def test_list_projects(self) -> None:
        response = client.get(route)

        assert response.status_code == 200
        assert len(response.json()) == self.number_of_projects

    def test_get_one(self) -> None:
        project = self.projects[0]

        response = client.get(f"{route}/{project.id}")

        assert response.status_code == 200
        data = response.json()

        assert data["id"] == project.id
        assert data["name"] == project.name
        assert data["profile_id"] == project.profile_id

    def test_get_nonexistent_404(self) -> None:
        response = client.get(f"{route}/9999")
        assert response.status_code == 404

    def test_create(self) -> None:
        new_project_data = {
            "name": "New Project",
            "profile_id": self.profiles[0].id,
            "start_date": "2024-01-01T00:00:00",
            "end_date": "2024-12-31T00:00:00"
        }

        response = client.post(route, json=new_project_data)

        assert response.status_code == 201
        data = response.json()

        assert data["name"] == new_project_data["name"]
        assert data["profile_id"] == new_project_data["profile_id"]

        db_project = self.db.query(ProjectModel).filter_by(id=data["id"]).first()
        assert db_project is not None

    def test_create_without_name_422(self) -> None:
        new_project_data = {
            "profile_id": self.profiles[0].id
        }

        response = client.post(route, json=new_project_data)

        assert response.status_code == 422

    def test_create_invalid_profile_404(self) -> None:
        new_project_data = {
            "name": "Invalid Project",
            "profile_id": 9999
        }

        response = client.post(route, json=new_project_data)
        assert response.status_code == 404

    def test_update(self) -> None:
        project = self.projects[0]

        update_data = {
            "name": "Updated Project",
            "profile_id": self.profiles[1].id,
            "start_date": "2025-01-01T00:00:00",
            "end_date": "2025-12-31T00:00:00"
        }

        response = client.put(f"{route}/{project.id}", json=update_data)

        assert response.status_code == 200
        data = response.json()

        assert data["name"] == update_data["name"]
        assert data["profile_id"] == update_data["profile_id"]

        self.db.expire_all()
        db_project = self.db.query(ProjectModel).filter_by(id=project.id).first()

        assert db_project.name == update_data["name"]
        assert db_project.profile_id == update_data["profile_id"]

    def test_update_nonexistent_404(self) -> None:
        update_data = {
            "name": "No Project",
            "profile_id": self.profiles[0].id
        }

        response = client.put(f"{route}/9999", json=update_data)
        assert response.status_code == 404

    def test_delete(self) -> None:
        project = self.projects[0]

        response = client.delete(f"{route}/{project.id}")

        assert response.status_code == 200

        db_project = self.db.query(ProjectModel).filter_by(id=project.id).first()
        assert db_project is None

    def test_delete_nonexistent_404(self) -> None:
        response = client.delete(f"{route}/9999")
        assert response.status_code == 404