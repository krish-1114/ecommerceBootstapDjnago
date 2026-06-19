from .models import Category

def menu_links(request):
    links = Category.objects.all()
    print("Links:", links)
    return {'links': links}