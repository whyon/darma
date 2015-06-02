from bottle import *

@route('/')
def index():
    return template('index.tpl')

run(port=7777)
