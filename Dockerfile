FROM python:3

WORKDIR /var/Ragequit.FritzBoxStatus

COPY main.py ./

COPY requirements.txt ./

RUN pip install fritzconnection

EXPOSE 8080

CMD ["python", "./main.py"]