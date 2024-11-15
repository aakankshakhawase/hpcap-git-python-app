FROM python
MAINTAINER Aakanksha <aakankshakhawase@gmail.com>
COPY . /tmp/app
RUN pip3 install flask
EXPOSE 5000
ENV FLASK_APP=app.py
CMD ["python3", "/tmp/app/app.py"]


