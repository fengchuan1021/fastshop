FROM python:3.10-slim
#FROM python:3.10
WORKDIR /app
COPY . /app
EXPOSE 8000
CMD sh ./dockerstart.sh