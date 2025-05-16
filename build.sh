pip install --upgrade pip

set -o errexit

pip install poetry -U
poetry install --only main

python manage.py collectstatic --noinput

python manage.py migrate
