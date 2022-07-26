FROM python:3.7-alpine
WORKDIR /code
ENV FLASK_APP dingtalk.py
ENV FLASK_ENV development
RUN pip install requests==2.26.0
RUN pip install flask==1.1.4
COPY ./dingtalk.py ./dingtalk.py
CMD ["python", "dingtalk.py"]
