Implement a simple connection pool using Bounded Blocking Queue.

docker-compose up -d    
docker-compose up --build -d

if i want to take backup for a volume:
docker run -it --rm -v db_data:/data alpine:latest sh -c "ls -l /data"

Using a Utility Container: You can run a temporary container with the same volume mounted to access the files directly from within that container's shell. For example:

This command will run an Alpine Linux container, mount your db_data volume to /data inside the container, and list the contents. You can then use other commands like cp or tar within the container to move or archive the data.



MYSQL users query:
SELECT User, Host FROM mysql.user;


PRIVILIEGES sql

DROP USER IF EXISTS 'rohan@123'@'%';

CREATE USER 'rohan123'@'%' IDENTIFIED BY 'rohan123';
GRANT ALL PRIVILEGES ON dummy_db.* TO 'rohan123'@'%';
FLUSH PRIVILEGES;


docker-compose down -v  # stops and deletes containers AND volumes
docker-compose up --build

DOCKER:
| Action                       | Command                                          |
| ---------------------------- | ------------------------------------------------ |
| Start only app               | `docker-compose up python-app`                   |
| Stop only app                | `docker-compose stop python-app`                 |
| Rebuild only app             | `docker-compose up --build python-app`           |
| Rebuild app w/o affecting DB | `docker-compose up --build --no-deps python-app` |
| Check container status       | `docker ps -a`                                   |

