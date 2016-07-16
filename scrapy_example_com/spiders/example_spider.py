# -*- coding: utf-8 -*-
import scrapy
import json
import string
import random
hostname = 'localhost'
username = 'jduser_rw'
password = 'password'
database = 'jddb'
# Simple routine to run a query on a database and print the results:
def doQuery( conn,name) :
	new_name = string.replace(name, "'", "''")
	cur = conn.cursor()
	try:
		cur.execute("INSERT INTO conditions (condition,consumer_id,doctor_id,user_rating) VALUES ('{0}','{1}','{2}','{3}')".format(new_name,random.randrange(1,10000),random.randrange(1,1000),random.uniform(0,10)))
		pass
	except Exception, e:
		print "Eroor ", new_name
	else:
		pass
	finally:
		pass

import psycopg2

class ExampleSpiderSpider(scrapy.Spider):
    name = "example_spider"
    allowed_domains = ["mayoclinic.org"]
    start_urls = (
        'http://www.mayoclinic.org/diseases-conditions/index',
        # All the URLs has to be listed here
    )

    def parse(self, response):
    	rows = response.xpath('/html/body/form/div/div/div/div/ol/li/a/text()').extract()    	
    	if len(rows) > 0:
			for row in rows:
				myConnection = psycopg2.connect( host=hostname, user=username, password=password, database=database )
   				myConnection.autocommit = True
   				doQuery( myConnection,row )
    			myConnection.close()
