from starlette.routing import Route

from api.api_v1 import controllers

routes = [
    Route("/registration", controllers.Registration),
    Route("/login", controllers.Login),
    Route("/refresh", controllers.Refresh),
    Route("/logout", controllers.Logout),
]
