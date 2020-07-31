from crum import get_current_request
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator

from core.security.decorators import access_module, get_absolute_path


class AccessModuleMixin(object):

    @method_decorator(login_required)
    @method_decorator(access_module)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class PermissionModuleMixin(object):
    permission_required = None

    def verify_permission(self):
        try:
            request = get_current_request()
            group_id = request.user.get_group_id_session()
            return Group.objects.get(pk=group_id).permissions.filter(codename=self.permission_required).exists()
        except:
            return False

    def dispatch(self, request, *args, **kwargs):
        if not self.verify_permission():
            messages.error(request, 'No tiene permisos para utilizar esta opción')
            group_id = request.user.get_group_id_session()
            url_absolute = get_absolute_path(group_id, request.path)
            return HttpResponseRedirect(url_absolute)
        return super().dispatch(request, *args, **kwargs)
