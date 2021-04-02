# auto-ambient-music
small system for linux ambient music automation

## Install
you will need the poetry installed in you system

clone repo

```
poetry install
poetry shell
python manage.py migrate
python manage.py createsuperuser

```

## Usage
Start server or create service to autorun in you system.

```
python manage.py runserver 0.0.0.0:8008 --noreload --insecure
```

access in you browser:
http://localhost:8008

insert the user and password created previously.

in interface create a music, adding a youtube link, in time, create a time configuration for player.

enjoy! 