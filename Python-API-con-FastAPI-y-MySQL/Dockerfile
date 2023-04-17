# FROM python:3.9.5
FROM python:3.8-slim-buster
WORKDIR /app
RUN pip3 install fastapi 
RUN pip3 install uvicorn 
RUN pip3 install pymysql 
RUN pip3 install peewee
COPY ./src .
EXPOSE 8000
ENTRYPOINT ["./runUvicorn.sh"]