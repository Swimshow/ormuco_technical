'''
Question C
At Ormuco, we want to optimize every bits of software we write. Your goal is to write a new library that can be integrated to the Ormuco stack. Dealing with network issues everyday, latency is our biggest problem. Thus, your challenge is to write a new Geo Distributed LRU (Least Recently Used) cache with time expiration. This library will be used extensively by many of our services so it needs to meet the following criteria:

    1 - Simplicity. Integration needs to be dead simple.

    2 - Resilient to network failures or crashes. (STORED IN MEMORY)

    3 - Near real time replication of data across Geolocation. Writes need to be in real time. (UPDATE GEO METHOD)

    4 - Data consistency across regions (IMPLEMENT ON CENTRAL SERVER)

    5 - Locality of reference, data should almost always be available from the closest region (IMPLEMENT ON CENTRAL SERVER)

    6 - Flexible Schema (PYTHON DICT)

    7 - Cache can expire (TTL CACHE)

As a hint, we are not looking for quantity, but rather quality, maintainability, scalability, testability and a code that you can be proud of.
'''

from cachetools import TTLCache

class LRU:

    def __init__(self,expire_time,max_items,other_servers):
        self.cache=TTLCache(maxsize=max_items,ttl=expire_time)
        self.server_list=other_servers

    def real_time_replication(self):
        for server in self.server_list:
            print("replication across servers")
            #some method for updating non local caches

    def get_item(self,key):
        if not self.cache[key]:
            self.cache[key]='some_item_value'
            self.real_time_replication()

        return self.cache[key]

ormuco_lru = LRU(expire_time=60,max_items=100,other_servers=['34.209.390.021','43.06.000.332'])
ormuco_lru.get_item('item_one')

