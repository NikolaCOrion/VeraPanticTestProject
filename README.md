### TEST ###


## Migrations
`docker compose run api alembic revision --autogenerate -m "Initial migration"` <br />
`docker compose run api alembic upgrade head`