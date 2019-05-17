
# Log Analysis
The third project in Udacity's full stack web development nanodegree program.
## Project Overview
The project requires students to create and use SQL queries that would fetch results from a large database of a news website.The objective of this project is to extend the student's SQL database skills. The code requirements suggest the use of only one  single query to answer each request. The answer code presented here does not change the original database but utilizes **views** to answer the third query.

## Requirements

[Python 3](https://www.python.org/download/releases/3.0/) - The code uses ver 3.6.4\
[Vagrant](https://www.vagrantup.com/) - A virtual environment builder and manager\
[VirtualBox](https://www.virtualbox.org/) - An open source virtualiztion product.\
[Git](https://git-scm.com/) - An open source version control system


##  How to access the project?

Follow the steps below to access the code of this project:

 1. If you don't already have the latest version of python download it from the link in requirements.
 2. Download and install Vagrant and VirtualBox.
 3. Download this Udacity [folder](https://d17h27t6h515a5.cloudfront.net/topher/2017/August/59822701_fsnd-virtual-machine/fsnd-virtual-machine.zip) with preconfigured vagrant settings.
 4. Clone this repository.
 5. Download [this](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) database.
 6. Navigate to the Udacity folder in your bash interface and inside that cd into the vagrant folder.
 7. Open Git Bash and launch the virtual machine with`vagrant up`
 8. Once Vagrant installs necessary files use `vagrant ssh` to continue.
 9. The command line will now start with vagrant. Here cd into the /vagrant folder.
 10. Unpack the  database folder contents downloaded above over here. You can also copy the contents of this repository here.
 11.  To load the database type `psql -d news -f newsdata.sql`
 12. To run the database type `psql -d news`
 13. You must run the commands from the Create views section here to run the python program successfully.
 14. Use command `python log-results.py` to run the python program that fetches query results.

##  Create Views

Views were created to answer the third query in the project with the purpose of leaving the original database unchanged. They also helped break the question down into comprehensible portions.

The first view code is as follows:

"create view mostviewedarticles as select articles.title, count(*)\n"
    "as num from articles join log on articles.slug = substring(log.path, 10)\n"
    "group by articles.title order by num desc"


##  Troubleshooting
TBD
