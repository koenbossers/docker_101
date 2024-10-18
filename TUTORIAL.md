# Docker 101 tutorial voor docenten Bio-informatica

## Hoe krijg ik mijn Flask applicatie in een container?

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