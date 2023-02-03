from starlette.routing import Route

from dao.api.api_v1 import controllers

routes = [
    Route("/registration", controllers.Registration),
    Route("/login", controllers.Login),
    Route("/refresh", controllers.RefreshToken),
    Route("/logout", controllers.Logout),
]
