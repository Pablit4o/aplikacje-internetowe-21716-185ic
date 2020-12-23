from redis import Redis
from time import sleep
from datetime import datetime

redis_connection = Redis(db=1, decode_responses=True)

redis_connection.setex("key", 30, "value")

print(datetime.now().time(), redis_connection.get("key"))
sleep(3)
print(datetime.now().time(), redis_connection.get("key"))
sleep(2)
print(datetime.now().time(), redis_connection.get("key"))