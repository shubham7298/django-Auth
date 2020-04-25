   # django-Auth Cookbook
 #### Ingridients:
 You can find it in
 > requirements.txt

### Recipe
 ------------
 To the terminal:
```sh
git clone https://github.com/shubham7298/django-Auth.git
cd django-Auth
```
To install without a virtual environment.
```sh
pip install -r requirements.txt
```
For virtual environment install $pipenv
```sh
pip install --user pipenv
pipenv install -r requirements.txt
pipenv shell
```

## Stir
 ------------
 To run django application.
```sh
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
Navigate to your server address in your preferred browser
```sh
http://localhost:8000/
```

> Add your sql database credentials in settings.py as per your taste.

### Taste
To test the application, run:
```sh
coverage run manage.py test
```

### Features
* ##### /register/
    - POST method
    - Creates an entry in Auth_userinfo table in mydb database
    -  Parameters
        - name
        - email
        - password
        - id (auto-increment in db)
        
    - curl request example-
    ```sh
    curl -X POST \
  http://localhost:8000/register/ \
  -H 'cache-control: no-cache' \
  -H 'content-type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW' \
  -F name=Random_guy \
  -F email=some@mail.com \
  -F password=lol
  ```

* ##### /oauth/
    - POST method
    - Checks for valid data in Auth_userinfo table in mydb database
    -  Parameters
        - email
        - password
    
    - curl request example-
    ```sh
    curl -X POST \
    http://localhost:8000/oauth/ \
    -H 'cache-control: no-cache' \
    -H 'content-type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW' \
    -F email=some@mail.com \
    -F password=lol
    ```
    - returns JWT Token
    ```sh
    {
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MjAsImVtYWlsIjoic29tZUBtYWlsLmNvbSJ9.Sg1tGyeG_1k0iE0tPFfbgRYXgNrqnPSCLbCeQE1qddQ"
    }
    ```

* ##### /home/
    - GET method
    - Checks for valid token and then authorizes user
    -  Header
        - JWTtoken
    
    - curl request example-
    ```sh
    curl -X GET \
  http://localhost:8000/home \
  -H 'authorization: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MjAsImVtYWlsIjoic29tZUBtYWlsLmNvbSJ9.Sg1tGyeG_1k0iE0tPFfbgRYXgNrqnPSCLbCeQE1qddQ' \
  -H 'cache-control: no-cache'
    ```
    - returns name of the user
    ```sh
    {
      name:'Random_guy'
  }
    ```

    Made with :heart:  during Lockdown :stuck_out_tongue_closed_eyes: 
   