# Running the project

- Clone the repo

- CD into the cloned directory

```cmd
CD path/to/directory  
```

- Create venv to not disturb your installed system packages(can vary depending on your system)

```cmd
python -m venv .  
```

- Install dependecies(also can vary depending on your system)

```cmd
pip install -r requirements.txt 
```
- Start the server using:

```
python manage.py runserver 0.0.0.0:8000
```

- CV data is available under following urls:

```
http://localhost:8000/api/all/
http://localhost:8000/api/personal/
http://localhost:8000/api/experience/
http://localhost:8000/api/education/
```

- To retreive data using CLI commands(last argument can be one or multiple sections(e.g. education personal experience)):

```
 python manage.py get_cv_data education 
```
