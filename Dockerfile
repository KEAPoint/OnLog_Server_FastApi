FROM python:3.11.6

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install --upgrade pip && pip install -r /app/requirements.txt

EXPOSE 8000

COPY ./ /app

CMD ["python", "main.py"]