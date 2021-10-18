FROM nikolaik/python-nodejs:python3.9-nodejs16

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /personalwebsite

COPY Pipfile Pipfile.lock /personalwebsite/
RUN pip install pipenv && pipenv install --system


COPY . /personalwebsite/