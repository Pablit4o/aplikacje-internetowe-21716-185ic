from redis import Redis

redis_connection = Redis(decode_responses=True)

script = """
local arr = {}
for i = 0, 10 do
    arr[i] = {}
    for j=1,10 do
        arr[i][j] = i*j
    end
end
return arr
"""

print(redis_connection.eval(script, 0))