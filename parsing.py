#!/usr/bin/env python
from __future__ import division
import psycopg2

try:
    db = psycopg2.connect("dbname=news")
except:
    print "Error connecting to database"

c1 = db.cursor()
c1.execute("CREATE VIEW mostviewedarticles\n"
           "AS SELECT articles.title, count(*)\n"
           "AS NUM FROM articles JOIN log ON\n"
           "articles.slug = substring(log.path, 10)\n"
           "GROUP BY articles.title ORDER BY num DESC")
c1.execute("SELECT * FROM mostviewedarticles LIMIT 3")
print('*' * 100)
print('What are the most popular three articles of all time?')
print('The top three most popular articles are:')
for items in c1:
    print("<" + str(items[0]) + '> with ' + str(items[1]) + ' views.')

c2 = db.cursor()
c2.execute("SELECT authors.name, count(*) AS NUM FROM authors JOIN articles\n"
           "ON authors.id = articles.author JOIN log \n"
           "ON articles.slug = substring(log.path, 10)\n"
           "WHERE log.status like '200 OK'\n"
           "GROUP BY authors.name ORDER BY num DESC")
print('*' * 100)
print('Who are the most popular article authors of all time?')
print("The most popular authors, in descending order, are:")
for items in c2:
    print(str(items[0] + ' with ' + str(items[1]) + ' views.'))

c3 = db.cursor()
c3.execute("CREATE VIEW statuscounter AS\n"
           "SELECT time::DATE,\n"
           "SUM (\n"
           "CASE WHEN status = '200 OK'\n"
           "THEN 1\n"
           "ELSE 0\n"
           "END)::INTEGER AS success,\n"
           "SUM (\n"
           "CASE WHEN status  =  '404 NOT FOUND'\n"
           "THEN 1\n"
           "ELSE 0\n"
           "END)::INTEGER AS error\n"
           "FROM log GROUP BY time::DATE\n")
c3.execute("select time, success, error, error/(success+error)::DECIMAL\n"
           "as rate from statuscounter\n"
           "where error/(success + error)::DECIMAL > 0.01")
print('*' * 100)
print("On which days did more than 1% of requests lead to errors? ")
print("The following days are when more than 1% lead to errors:")
for items in c3:
    print('On ' + str(items[0]) + ', there was an error rate of '
          + "{0:.2f}%".format(items[3]*100))
