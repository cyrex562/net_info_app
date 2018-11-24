from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register('services', ServiceViewSet)
router.register('addresses', NetworkAddressViewSet)
router.register('interfaces', InterfaceViewSet)
router.register('systems', SystemViewSet)

urlpatterns = [
    path('', default_view),
    path('api/', include(router.urls)),
    # services
    path('services/', ServiceListView.as_view()),
    path('services/<int:pk>', ServiceDetailView.as_view()),
    path('services/create/', ServiceCreateView.as_view()),
    # interfaces
    path('interfaces/', InterfaceListView.as_view()),
    path('interfaces/<int:pk>', InterfaceDetailView.as_view()),
    path('interfaces/create/', InterfaceCreateView.as_view()),
    # addresses
    path('addresses/', NetworkAddressListView.as_view()),
    path('addresses/<int:pk>', NetworkAddressDetailView.as_view()),
    path('addresses/create/', NetworkAddressCreateView.as_view()),
    # systems
    path('systems/', SystemListView.as_view()),
    path('systems/<int:pk>', SystemDetailView.as_view()),
    path('systems/create/', SystemCreateView.as_view())
]
