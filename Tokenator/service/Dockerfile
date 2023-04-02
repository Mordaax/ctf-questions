FROM python:3.8-slim-buster

ADD . /www

EXPOSE 5121

RUN pip install -r /www/website/requirements.txt
CMD python3 /www/website/main.py
