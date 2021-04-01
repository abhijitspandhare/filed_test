from rest_framework import routers
from . import views 

router = routers.DefaultRouter()
router.register(r'song', views.SongViewset)
router.register(r'podcast',views.PodcastViewset)
router.register(r'audiobook', views.AudiobookViewset)