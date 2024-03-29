# Exercise 4: Python App to Kakfa running in Docker

## Objectives

1) Run Zookeeper + Kafka
2) Produce messages from the command line
3) Consume/Read messages from the command line
4) Produce messages from a Java application.
5) Consume/Read messages from a Java application.
6) Modify the Java Producer and/or Consumer Java application.


## Run Kafka in your computer with Docker
Simple scenario: 1 zookeeper + 1 Kafka broker.

Start the ZooKeeper and Kafka container.

```sh
$ docker-compose up -d
```

## Command Line , create a new Kafka topic
Using the terminal create the topic 'ventas'

```sh
docker-compose exec kafka kafka-topics --create --topic ventas --partitions 1 --replication-factor 1 --if-not-exists --bootstrap-server localhost:9092
```

## Run the Producer Python App from VisualStudio

## Run the Consumer Python App from VisualStudio

## Console Kafka commands
Read topic content:

```sh
$ docker-compose exec kafka kafka-console-consumer --topic ventas --from-beginning --bootstrap-server localhost:9092
hi
dlp
```

#### More Exercises
##### Exercise 4.1 
Create a new topic from the command line. Then modify the Producer App and the Consumer App to use the new topic.

##### Exercise 4.2
Produce messages from the console. Read them from the Python Consumer App in VisualStudio.

##### Exercise 4.3
Produce messages from the Producer App in VisualStudio, and read them in the console. 
Read the messages also with the Kafka Admin screen at http://localhost:9021/clusters

### Clean up

Shut down Docker Compose

```sh
$ docker-compose down
```
