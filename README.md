# Automated ETL Pipeline with OpenWeather API

<hr>

Kafka Execution Code:
```
.\bin\windows\zookeeper-server-start.bat .\config\zookeeper.properties
.\bin\windows\kafka-server-start.bat .\config\server.properties
.\bin\windows\kafka-console-consumer.bat --bootstrap-server localhost:9092 --topic weather-data --from-beginning