FROM python:3.6
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE liveapi.settings

ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt


ADD . /code
WORKDIR /code

ENTRYPOINT [gun]