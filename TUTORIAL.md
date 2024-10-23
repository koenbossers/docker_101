# Docker 101 tutorial voor docenten Bio-informatica

Deze praktische demo focust zich op de volgende Docker commando's:

- `docker run`
- `docker build`

Er zijn er echter veel meer. Zie hieronder een *stukje* van de output van het commando `docker` waarbij alleen de common commands te zien zijn. Ik raad iedereen aan om ook eens `docker ps` en `docker images` te proberen als je deze tutorial hebt doorlopen.

```bash
Usage:  docker [OPTIONS] COMMAND

A self-sufficient runtime for containers

Common Commands:
  run         Create and run a new container from an image
  exec        Execute a command in a running container
  ps          List containers
  build       Build an image from a Dockerfile
  pull        Download an image from a registry
  push        Upload an image to a registry
  images      List images
  login       Authenticate to a registry
  logout      Log out from a registry
  search      Search Docker Hub for images
  version     Show the Docker version information
  info        Display system-wide information

  ...

```

## Het runnen van een Docker container

We beginnen met het runnen van een reeds bestaande image, in dit geval de tool [fastq-scan](https://github.com/rpetit3/fastq-scan).

```bash
docker run quay.io/biocontainers/fastq-scan:0.4.4--h7d875b9_0
```

Je kunt het default commando aanpassen:

```bash
docker run quay.io/biocontainers/fastq-scan:0.4.4--h7d875b9_0 fastq-scan -h
```

Een interactieve terminal openen in de container:

```bash
docker run -it quay.io/biocontainers/fastq-scan:0.4.4--h7d875b9_0 sh
```

Om reads van buiten de container door te geven aan de container kunnen we gebruik maken van een STDIN stream: 

```bash
cat reads.fastq | docker run -i quay.io/biocontainers/fastq-scan:0.4.4--h7d875b9_0 fastq-scan

# alternatief
docker run -i quay.io/biocontainers/fastq-scan:0.4.4--h7d875b9_0 fastq-scan < reads.fastq

```

Waar kan je images vinden? Bijvoorbeeld https://hub.docker.com/ en dan zoeken. Of voor bioinformatica tools: https://quay.io/biocontainers/.


## Hoe krijg ik mijn Flask applicatie in een container?

Hier volgt simpele uitwerking om een Flask applicatie te containerizen met Docker.

### Anatomie van een `Dockerfile`

FIXME uitleggen hoe die in elkaar zit

### Bouwen van de image

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

[1]: *let wel op: als je de `requirements.txt` aanpast, moet je wel je container rebuilden*

## Docker image layers

Docker optimaliseert het bouwen van container images door middel van layers. Layers zijn *immutable*. Elke keer als een layer verandert, moeten de layers die daarna komen, ook worden gerebuild. Het optimaliseren van de volgorde van je layers zijn daarom belangrijk. 

Het volgende stappenplan komt van de [officiele Docker documentatie](https://docs.docker.com/get-started/docker-concepts/building-images/understanding-image-layers/).

- The first layer adds basic commands and a package manager, such as apt.
- The second layer installs a Python runtime and pip for dependency management.
- The third layer copies in an application’s specific requirements.txt file.
- The fourth layer installs that application’s specific dependencies.
- The fifth layer copies in the actual source code of the application.

Als je deze principes toepast op onze oorspronkelijke Flask [Dockerfile](./flask_in_docker/Dockerfile) krijg je de [Dockerfile_optimized](./flask_in_docker/Dockerfile_optimized). Deze build sneller als je alleen je code in `app.py` aanpast aangezien het installeren van de requirements dan gecached is (=die layer bestaat al).


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

```bash
docker build -t bprop_s101010 .
```


## Container met Conda packages

In de folder 

```bash
cd conda_env_in_docker
docker build -t bngp .
```

Je 

## Jupyter Docker containers

Jupyter heeft een [hele mooie selectie aan pre-built Docker images](https://jupyter-docker-stacks.readthedocs.io/en/latest/) klaarstaan op hun website. Daarmee is het supermakkelijk om een uitgebreide jupyter server/notebook te starten. Er staat ook een prima uitleg op die pagina om te leren werken met deze containers (spoiler alert: ongeveer alles kennen jullie nu al vanuit het voorbeeld met de Flask app).

```bash
docker run -it --rm -p 10000:8888 -v "${PWD}":/home/jovyan/work quay.io/jupyter/datascience-notebook:2024-10-07
```


## Docker compose

Flask app met whoami als ext dependency (en database, maar die nog niet gebruiken)


## Extra links

https://docs.docker.com/guides/?levels=beginner
https://medium.com/@geeekfa/dockerizing-a-python-flask-app-a-step-by-step-guide-to-containerizing-your-web-application-d0f123159ba2
