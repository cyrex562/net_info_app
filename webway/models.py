from django.db import models


# Create your models here.
# class Protocol(models.Model):
#     name = models.CharField(max_length=255)
#     port = models.SmallIntegerField(blank=True)
#
#     def __str__(self):
#         return "id: {}, name: {}, port: {}".format(
#             self.id,
#             self.name,
#             self.port
#         )


class NetworkAddress(models.Model):
    # address types
    IPV4_ADDR = "IPV4"
    IPV6_ADDR = "IPV6"
    MAC_ADDR = "MAC"
    SSID_ADDR = "SSID"
    ADDR_TYPE_CHOICES = (
        (IPV4_ADDR, "IPv4 Address"),
        (IPV6_ADDR, "IPv6 Address"),
        (MAC_ADDR, "MAC Address")
    )

    value = models.CharField(max_length=1024)
    type = models.CharField(choices=ADDR_TYPE_CHOICES,
                            max_length=255,
                            default=IPV4_ADDR)

    def __str__(self):
        return "id: {}, value: {}, type: {}".format(self.id, self.value,
                                                    self.type)


class Service(models.Model):
    name = models.CharField(max_length=255)
    # protocols
    TCP = "TCP"
    UDP = "UDP"
    ETHER = "ETH"
    PROTO_CHOICES = (
        (TCP, "TCP"),
        (UDP, "UDP"),
        (ETHER, "Ethernet")
    )
    # protocol = models.ForeignKey(Protocol, on_delete=models.CASCADE)
    protocol = models.CharField(choices=PROTO_CHOICES,
                                max_length=255,
                                default=TCP)
    port = models.SmallIntegerField(blank=True, null=True)
    description = models.TextField(blank=True)
    bind_addr = models.ForeignKey(NetworkAddress, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return "id: {}, name: {}, protocol: {}, port: {}, description: {}, bind addr: {}".format(
            self.id,
            self.name,
            self.protocol,
        self.port,
        self.description,
        self.bind_addr)


class Interface(models.Model):
    name = models.CharField(max_length=255)
    addresses = models.ManyToManyField(NetworkAddress)

    def __str__(self):
        return "id: {}, name: {}, addresses: {}".format(
            self.id,
            self.name,
            self.addresses)


class System(models.Model):
    hostname = models.CharField(max_length=512)
    services = models.ManyToManyField(Service)
    interfaces = models.ManyToManyField(Interface)
    description = models.TextField(blank=True)
    nickname = models.CharField(max_length=512, blank=True)

    def __str__(self):
        return "id: {}, hostname: {}, nickname: {}, interfaces: {}, services: {}, description: {}".format(
            self.id, self.hostname, self.nickname, self.interfaces,
            self.services)
