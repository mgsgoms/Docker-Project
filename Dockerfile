FROM python:3.7
RUN pip install flask
RUN pip3 install MySQL
RUN pip install requests
RUN pip install flask_mysqldb
VOLUME /flask
COPY . /flask
EXPOSE 8080
WORKDIR /flask
CMD [ "python", "./app_script.py" ]
