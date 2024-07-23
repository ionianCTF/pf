FROM python:latest

WORKDIR /flask

COPY ./flask .
RUN pip install -r requirements.txt

CMD [ "python", "app.py" ]
