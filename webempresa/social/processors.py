from .models import Link

def ctx_dict(request):
    ctx = {}
    links = Link.objects.all()
    for link in links:
        ctx[link.key] = link.url
    #sidebars = SideBar.objects.all()
    #ctx['sidebars'] = sidebars
    return ctx