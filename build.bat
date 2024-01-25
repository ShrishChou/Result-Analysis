@REM @echo off
cd C:\Users\email\Documents\ResultTracker
call env\Scripts\activate

rem exit on error
set -o errexit

rem Install dependencies using poetry
poetry install

rem Collect static files
python manage.py collectstatic --no-input

echo Collecting static files

rem Apply migrations
python manage.py migrate

rem Deactivate the virtual environment
deactivate