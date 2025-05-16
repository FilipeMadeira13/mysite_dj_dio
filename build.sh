set -o errexit

pip install poetry -U
poetry install --no-root --without-dev

python manage.py collectstatic --noinput

python manage.py migrate
