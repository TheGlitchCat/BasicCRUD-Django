# Set up 

- python 3.6 
- psql 11

## Create venv
```
virtualenv venv
source venv/scripts/activate
```


## Install requirements
```
pip install -r requirements.txt
```

## DB Settings
```
DBname = students
username = postgres
password = admin1234
port = 5432
host = localhost
```

## Migrations
```
python manage.py makemigrations
python manage.py migrate
```

## URLS - Students

| URL | METHODS | PARAMS |
|:----|:-------:|:-----: |
| http://localhost:8000/api/v1/students/ | GET POST | name |
| http://localhost:8000/api/v1/student/create/ | POST | name| 
| http://localhost:8000/api/v1/student/pk/ | GET | |
| http://localhost:8000/api/v1/student/update/pk/ | PUT | name |
| http://localhost:8000/api/v1/student/delete/pk/ | DELETE | |
| http://localhost:8000/api/v1/students/?search=param | | name pk |
| http://localhost:8000/api/v1/students/?ordering=param | | name id |

## URLS - Professors

| URL | METHODS | PARAMS |
|:----|:-------:|:------:|
| http://localhost:8000/api/v1/professors/ | GET POST | name |
| http://localhost:8000/api/v1/professor/create/ | POST | name |
| http://localhost:8000/api/v1/professor/pk/ | GET | |
| http://localhost:8000/api/v1/professor/update/pk/ | PUT | name | 
| http://localhost:8000/api/v1/professor/delete/pk/ | DELETE | |
| http://localhost:8000/api/v1/professors/?search=param | | name pk |
| http://localhost:8000/api/v1/professors/?ordering=param | | name id |


## URLS - Scores

| URL | METHODS | PARAMS |
|:----|:-------:|:------:|
| http://localhost:8000/api/v1/scores/ | GET POST | name student professor value |
| http://localhost:8000/api/v1/score/create/ | POST | name student professor value | 
| http://localhost:8000/api/v1/score/pk/ | GET | |
| http://localhost:8000/api/v1/score/update/pk/ | PUT | name student professor value |
| http://localhost:8000/api/v1/score/delete/pk/ | DELETE | |
| http://localhost:8000/api/v1/scores/?search=param | | name pk student__id student__name professor__id professor__name value |
| http://localhost:8000/api/v1/scores/?ordering=param | | name pk student__id student__name professor__id professor__name value |

