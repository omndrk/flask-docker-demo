from flask import Flask
import redis
import os

app = Flask(__name__)

redis_host = os.environ.get('REDIS_HOST', 'redis')
redis_port = int(os.environ.get('REDIS_PORT', 6379))
cache = redis.Redis(host=redis_host, port=redis_port)

@app.route("/")
def hello():
    count = cache.incr('hits')
    return f"Hello, Flask! This page has been visited {count} times."

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)