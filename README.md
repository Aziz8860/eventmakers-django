```
python -m venv .venv
.\.venv\Scripts\activate
```

```
pip install django
django-admin startproject core .
```

```
python ./manage.py startapp notes
```

Setelah bikin app:

1. Start from view
2. Buat template -> folder templates di app
3. Buat URL dispatcher -> urlpatterns (urls.py di app)
4. Register urls.py ke core urls
5. Bikin model di models.py
6. Register model ke admin.py (di app)
