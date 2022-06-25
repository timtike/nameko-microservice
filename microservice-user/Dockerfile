FROM centos:7
WORKDIR /code
RUN yum install -y python3
RUN pip3 install -i https://pypi.douban.com/simple/ nameko

COPY ./user.py ./user.py
CMD sh -c "nameko run user --broker amqp://$nameko_username:$nameko_password@$nameko_host"