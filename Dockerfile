FROM python:3.12-slim

WORKDIR /app

ADD requirements.txt /app/
RUN pip install -r /app/requirements.txt

ADD src/app.py /app/

CMD ["python", "app.py"]