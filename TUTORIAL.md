# Docker 101 tutorial voor docenten Bio-informatica

## Hoe krijg ik mijn Flask applicatie in een container?

Hier volgt simpele uitwerking om een Flask applicatie te containerizen met Docker.


```bash
cd flask_in_docker
docker build -t myflaskapp .
```

Runnen:

```bash
docker run myflaskapp
```

Runnen met toegang tot netwerk

```bash
docker run -it -p 8999:5000 myflaskapp
```

Runnen met custom entry commando

```bash
docker run -it -p 8999:5000 myflaskapp flask run --host 0.0.0.0 --debug

```

Zie: https://medium.com/@geeekfa/dockerizing-a-python-flask-app-a-step-by-step-guide-to-containerizing-your-web-application-d0f123159ba2

## Hoe kunnen studenten een Docker image inleveren?

```bash
docker image save myflaskapp > s101010_app.tar            # zonder gzip compressie
docker image save myflaskapp | gzip > s101010_app.tar.gz  # met gzip compressie
```

Laden

```bash
docker image load -i s101010_app.tar
docker image load -i s101010_app.tar.gz
```