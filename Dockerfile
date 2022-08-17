FROM python:3.10-alpine

WORKDIR /tests

COPY requirements.txt .

RUN pip install -U pip
RUN pip install -r requirements.txt

COPY . .

CMD ["pytest", "--browser", "chrome", "--bv", "102.0", "--executor", "http://192.168.0.12"]