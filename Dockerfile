FROM python:3.12

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update -y

EXPOSE 8000

COPY . /fast_api_test

WORKDIR /fast_api_test

RUN pip install -r requirements.txt --no-cache-dir

CMD ["uvicorn", "main:app", "--reload", "--host=0.0.0.0"]