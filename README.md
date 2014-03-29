Twitter Stream Listener
==============================================
Twitter stream listener, which fetch the data from twitter and provide APIs to access the tweets and users data

### Project Setup
1. ```git clone``` this repository.
2. Run ```python bootstrap.py```
3. Run ```bin/buildout```

The above steps would be needed one time for setting up a new project and generating the project structure. Once done, subsequent builds on new machines are just standard buildout builds i.e.
```sh
    python bootstrap.py
    bin/buildout
```
### Package Installation
Following package are required to install
1. Elasticsearch
2. Redis
3. Nginx

After installation start both services:
```sh
    sudo service elasticsearch start
    sudo service redis-server start
    sudo service nginx start
```
### Deployment
To start and stop the server, run ```runscript.sh```
```sh
    runscript.sh
```
### APIs Documentation

