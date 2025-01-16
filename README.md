# microservice_application

That project shows the example of a simple application written in a microservice architecture principle. 
Also, the repo contains a respective version of app that written in a monolithic style. 

### Details
The app represents a list of simple text operations such as make text upper or lower. Each text operation is executed by a separate service. 
The are 4 services:
* ui-service
* text-revert-service
* text-to_upper-service
* text-to_lower-service

![services_structure](.images/services_structure.png)

### Run
Docker-compose is used to deploy all services.

Do:
```bash
docker-compose up
```
in the simple_microservice_app folder.


### Resulting app

![resulting_app](.images/resulting_app.PNG)
