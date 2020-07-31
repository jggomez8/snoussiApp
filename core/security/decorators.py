from django.http import HttpResponseRedirect

from config import settings
from core.security.models import Module


def access_module(f):
    def access(*args, **kwargs):
        request = args[0]
        try:
            request.user.set_group_session()
            id = request.user.get_group_id_session()
            url_absolute = get_absolute_path(id, request.path)
            request.session['path'] = request.path
            modules = Module.objects.filter(groupmodule__groups_id__in=[id], is_active=True, url=url_absolute,
                                            is_visible=True)
            if modules.exists():
                if modules.filter(type_id__isnull=True).exists():
                    request.session['module'] = modules[0]
                    return f(request)
                elif modules.filter(type__is_active=True).exists():
                    request.session['module'] = modules[0]
                    return f(request)
        except:
            pass
        return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)

    return access


def get_absolute_path(id, url):
    search = Module.objects.filter(groupmodule__groups_id=id, is_active=True, is_visible=True)
    for m in search:
        if url == m.url:
            return m.url
    for m in search:
        if url.__contains__(m.url):
            return m.url
    return ''
