# django-Auth

# /oauth POST request
- It sends the user TOKEN, if the user is valid.
curl -X POST \
  http://localhost:8000/oauth/ \
  -H 'cache-control: no-cache' \
  -H 'content-type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW' \
  -F email=w@q.wq \
  -F password=123

  This returns you the JWT Token
  ex:



  # /home GET request
  - It sends token received by '/oauth' inside headers authorization.
  curl -X GET \
  http://localhost:8000/home \
  -H 'authorization: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MTgsImVtYWlsIjoid0BxLndxIn0.f9_nC7KDY-PBFPyTkzYFw9ReuVDE6MOXnRNY_NQj3Z8' \
  -H 'cache-control: no-cache'
