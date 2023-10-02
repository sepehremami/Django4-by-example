# Django 4 by example

hi everyone! this code repository is the exact copy of the codes found in chapter 3 to 5 of the book Django 4 by example! 
(oh maybe exept the docker configuration.)

### here is how you can run this project

#### do this with docker compose

- `docker-compose up`

#### If you use Docker

-  in the root of the project type:<br/>
> `docker build -t django4 .`<br/>
-  and then<br/>
> `docker run -p 127.0.0.1:8000:8000 django4`<br/>

#### otherwise you can

- `pip install -r requirements.txt`
- `python manage.py makemigrations`
- `python manage.py migrate`
- `python manage.py runserver`

do the instructions in order they are presented to you and you must be good to do! 
>> Note: be careful to set the right environment variables in settings.py before running the project.
