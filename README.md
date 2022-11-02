# [_Fullstack_Course_]() 🤯
![GitHub language count](https://img.shields.io/github/languages/count/xiyuanzhou/fullstack_selflearning) ![Bitbucket open issues](https://img.shields.io/bitbucket/issues/xiyuanzhou/fullstack_selflearning) ![GitHub repo size](https://img.shields.io/github/repo-size/xiyuanzhou/fullstack_selflearning) ![GitHub last commit](https://img.shields.io/github/last-commit/xiyuanzhou/fullstack_selflearning)

> `Author: Xiyuan(Lucas) Z`

***

```diff
+ Django 4
+ Python3 
+ Bootstrap v5

- SQLite
- HTML 5
- CSS
```

## ~~*HTML5 version learning*~~ 
- Basic html ✅
- List html ✅
- Div and Spans ✅
- Attributes(img...) ✅
- Tables ✅
- Forms ✅
> `done` 🐵

## ~~*CSS*~~
- Basic Css ✅
- Common Style ✅
- Selector ✅
- Fonts ✅
- Box ✅
> `done` 🐵

## *~~Bootstrap~~ (practice)*
> `bootstrap@5.2.2`

```diff
! Options install: 
```

$ npm install bootstrap@5.2.2

$ gem install bootstrap -v 5.2.2

```diff
! Link Bootstrap to HTML
```

```html
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-Zenh87qX5JnK2Jl0vWa8Ck2rdkQ2Bzep5IDxbcnCeuOxjzrPF/et3URy9Bv1WTRi" crossorigin="anonymous">
```

> `Using bootstrap forms and style for Django APP (Future)` -> `done` 🐵 

## ~~*Python3*~~ *(Skip)*
***(Python Learned)***

$ python3 --version

$ sudo apt install python3.9
```python
'''
comment a lot
'''

#single comment
print('Hello World')

def Foo(self, bar):
    self.bar = bar

list1 = [1,23,4]
dict1 = {1:'2',2:'3'}
tuple1 = ('hello', 2.343,1000, [1,2,3,4])
```

> `Move on` -> `done` 🐵

## ~~*Django Framework*~~ ##

```diff
- Please check out the readme.txt for (Django environment) Installation
```
> ~~Required Python3~~

> ~~Required ternimal access(will be best)~~

> ~~Required install Django4~~

> ~~Required install virtualenv~~

> *Check Python and Django Version below*
```diff
+ python -m django --version
```

```html
<br>
```

- Django project created ✅
- Django first application created ✅

> `done` 🐵

## ~~*Django (Views, Routing, URLS)*~~ 
$ python manage.py startapp (your file name)

```python
'''
important information announce 
'''
import os
TEMPLATES_DIR = os.path.join(BASE_DIR,'templates')

```
- Basic URLS ✅
- Basic views (linking) ✅
- Templates created ✅

> `done` 🐵

## ~~*Django-Templates*~~
> important notes

$ python manange.py migrate

$ python manange.py makemigrations my_app

```python
"my_app.apps.MyAppConfig"
```

- Templates Directories ✅
- Passing simple variables ✅
```python
    my_var ={
        'first_name' : 'lucas',
        'last_name' : 'juesi',
        'some_list' : [1,2,3,4,4],
        'some_dict' : {'insidekey': 'inside_value'}
    }
    
    return render(request, 'my_app/variables.html', context=my_var)
```
```html
<p>{{ first_name }}</p>
<p>{{ some_list.0 }}</p>
<p>{{ some_dict.insidekey }}</p>
```
- Django Filter ✅

[_Built-in template tags and filters_](https://docs.djangoproject.com/en/4.1/ref/templates/builtins/) (click to see)

- Django For Loop ✅
> notes
```django
{% for item in some_list %}
    <p>{{ item }}</p>
{% endfor %}

{% for key, value in some_dict.items %}
    <li>{{ key }} </li>
    <li>{{ value | capfirst }} </li>
{% endfor %}
```
- Django If, Elif, Else ✅
> notes
```django
{% if count == 0 %}
    <p>yes</p>
{% endif %}
```
- Tags and Url name in templates ✅
> Register the app namespace in urls.py
```python
    #my_app is your app folder name
    app_name = 'my_app'

    #example
    urlpatterns =[
    path('example/', views.example_view, name='example'),
    path('var/', views.variables, name='variables'),
    ]
```
> How to use
```html
    <p>Example</p>
    <h1><a href="{% url 'my_app:example'  %}">Click me</a></h1>
```
- Templates Inheritance ✅
> Note need add a templates path into setting
```python
    TEMPLATE_DIR = os.path.join(BASE_DIR,'templates')
```
```html
{% extends 'base.html' %}
{% block  content %}
    <p>Welcome again</p>
    <a href="{% url 'my_app:variables' %}"> Click me</a>
{% endblock  %}
```
- ~~Custom Error 404 html~~ ✅
> Pass
- Static Files ✅
> notes
```html
    <img src ="{% static 'my_app/IMG_6019.jpeg' %}" alt='no image found'> 
```
> `done` 🐵

## ~~*Django-Model, Database and Queries*~~
- Database Migrations ✅
> Add the app into setting INSTALLED_APP
> https://docs.djangoproject.com/en/4.1/ref/databases/

    $ python manage.py migrate
    $ python manage.py makemirgrations office (apps)
    $ python manage.py migrate 
- Creating and Insert ✅
> runing on shell/terminal python

    $ python manage.py shell
```python
    from office,models import Patient

    #create first object
    p1 = Patient(first_name='carl',last_name='kit', age = 30)
    #shortcut create
    Patient.objects.create(first_name='lucas',last_name='kit', age = 45)
    mylist=[Patient(first_name='jack',last_name='zhu', age=22), Patient(first_name='lucas',last_name='zhou',age=12)]
    '''
    Access Objects
    p1.age
    p1.last_name
    '''
    #save object
    p1.save()
    #see all objects
    Patient.objects.all() #Patient.objects.all()[0]
    Patient.objects.bulk_create(mylist)
```
- Filter and Get ✅
> Notes (options)

$ python manage.py shell
```python
    #import the models first
    from office.models import Patient
    #import Q (for look up)
    from django.db.models import Q

    #without Q oprand
    Patient.objects.filter(last_name='kit').filter(age=22).all()

    Patient.objects.filter(Q(last_name='kit') & Q(age=22)).all()
```
- Field Lookups ✅
> Notes -> [_Field lookups_](https://docs.djangoproject.com/en/4.1/ref/models/querysets/#id4)
```python
    Patient.objects.filter(last_name__startswith='k').all()
    Patient.objects.filter(age__in=[10,20,40,22]).all()
    #gte stands for (greater than equal to) 
    Patient.objects.filter(age__gte= 22).all()

    Patient.objects.order_by('age').all()
    Patient.objects.order_by('last_name').all()
```
- Updating Models ✅
> Notes
```python
'''
If want to updated new data field in existing models
'''
    # Set a default value and it can updated data later
    heartrate = models.IntegerField(default=70,validators=[MinValueValidator(60), MaxValueValidator(150)])

    #and validators field
    from django.core.validators import MaxValueValidator, MinValueValidator
    
    age = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(150)])
```
>After updating the models field (start migrations)

$ python manage.py makemigrations office 

$ python manage.py migrate

- Updating Entries ✅
> Notes
```python
'''
It can write in different way
'''
#example
    #assign the data first
    first = Patient.objects.all()[0]
    first = Patient.objects.get(pk=1) #primary key
    first.heartrate = 90
    first.save()
```
- Deleting Entries ✅
> Notes -> just call delete()
```python
#example
    #assign the data first
    first = Patient.objects.get(pk=1) #primary key
    first.delete()
```
- Connecting Templates and Database Models ✅
> Notes
```python
    from office import models

    all_patient = models.Patient.objects.all()
    context = {'patient': all_patient}
```
> HTML
```html
    {% for i in patient %}
        <tr>
            <td>{{ i.first_name }}</td>
            <td>{{ i.last_name }}</td>
            <td>{{ i.age }} </td>
            <td>{{ i.heartrate }}</td>
        </tr>
    {% endfor %}
```
> `done` 🐵 (next session)
## ~~*Django Admin*~~
- Model and Website P1 ✅
> Notes (using boostrap)
```html
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-Zenh87qX5JnK2Jl0vWa8Ck2rdkQ2Bzep5IDxbcnCeuOxjzrPF/et3URy9Bv1WTRi" crossorigin="anonymous">
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-OERcA2EqjJCMA+/3y+gxIOqMEjwtxJY7qPCqsdltbNJuaOe923+mo//f6V8Qbsw3" crossorigin="anonymous"></script>

        <li><a class="dropdown-item" href="{% url 'cars:list' %}">List</a></li>
        <li><a class="dropdown-item" href="{% url 'cars:add' %}">Add</a></li>
        <li><a class="dropdown-item" href="{% url 'cars:delete' %}">Delete</a></li>
```
- Model and Website P2 ✅
> Important Notes
```python
    '''
    when access the website from inside the app tempates
    please using ex. 
    {% url 'cars:list' %}
    {% url 'cars:add' %}
    {% url 'cars:delete' %}
    '''
    app_name = "cars"
    urlpatterns = [
        path('list/', views.list, name='list'),
        path('add/', views.add, name='add'),
        path('delete/', views.delete, name='delete'),]
    #cars:list -> 'list' is from the name NOT NOT class object name
```
> Taking information form HTML
```html
    <form action="" method="POST">
        {% csrf_token %}
    </form>
```
```python
def add(request):
    #print(request.POST)
    if request.POST:
        brand = request.POST['brand']
        year = int(request.POST['year'])

        models.cars.objects.create(brand=brand,year=year)
        return redirect(reverse('cars:list'))
    else:
        return render(request, "cars/add.html")

def delete(request):
    if request.POST:
        brand = request.POST['brand']
        year = int(request.POST['year'])

        if models.cars.objects.filter(Q(brand=brand) & Q(year=year)).all():
            temp1 = models.cars.objects.filter(Q(brand=brand) & Q(year=year)).all()[0]
            #print(temp1)
            temp1.delete()
            return redirect(reverse('cars:list'))
    else:
        return render(request, "cars/delete.html")
```
- Django Administration and Models ✅
> notes (create super user) check to see if interest custom own admin site.
[_custom_admin_site_](https://docs.djangoproject.com/en/4.1/ref/contrib/admin/)

$ python manange.py createsuperuser
```python
    '''
    Go to admin.py (edit)
    register the model int admin site
    '''
    admin.site.register(cars)
```
> `done` 🐵
## *Django Forms* ##
- Django Form Class basic ✅
> notes (Optional) (Simple forms) only need to know the concept
```python
from django import forms

    if request.POST:
        form = ReviewForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return redirect(reverse('computers:thank_you'))
    else:
        form = ReviewForm()
    return render(request, 'computers/computerinfo.html',context={'form': form})

    class ReviewForm(forms.Form):
        first_name = forms.CharField(label='First name', max_length=100)
        last_name = forms.CharField(label='Last name', max_length=100)
        email = forms.EmailField(label='email')
        review = forms.CharField(label='write your review here')
```
- Widgets and Styling


- Model Forms & Customization
> model form is what we need (similar to simple forms)
