# docker build -t kamutest .
# docker run --name kamutest -it kamutest
FROM python:3
WORKDIR /usr/src/app
COPY . .
CMD ["python", "./gm.py"]