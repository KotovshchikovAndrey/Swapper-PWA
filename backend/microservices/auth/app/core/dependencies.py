# dependencies settings
from utils.injector import injector


# TokenRepository
from database.repositories.token import TokenPostgreSQLRepository

injector.register("TokenRepository")(TokenPostgreSQLRepository)


# UserRepository
from database.repositories.user import UserPostgreSQLRepository

injector.register("UserRepository")(UserPostgreSQLRepository)


# TokenService
from services.token import TokenService

injector.register("TokenService")(TokenService)


# UserService
from services.user import UserService

injector.register("UserService")(UserService)
