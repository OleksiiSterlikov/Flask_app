echo Run db upgrade
flask db upgrade
flask db migrate

echo Run Application
flask run -h 0.0.0.0 -p 5000

