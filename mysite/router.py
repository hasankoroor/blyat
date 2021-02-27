from rest_framework import routers
from polls.api.viewsets import *
router = routers.DefaultRouter()
router.register(r"profile",myfirstViewset, basename="kossher")
router.register(r"signup",SignupViewset, basename="kossher")