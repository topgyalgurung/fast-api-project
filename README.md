
FAST API: 
https://fastapi.tiangolo.com/tutorial/ 

- $ cd fastapi-project
- $ python3 -m venv venv
- $ source venv/bin/activate 
- $ pip install "fastapi[standard]"
- run live server 
  - $  fastapi dev main.py

Benefits of Fast API
- its just plain python
- built in async 
- built in data validation with pydantic 
- fast api is typed python 
- errors are in json (flask show in html )
- authentication built in: supports http basic Oauth2 tokens(jwt token) and header api keys
- swagger ui built in: http://127.0.0.1:8000/docs. useful if frontend dev need access to data, demo to stakeholder, UI to represent api etc
    -  http://127.0.0.1:8000/redoc