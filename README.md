# Grupo Boticário API Test


# Introduction
This Test API was created to solve a fake business rule. 

CreatedBy: Douglas Buss Ronchi <br>
CreationDate: 2023/03 <br>
CreaterEmail: douglasronchi02@hotmail.com<br>
Credits: Douglas Buss Ronchi<br>

# Getting Started
### 1. Installation process

- Clone this repo
- Run ```pip install -r requirements/dev.txt``` command
- Create a ```.env``` file with the environment variables like ```.env.example```
- Run ```docker-compose up -d``` command
- Start ```run.py``` file.
- It runs an uvicorn server at ```127.0.0.1:8000```
- Acess the docs from ```127.0.0.1:8000/docs```
- To generate a valid token use the method in: ```app/utils/authentication.generate_token()```

### 2. Software dependencies
   - MongoDB

### 3. Latest releases
- v1.0.0 - First Release

### 4. API references
- FastAPI

# Build and Test
To run the tests just follow the steps:
- Run ```pip install -r requirements/test.txt``` command
- Run ```pytest``` command

# Contribute
Feel free to contribute, just make a new branch from main branch, make the changes and open a new pull request.
