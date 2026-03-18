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
        # TODO
        pass

    def test_get_nonexistent_401(self) -> None:
        # TODO
        pass

    def test_create(self) -> None:
        # TODO
        pass

    def test_update(self) -> None:
        # TODO
        pass

    def test_update_nonexistent_401(self) -> None:
        # TODO
        pass

    def test_delete(self) -> None:
        # TODO
        pass

    def test_delete_nonexistent_401(self) -> None:
        # TODO
        pass
