from redis import Redis

redis_connection = Redis(decode_responses=True)

key = "some-key-int-1"
value = 56

key2 = "some-key-int-2"
value2 = 420

redis_connection.set(key, value)
redis_connection.set(key2, value2)

print(redis_connection.get(key))


print(redis_connection.incr(key, 13))


print(redis_connection.decr(key, 2))