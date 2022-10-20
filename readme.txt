$Check if python downloaded |||
python3
---------------------------------------------------------------------------------
$Otherwise |||
sudo pip install python3
---------------------------------------------------------------------------------
$Next |||
sudo pip install virtualenv
virtualenv (thanos) ---> you create your own folder name
cd (thanos)
---------------------------------------------------------------------------------
$After that, go into project active |||
source bin/activate
---------------------------------------------------------------------------------
$Install Django |||
sudo pip install django  ---> any version you want ex. ...django==3.0.1
python -m django --version  ---> check if installed and version
---------------------------------------------------------------------------------
$Creat startup project ||| 
django-admin startproject (thanosback) ---> project folder name your own
cd (thanosback)
python manage.py runserver ---> manage.py if auto create py files 
---------------------------------------------------------------------------------
localhost:8000

python manage.py startapp (first_app) ---> your own file name

\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
python manage.py migrate

python manage.py makemigrations accounts (just example)

python manage.py migrate (checking)
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

python manage.py createsuperuser (to create django account for manage the program)


----------------------------------------------------------------------------------------
Github and Git (Linking repo) steps:

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

$ security find-internet-password -l github.com


$ security delete-internet-password -l github.com


