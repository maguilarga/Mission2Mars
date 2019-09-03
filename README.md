# Mission2Mars
Mission2Mars Mission2Mars a web site with information about Mars collected from various sites (NASA, twitter, space-fact.com and astrology.usgs.gov). Every time the users requests it, the information is refreshed. This projects was created to practice Beautiful Soup scraping, Splinter, Mongo DB, Flask and Jinja.

### Prerequisites

* Obviously you will need python; Jupyter Notebooks is optional (the same code is in files "mission_to_mars.ipynb" and "scrape_mars.py"). For any additional libraries, please check requirements.txt
* You should have MongoDB installed, up and running in your system.
* File "chromedriver.exe" should be downloaded in your system abd its path should be added to your system PATH or you should copy the file in the local directory in which you copied the GitHub repo.

### Installing

Download "Mission2Mars" GitHub repo to a local directory

## Running the web site

1. Start your python enviornment
2. Execute file "mars_site.py", this file will invoke allo necessary code from other python or HTML files. 
3. The first time you execute the program in your system, the web site will come up empty.
4. Click on button "Scrape New Data. The necessary code will be executed to bring new information. Since this information will be stored in a local Mongo database, any further execution will come up showing data.

## Built With

* [Pandas](https://pandas.pydata.org/)
* [Flask](https://flask.palletsprojects.com/en/1.1.x/) 
* [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) 
* [Splinter](https://splinter.readthedocs.io/en/latest/) 
* [Jinja](https://jinja.palletsprojects.com/en/2.10.x/) 
* [MongoDB](https://docs.mongodb.com/) 


## Contributing

* Thank you to SrackOverflow who cleared many doubts and provided code snippets
* Thank you to John Hawkins who answered my question and unstucked me 

## Versioning

v 1.0

## Authors

* Martha Aguilar
