import time

class SimpleCache:
    def __init__(self, timeout=3600):
        self.cache = {}
        self.timeout = timeout

    def get(self, key):
        """Retrieve an item from cache, if it's not expired."""
        if key in self.cache:
            cached_item = self.cache[key]
            if time.time() - cached_item['timestamp'] < self.timeout:
                return cached_item['value']
        return None

    def set(self, key, value):
        """Store an item in the cache."""
        self.cache[key] = {
            'value': value,
            'timestamp': time.time()
        }
