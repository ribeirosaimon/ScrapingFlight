FROM python:latest

COPY ./requirements.txt /root/requirements.txt

RUN pip install -r /root/requirements.txt


COPY . /root/
WORKDIR /root

CMD ["python","app.py"]