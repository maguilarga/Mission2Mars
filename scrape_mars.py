# Import all dependencies
from bs4 import BeautifulSoup as bs
import requests
from splinter import Browser
import pandas as pd


def scrape():
    # NASA Mars News
    # URL of page to be scraped
    url = 'https://mars.nasa.gov/news/'

    # Read the Web Page
    response = requests.get(url)

    # Create a Beautiful Soup object
    soup = bs(response.text, 'html.parser')

    # Search for Header list section to scrape first Title and sub head
    results = soup.find('div', class_="slide")

    # Identify and return the teaser paragraph of the article
    news_p = results.find('div', class_="rollover_description_inner").text.strip()

    # Identify and return title of listing
    news_title = results.find('div', class_="content_title").a.text.strip()

    # create a dictionary and save news
    mars_news = {
        "Title": news_title,
        "SubHead": news_p
    }

    # JPL Mars Space Images - Featured Image
    # Use splinter to navigate the site and find the image url for the current Featured Mars Image

    # Path to 'chromedriver.exe' file
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)

    # Open the browser to the web site
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    site_url = url.split('/spaceimages')[0]
    browser.visit(url)

    # Read the first page
    html = browser.html
    soup = bs(html, 'html.parser')

    # Read the page
    html = browser.html
    # wait for the page to be fully loaded
    time.sleep(2)
    soup = bs(html, 'html.parser')
    # Navigate to more info page
    browser.click_link_by_partial_text('more info')

    # Read the page
    html = browser.html
    soup = bs(html, 'html.parser')

    # find the image
    mars_image = soup.find('figure', class_="lede").a['href']
    mars_image = f"{site_url}{mars_image}"


    # Mars Weather
    # URL of page to be scraped
    url = 'https://twitter.com/marswxreport?lang=en'

    # Read the Web Page
    response = requests.get(url)

    # Create a Beautiful Soup object
    soup = bs(response.text, 'html.parser')

    # Search for Mars weather tweets
    mars_weather = soup.find('div', class_="js-tweet-text-container").p.text


    # Mars Facts (using pandas)
    # point to the site 
    url = 'https://space-facts.com/mars/'

    # Use Panda's `read_html` to parse the url
    tables = pd.read_html(url)
    # mars_facts_html = tables[1].rename(columns={0: "Description", 1: "Value"}). \
    #     set_index("Description").to_html(bold_rows=True, border=2, classes=['table_fmt'])
    mars_facts_html = tables[1].rename(columns={0: "Description", 1: "Value"}). \
        to_html(bold_rows=True, border=2, index=False, classes=['table_fmt'])


    # Mars Hemispheres

    # # Path to 'chromedriver.exe' file
    # executable_path = {'executable_path': 'chromedriver.exe'}
    # browser = Browser('chrome', **executable_path, headless=False)

    # Open the browser to the web site
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)

    # Read the first page
    html = browser.html
    soup = bs(html, 'html.parser')

    # Get a list of the hemisferes links
    hem_links = []
    all_hemis = soup.find_all('div', class_='description')

    for hemis in all_hemis:
        hem_links.append(hemis.h3.text.strip())  

    # Create a list of dictionaries with the information of each hemisfere
    hemisphere_image_urls = []

    # Navigate to each hemisfere to gather the required information
    for hem in hem_links:
        
        # Navigate to the category
        browser.click_link_by_partial_text(hem)

        html = browser.html
        soup = bs(html, 'html.parser')

        # Gather title information
        hem_url = soup.find('div', class_="downloads").find('li').a['href']
        
        # All info in a dictionary and append to hemisferes list
        hem_info = {
            "title": hem.replace('Enhanced', '').strip(), 
            "img_url": hem_url
        }
        hemisphere_image_urls.append(hem_info)

        # Go back to previous page and continue
        browser.back()
        
    # Close the browser
    browser.quit()

    mission_mars_dict = {
        "Mars_News": mars_news,
        "Mars_Images": mars_image,
        "Mars_Weather": mars_weather,
        "Mars_Facts": mars_facts_html,
        "Mars_Hem": hemisphere_image_urls
    }

    return mission_mars_dict