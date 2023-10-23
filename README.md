# calorieTracker-REST-APIs

## Screenshots

<img width="960" alt="api-1" src="https://github.com/Suryanshm000/calorieTracker-REST-APIs/assets/65828169/a4d96223-b5d2-4c6a-ac1d-05b253f3c295">

<img width="960" alt="api-2" src="https://github.com/Suryanshm000/calorieTracker-REST-APIs/assets/65828169/d9ce6b75-7a61-49ec-8b1f-d4258914628c">

<br>

## API Reference

**Signup API**

```
curl --location --request POST 'http://127.0.0.1:8000/user/create' \
--form 'username="<username>"' \
--form 'password="<password>"' \
--form 'email="<email>"'
```

**Login API**
```
curl --location --request POST 'http://127.0.0.1:8000/user/login' \
--form 'username="<username>"' \
--form 'password="<password>"'
```

**User setting API**
```
curl --location --request POST 'http://127.0.0.1:8000/user/set_calorie' \
--header 'Authorization: Token <YOUR ACCESS TOKEN>' \
--form 'expected_calories_per_day="<value>"'
```

**Create calorie entry API**
```
curl --location --request POST 'http://127.0.0.1:8000/user/entry' \
--header 'Authorization: Token <YOUR ACCESS TOKEN>' \
--form 'text="<meal>"' \
--form 'calories="<value>"'
```

**Get entry list API**
```
curl --location --request GET 'http://127.0.0.1:8000/user/view_entry' \
--header 'Authorization: Token d9a6b3d949448ed1b0bef79328eba00e2dcd30e9'
```

**Get entry API**
```
curl --location --request GET 'http://127.0.0.1:8000/user/entry/<id>' \
--header 'Authorization: Token <YOUR ACCESS TOKEN>'
```

**Delete entry API**
```
curl --location --request DELETE 'http://127.0.0.1:8000/user/entry/<id>' \
--header 'Authorization: Token <YOUR ACCESS TOKEN>'
```

**Update entry API**
```
curl --location --request PUT 'http://127.0.0.1:8000/user/entry_update/<id>' \
--header 'Authorization: Token <YOUR ACCESS TOKEN>' \
--form 'text="<meal>"' \
--form 'calories="<value>"'
```

**Set Usermanager API**
```
curl --location --request PUT 'http://127.0.0.1:8000/user/set_usermanager/4' \
--header 'Authorization: Token <YOUR ACCESS TOKEN>' \
--form 'is_staff="1"'
```

**User List API**
```
curl --location --request GET 'http://127.0.0.1:8000/users' \
--header 'Authorization: Token <YOUR ACCESS TOKEN>'
```

**User detail API**
```
curl --location --request GET 'http://127.0.0.1:8000/user/<id>' \
--header 'Authorization: Token <YOUR ACCESS TOKEN>'
```

**User delete API**
```
curl --location --request DELETE 'http://127.0.0.1:8000/user/<id>' \
--header 'Authorization: Token <YOUR ACCESS TOKEN>'
```

**User update API**
```
curl --location --request PUT 'http://127.0.0.1:8000/user/update/<id>' \
--header 'Authorization: Token <YOUR ACCESS TOKEN>' \
--form 'username="<username>"' \
--form 'password="<password>"' \
--form 'email="<email>"'
```

### User credentials

username: testuser1

password: testpassword

### Usermanager credentials

username: testuser

password: testpassword

### Admin credentials

username: testadmin

password: test

<br>

# Running at localhost

These are the steps to follow in order to run the project on local host: 
<br>

```
git clone https://github.com/Suryanshm000/calorieTracker-REST-APIs.git`
```

```
cd calorieTracker-REST-APIs
```

Virtual Environment setup
```
pip install virtualenv
python -m venv <name of environment>
cd <name of environment>/Scripts
activate
pip install -r requirements.txt
cd ..
cd ..
```

The *django api server* is started via the following command.

```
python manage.py runserver
```

<br>

# Command to run the test suite
```
python manage.py test
```


