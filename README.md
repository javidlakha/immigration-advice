# immigration-advice

## Installation

First, install

* [AWS CDK](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html)
* [Docker](https://docs.docker.com/engine/install/)
* [Docker Compose](https://docs.docker.com/compose/install/)

and then run

```bash
yarn install
```

## Local development

To launch the development server, ensure Docker is running and then run

```bash
yarn dev
```

The development server will be running in a container that can be accessed at
[http://localhost:8000/](http://localhost:8000/). It supports hot reloading:
changes made to the `api` directory will automatically be applied.


```
source .env && ngrok http --domain=$NGROK_DOMAIN 8000
```
