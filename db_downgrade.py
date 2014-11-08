from migrate.versioning import api
from config import SQLALCHEMY_DATABASE_URI
from config import SQLALCHEMY_DATABASE_REPO


v = api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_DATABASE_REPO)
api.downgrade(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_DATABASE_REPO, v - 1)
v = api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_DATABASE_REPO)
print('Current database version: ' + str(v))
