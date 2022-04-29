from rest_framework.routers import DefaultRouter
#from backend_task_2.backend.mortgage import views
from mortgage import views

router = DefaultRouter()
router.register('offer', views.OfferViewSet, basename='offer')



