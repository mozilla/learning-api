## API server for learning.mozilla.org site

### How to run the server

#### Prerequisite

1. Git
2. Python 3

#### Install

1. Install dependencies

```
$ pip install -r requirements.txt
```

2. Copy `.env`
```
cp env.sample .env
```

3. Run the migration script
```
$ python app/manage.py migrate
```

#### Run the server

```
$ python app/manage.py runserver
```

#### Environment variables
This app should work out of the box, unless you want to override some of the env which can be found in `.env` file.

