from django.shortcuts import render



# Create your views here.
from django.views import generic
from rest_framework import viewsets

from .models import *
from .serializers import *


# REST API Views
class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class NetworkAddressViewSet(viewsets.ModelViewSet):
    queryset = NetworkAddress.objects.all()
    serializer_class = NetworkAddressSerializer


class InterfaceViewSet(viewsets.ModelViewSet):
    queryset = Interface.objects.all()
    serializer_class = InterfaceSerializer


class SystemViewSet(viewsets.ModelViewSet):
    queryset = System.objects.all()
    serializer_class = SystemSerializer


# interface
class InterfaceListView(generic.ListView):
    model = Interface
    template_name = "webway/interface_list.html"
    context_object_name = "interfaces"


class InterfaceDetailView(generic.DetailView):
    model = Interface
    template_name = "webway/interface_detail.html"
    context_object_name = "interface"


class InterfaceCreateView(generic.CreateView):
    model = Interface
    fields = ["name", "addresses"]
    template_name = "webway/interface_create.html"
    success_url = "/interfaces/"


# services
class ServiceListView(generic.ListView):
    model = Service
    template_name = "webway/service_list.html"
    context_object_name = "services"


class ServiceDetailView(generic.DetailView):
    model = Service
    template_name = "webway/service_detail.html"
    context_object_name = "service"


class ServiceCreateView(generic.CreateView):
    model = Service
    fields = ["name", "protocol", "port", "description", "bind_addr"]
    template_name = "webway/service_create.html"
    success_url = "/services/"


# network addresses
class NetworkAddressListView(generic.ListView):
    model = NetworkAddress
    template_name = "webway/address_list.html"
    context_object_name = "addresses"


class NetworkAddressDetailView(generic.DetailView):
    model = NetworkAddress
    template_name = "webway/address_detail.html"
    context_object_name = "address"


class NetworkAddressCreateView(generic.CreateView):
    model = NetworkAddress
    fields = ["value", "type"]
    template_name = "webway/address_create.html"
    success_url = "/addresses/"


# systems
class SystemListView(generic.ListView):
    model = System
    template_name = "webway/system_list.html"
    context_object_name = "systems"


class SystemDetailView(generic.DetailView):
    model = System
    template_name = "webway/system_detail.html"
    context_object_name = "system"


class SystemCreateView(generic.CreateView):
    model = System
    fields = ["hostname", "services", "interfaces", "description", "nickname"]
    template_name = "webway/system_create.html"
    success_url = "/systems/"


def default_view(request):
    return render(request, "webway/index.html")




