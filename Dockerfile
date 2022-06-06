FROM python:3.9-alpine
WORKDIR /app
COPY src/ src/
COPY apidocs/ apidocs/
COPY gunicorn.sh .
COPY requirements.txt .
RUN pip3 install -r requirements.txt
ENTRYPOINT ["./gunicorn.sh"]