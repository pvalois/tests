FROM python:3.5.1
RUN apt-get update && apt-get -y install python3-pip 
ADD flask1.py /root/flask.py
ADD requirements.txt /root/requirements.txt
RUN pip3 install -r /root/requirements.txt
ENTRYPOINT ["python3","/root/flask.py"
