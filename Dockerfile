FROM python:3.7
RUN pip install flask
RUN apt-get install libmysqlclient-dev python3-dev
RUN pip3 install mysqlclient mysql mysql-connector-python
RUN pip3 install mysql
RUN pip install requests
RUN pip install flask_mysqldb
VOLUME /flask
COPY . /flask
EXPOSE 8080
WORKDIR /flask
CMD [ "python", "./app_script.py" ]
