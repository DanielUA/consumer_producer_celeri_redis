import pickle
import redis

client  = redis.Redis(host='localhost', port=6379, password=None)

if __name__=="__main__":
    client.set("username1", "Danyil")
    client.set("username2", "Misha")
    client.expire("username2", 600)

    n = client.get('username1')
    print(n)