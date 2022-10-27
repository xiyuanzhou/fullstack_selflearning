# [_Fullstack_Course_]() 🤯
![GitHub language count](https://img.shields.io/github/languages/count/xiyuanzhou/fullstack_selflearning) ![Bitbucket open issues](https://img.shields.io/bitbucket/issues/xiyuanzhou/fullstack_selflearning) ![GitHub repo size](https://img.shields.io/github/repo-size/xiyuanzhou/fullstack_selflearning) ![GitHub last commit](https://img.shields.io/github/last-commit/xiyuanzhou/fullstack_selflearning)

> `Author: Xiyuan(Lucas) Z`

***

```diff
+ Django 4
+ Python3 
+ Bootstrap v5

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

## *Django-Model, Database and Queries*
- 