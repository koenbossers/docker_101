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

Mounten lokale folder in Docker container:

```bash
docker run -v /Users/koen/CODING/precisionfoodsafety:/pfs_in_docker  -p 8999:5000 myflaskapp
curl http://localhost:8999/lister/pfs_in_docker
```

Interactive development terwijl je app in een container runt! Makkelijk, gewoon je app folder mounten in je container en `--debug` aanzetten in Flask[1].

```bash
docker run -v /Users/koen/CODING/docker_101/flask_in_docker:/flask  -p 8999:5000 myflaskapp flask run --host 0.0.0.0 --debug
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

Laat de studenten vooral hun image taggen met hun studentnummer of zo. Dat maakt het leven een stuk makkelijker voor de nakijkende docent.


[1]: *let wel op: als je de `requirements.txt` aanpast, moet je wel je container rebuilden*