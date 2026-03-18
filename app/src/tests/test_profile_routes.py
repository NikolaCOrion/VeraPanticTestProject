from sqlalchemy.orm import Session

from misc.database import SessionLocal

from models.models import Profile as ProfileModel

from repositories.profile_repository import create_profile

from tests.conf import client


route = "/api/v1/profiles"


def create_profiles(
        number_of_profiles: int, db: Session
) -> list[ProfileModel]:
    profiles: list[ProfileModel] = []

    for i in range(number_of_profiles):
        profile = ProfileModel(name=f"Profile {i + 1}",
                               age=25)
        created_profile = create_profile(db, profile)
        profiles.append(created_profile)

    return profiles


class TestProfiles:

    def setup_method(self) -> None:
        self.number_of_profiles = 3
        self.db = SessionLocal()
        self.profiles = create_profiles(self.number_of_profiles, self.db)

    def teardown_method(self) -> None:
        self.db.query(ProfileModel).delete()
        self.db.commit()

    def test_list_profiles(self) -> None:
        response = client.get(route)

        assert response.status_code == 200
        assert len(response.json()) == self.number_of_profiles

    def test_get_one(self) -> None:
        profile_id = self.profiles[0].id
        response = client.get(f"{route}/{profile_id}")
        assert response.status_code == 200
        data = response.json()
        assert data["id"] == profile_id
        assert data["name"] == self.profiles[0].name
        assert data["age"] == self.profiles[0].age

    def test_get_nonexistent_404(self) -> None:
        nonexistent_id = 9999
        response = client.get(f"{route}/{nonexistent_id}")
        assert response.status_code == 404

    def test_create(self) -> None:
        new_profile_data = {"name": "New Profile", "age": 30}
        response = client.post(route, json=new_profile_data)
        assert response.status_code == 201
        data = response.json()
        assert data["name"] == new_profile_data["name"]
        assert data["age"] == new_profile_data["age"]

        db_profile = self.db.query(ProfileModel).filter_by(id=data["id"]).first()
        assert db_profile is not None

    def test_update(self) -> None:
        profile_id = self.profiles[0].id
        update_data = {"name": "Updated Name", "age": 35}
        response = client.put(f"{route}/{profile_id}", json=update_data)
        assert response.status_code == 200
        data = response.json()
        assert data["name"] == update_data["name"]
        assert data["age"] == update_data["age"]

        self.db.expire_all()  # OVO
        db_profile = self.db.query(ProfileModel).filter_by(id=profile_id).first()
        assert db_profile.name == update_data["name"]
        assert db_profile.age == update_data["age"]

    def test_update_nonexistent_404(self) -> None:
        nonexistent_id = 9999
        update_data = {"name": "No One", "age": 50}
        response = client.put(f"{route}/{nonexistent_id}", json=update_data)
        assert response.status_code == 404

    def test_delete(self) -> None:
        profile_id = self.profiles[0].id
        response = client.delete(f"{route}/{profile_id}")
        assert response.status_code == 200  # successful delete

        db_profile = self.db.query(ProfileModel).filter_by(id=profile_id).first()
        assert db_profile is None

    def test_delete_nonexistent_404(self) -> None:
        nonexistent_id = 9999
        response = client.delete(f"{route}/{nonexistent_id}")
        assert response.status_code == 404
