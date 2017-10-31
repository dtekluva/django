import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django
django.setup()

from rango.models import Category, Page


def populate():
    python_cat = add_cat('python frameworks',"13","34")

    add_page(cat=python_cat,
        title="Official Python Tutorial",
        url="http://docs.python.org/2/tutorial/")

    add_page(cat=python_cat,
        title="How to Think like a Computer Scientist",
        url="http://www.greenteapress.com/thinkpython/")

    add_page(cat=python_cat,
        title="Learn Python in 10 Minutes",
        url="http://www.korokithakis.net/tutorials/python/")

    django_cat = add_cat("Tango with django","122","21")

    add_page(cat=django_cat,
        title="learn to tango with django",
        url="http://www.tangowithdjango.com/book17/chapters/models_templates.html#modifying-the-index-view")

    add_page(cat=django_cat,
        title="Django Rocks",
        url="http://www.djangorocks.com/")

    add_page(cat=django_cat,
        title="Product design",
        url="http://zeplin.com")

    frame_cat = add_cat("Just watch videos","100","56")

    add_page(cat=frame_cat,
        title="Bottle",
        url="http://youtube.com")

    add_page(cat=frame_cat,
        title="Flask",
        url="http://flask.pocoo.org")

    # Print out what we have added to the user.
    for c in Category.objects.all():
        for p in Page.objects.filter(Category=c):
            print ("- {0} - {1}".format(str(c), str(p)))

def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(Category=cat, title=title)[0]
    p.url=url
    p.views=views
    p.save()
    return p

def add_cat(name,views,likes):
    c = Category.objects.get_or_create(name=name,views=views,likes=likes)[0]

    return c

# Start execution here!
if __name__ == '__main__':
    print ("Starting Rango population script...")
    populate()