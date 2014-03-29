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

### Configuration
Following configuration are needed to get stream from twitter. Register your application in twitter developer site. This will provide ```consumer_key``` ```consumer_secret``` ```access_token``` and ```access_token_secret```. Add these detail in dev_settings.py

```sh
    TWITTER_CONFIG = {
	    "consumer_key":{consumer_key},
	    "consumer_secret":{consumer_secret},
	    "access_token":{access_token},
	    "access_token_secret":{access_token_secret},
    }
```


### Deployment
To start and stop the server, run ```runscript.sh```
```sh
    sh runscript.sh
```
### APIs Documentation
1. /v1/keywords - This APIs support GET, POST, PUT and DELETE method. It's store list of keyword data.
2. /v1/keywords/{id} - Return the keyword detail for specific id
3. /v1/tweets - Return the list of tweets from elasticsearch
4. /v1/tweets/search?q={free text} - It's return the list of tweets which matches with free text
5. /v1/tweets/search?user_name={user_name} - It's return the list of tweets from specific user_name.

### Note
On adding or updating the keyword, it's in sync after 1-hours to change this durantion we need the modify the ASYNC_TIME in dev_settings.py
