pip install --upgrade pip

set -o errexit

pip install poetry -U
poetry install --only main --no-root

python manage.py collectstatic --noinput

python manage.py migrate
