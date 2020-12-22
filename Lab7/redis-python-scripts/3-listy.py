from redis import Redis

redis_connection = Redis(decode_responses=True)

list_key = "example-list-B2"

redis_connection.lpush(list_key, 1, 2, 3, 4, 5)

print(redis_connection.lrange(list_key, 0, -1))

# lpop i rpop zwraca lewy lub prawy skrajny element i go usuwa
print(redis_connection.lpop(list_key))

print(redis_connection.rpop(list_key))
print(redis_connection.lrange(list_key, 0, -1))

print(redis_connection.lindex(list_key, 4))
print(redis_connection.llen(list_key))