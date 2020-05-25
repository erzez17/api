FROM ubuntu:16.04

RUN apt-get update && apt install -y python-pip && python && pip install flask 

COPY . .

CMD ["python", "api.py"]


