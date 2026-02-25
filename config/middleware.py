from django.utils.deprecation import MiddlewareMixin
from account.models import BlockedIpAddress
from django.contrib.auth import get_user_model
User = get_user_model()

class GetUserIpsMiddleware(MiddlewareMixin):

    def process_request(self, request):
        ip = request.META.get('REMOTE_ADDR')
        print(ip)

        if request.user.is_authenticated:
            request.user.ips = []
            if ip not in request.user.ips:
                request.user.ips.append(ip)
                request.user.save()


class BlockUserMiddleware(MiddlewareMixin):
     
    def process_request(self, request):
        ip = request.META.get('REMOTE_ADDR')
        ip_addr = BlockedIpAddress.objects.filter(ip_address = ip)
        if ip_addr:
            raise PermissionError