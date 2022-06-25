### Overview

web service is main service (Flask)

book and user is another 2 microservice

web service will get data from microservice by nameko rpc

### Start Service

```
docker-compose up
```
then access http://127.0.0.1:5000/user or http://127.0.0.1:5000/book


### nameko与rabbitmq交互模式说明

```
1.采用topic的路由方式；
2.exchange默认为rpc-nameko；
3.mq的队列名称与服务名称关联，比如服务名为user_service，则请求队列的名称为rpc-user_service，响应队列名为rpc.reply-user_service-随机数；
4.每个消费队列的prefetch_count取自max_works，即与消费服务线程数一致
5.为保证消息可靠性，rabbitmq会进行持久化，同时也会损耗一定的性能，在高并发情况下CPU会消耗比较大
```