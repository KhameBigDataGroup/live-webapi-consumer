FROM python:3.6
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE liveapi.settings

ADD ./confs/pip /requirements
WORKDIR /requirements
RUN pip install -r requirements.txt


ADD . /code
WORKDIR /code

ENTRYPOINT [gun]