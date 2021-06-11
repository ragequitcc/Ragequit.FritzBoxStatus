FROM python:3

ADD main.py /

RUN pip install fritzconnection requests

EXPOSE 8080

CMD ["python", "./main.py"]