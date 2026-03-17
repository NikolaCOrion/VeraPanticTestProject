from repositories import profile_repository


def list_profiles(db):
    return profile_repository.list_profiles(db)

def get_profile(db, profile_id):
    return profile_repository.get_profile(db, profile_id)

def create_profile(db, profile):
    return profile_repository.create_profile(db, profile)


def update_profile(db, profile_id, profile):
    return profile_repository.update_profile(db, profile_id, profile)


def delete_profile(db, profile_id):
    return profile_repository.delete_profile(db, profile_id)