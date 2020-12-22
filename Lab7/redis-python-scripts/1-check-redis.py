from redis import Redis
redis_connection = Redis()
print("Connected to Redis server: ", redis_connection.ping())