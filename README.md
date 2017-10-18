# Introduction

We here present an application called with a single argument "n".
This application returns the 'nth' prime number.
The program is called through a REST api via an URL.

The computation of the Nth prime number is a very classical problem and many methods have already been proposed.
Overall, these methods require either a high computational complexity or a large amount of RAM memory.

The program should run on an embedded device like a Raspberry Pi 3.
To maintain a high efficiency of the service and reduce the computational cost, this code is based on a NoSQL database.

# Platform

This code has been developped on Ubuntu 16.04 and does not depend on a specific version of Python.


# Python requirements

Install required packages from requirements.txt

    pip install -r requirements.txt

This will install the following packages

    #cat requirements.txt
    redis==2.10.6
    web.py==0.38

For python3, you may have to install web.py using easy_install

    :~$ easy_install web.py
    :~$ pip install redis

# Redis requirement

Install Redis client and server for your plateform from [https://redis.io/](https://redis.io/).

A quickstart can be found in [https://redis.io/topics/quickstart](https://redis.io/topics/quickstart).

Redis may also be quickly installed by running the following commands.

    wget http://download.redis.io/redis-stable.tar.gz
    tar xvzf redis-stable.tar.gz
    cd redis-stable
    make
    sudo make install

# Package content

The current application contains 4 files: 

* *requirements.txt* : list of required python modules, to be ran with pip
* *primes.data* : text file containing the 10M first prime numbers
* *fillup_redis.py* : running the python script will laod 10M primes number in the Redis DB.
* *nth_prime_app.py* : the main application will start a REST service available from your web browser.

**All the files listed above must be placed the same directory.**

# How-To

In a Terminal, start the redis server. Keep this console open.

    :~$ redis-server

In another terminal, check the connection to redis server by running:

    :~$ redis-cli PING

This command should return **PONG**

Then install python dependencies

    :~$ pip install -r requirements.txt

For python3, you may have to install web.py using easy_install

    :~$ easy_install web.py
    :~$ pip install redis

Unzip the file primes.data.gz

	:~$ gunzip primes.data.gz
	
Then fill up the redis database by running

    :~$ python fillup_redis.py

Filling up the redis database takes about 4 to 5 minutes depending on your system.
You'll have to run this script only once.

Finally, you can launch the main app with

    :~$ python nth_prime_app.py 8081

The service is now available from your web browser.

Connect to [http://localhost:8081/nth_primes/n](http://localhost:8081/nth_primes/1) and set n to the value of nth prime number you want to return.

Example: [http://localhost:8081/nth_primes/10000000](http://localhost:8081/nth_primes/10000000) returns 179424673

If *n* exceeds 10 million, the app returns *None*

