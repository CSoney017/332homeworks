FROM python:3.8.10

RUN pip install Flask==2.2.0 redis requests

ADD ./genes_redis.py /genes_redis.py

CMD ["python", "genes_redis.py"]
