from repositories import profile_repository


def list_profiles(db):
    return profile_repository.list_profiles(db)
