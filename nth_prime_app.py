import redis
import web
r = redis.StrictRedis(host='localhost', port=6379, db=0)
urls = ('/nth_primes/(.*)', 'get_primes')


	
class get_primes:
	def GET(self, nth_prime):
		n = r.get('primes_' + str(nth_prime))
		return n

if __name__ == "__main__": 
	
	# redis server wrapper instance
	r = redis.StrictRedis(host='localhost', port=6379, db=0)
	try:
		response = r.client_list()
		print('Connected to Redis DB')
	except redis.ConnectionError:
		raise Exception('Unable to connect to Redis DB')
	
	app = web.application(urls, globals())
	app.run()
