# About

This originated from a joke between me and a couple of colleagues. It was inspired by the [BOFH excuse generator](https://pages.cs.wisc.edu/~ballard/bofh/).

# Running

Build ohwauw-flask image:

```
cd ohwauw-flask
docker build -t ohwauw-flask:latest
```

Then, to deploy the app run from the root directory of this repo:

```
docker-compose build
docker-compose up -d
```
# Reverse proxy

Note that there are some rules pre-defined in the docker-compose.yml file to publish this app via traefik. You might want to adjust those according to your needs.

# Disclaimer

Any opinions expressed here are exclusively our own and are not representative of our employer.