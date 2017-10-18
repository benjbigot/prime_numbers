import redis
import io
import os

# redis server wrapper instance
r = redis.StrictRedis(host='localhost', port=6379, db=0)
try:
    response = r.client_list()
    print('Redis server found')
except redis.ConnectionError:
    raise Exception('Unable to connect to Redis DB')

if r.get('primes_1') is None:
	print('here')
	if not os.path.exists('./primes.data'):
		raise Exception('Unable to find  the file ./primes.data')
	else:
		w = io.open('./primes.data', 'r')
		n = 1
		print('Filling up Redis DB wirth values')
		for line in w.readlines():
			tag = 'primes_' + str(n)
			r.set(tag, line.rstrip())
			n = n + 1
			if n%10000 == 0:
				print(str(n) + ' values loaded')
		w.close()
		print('Loading db Done')

if r.get('primes_1') == b'2' :
	print('Redis DB ready -- you can run : python nth_prime_app.py 8081')
	
