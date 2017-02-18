# tokenizer

## Requires
##### Python 2.7
##### MongoDB

## Install
##### git clone https://github.com/kotaba/tokenizer.git
##### cd tokenizer
##### pip install -r pip.list

## Config
### Edit .py files in tokenizer/src/config

### api.py
##### settings for parse data from api.meeetmix.ru

###### meetmix_api_url - url of api, must be url to api of meetmix.ru *required
###### active_cities - cities ids for parse, must be list of integers *required

### db.py
###### mongodb_host -host of mongodb server, must be string *required
###### mongodb_user - user for mongodb server, must be string *required
###### mongodb_password - password of user in mongodb, must be string *required
###### mongodb_port - port for connect to mongo server, must me integer
###### mongodb_database - specify database of mongodb *required



