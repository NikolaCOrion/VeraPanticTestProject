### TEST ###


## Migrations
`docker compose run api alembic revision --autogenerate -m "Initial migration"` <br />
`docker compose run api alembic upgrade head`


## Unit tests
`docker compose run -e TESTING=True -e DATABASE_URL=postgresql://user:password@db:5432/testing api python -m pytest -s tests --disable-warnings`