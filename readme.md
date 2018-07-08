# upcanvas

## USAGE(python)

install chromedriver

install pip package

```sh
$ pipenv install
```

run

```sh
$ pipenv run python index.py 1.svg
```

## USAGE(docker)

create image

```sh
$ docker build t- upcanvas .
```

run

```sh
$ docker run -d --name upcanvas upcanvas
$ docker cp .env upcanvas:/home/seluser/.env
$ docker cp 1.svg upcanvas:/home/seluser/1.svg
$ docker exec upcanvas pipenv run python index.py 1.svg
```

delete container

```sh
$ docker stop upcanvas
$ docker rm upcanvas
```