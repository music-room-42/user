# user
User service for 42 school Music Room students project

### Dependencies

- docker
- docker-compose

### Development instructions

Note, [db_images](https://github.com/music-room-42/db_images) repo should be in the sibling directory to this project

to launch the user service run:
```
docker-compose up -d user
```
to run user service shell:
```
docker-compose run --rm -p 8082:8082 user sh
```
to execute command in running container:
```
docker-compose exec user COMMAND_NAME
```
to view logs:
```
docker-compose logs -f user
```
to restart the service:
```
docker-compose restart user
```
to tear down the service:
```
docker-compose down
```
to tear down and delete database volumes:
```
docker-compose down -v
```
