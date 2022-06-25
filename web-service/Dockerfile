FROM centos:7
WORKDIR /code
RUN yum install -y python3
RUN pip3 install -i https://pypi.douban.com/simple/ flask nameko

EXPOSE 5000
COPY . .
CMD ["python3", "app.py"]