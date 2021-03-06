FROM python:3

COPY ./requirements.txt /requirements.txt
COPY . .

RUN pip install -r /requirements.txt
RUN chmod +x /app.py

CMD ["python","./app.py"]