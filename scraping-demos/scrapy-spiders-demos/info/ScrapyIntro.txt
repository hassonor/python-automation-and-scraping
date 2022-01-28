# m3-demo-01-ScrapyIntro

# Installation & setup of scrapy

# Install scrapy
pip install scrapy --upgrade
(or) 
pip3 install scrapy --upgrade

# Issues with installing scrapy run on the mac and fix issues
brew doctor

# to check whether scrapy is installed or not open terminal 
scrapy
# if every thing is fine then we can find a list of commands on terminal

scrapy version

# Scrapy comes with a simple benchmarking suite.
# benchmarking is used to get to have an idea of how Scrapy performs in your hardware
scrapy bench

scrapy fetch --nolog https://stackoverflow.com/questions/19687421/difference-between-beautifulsoup-and-scrapy-crawler

scrapy fetch --nolog https://stackoverflow.com/questions/19687421/difference-between-beautifulsoup-and-scrapy-crawler > stackoverflow_file.html

# Open up this file using sublimetext and show the content

# getting settings(by default it is empty)
scrapy settings

# it will open the given url in chrome as scrapy spider would see the page
scrapy view https://stackoverflow.com/questions/19687421/difference-between-beautifulsoup-and-scrapy-crawler

#scrapy shell

#starting of the scrapy shell  
scrapy shell https://stackoverflow.com/questions/19687421/difference-between-beautifulsoup-and-scrapy-crawler 

#It will give the all available scrapy objects
shelp()

#to get address of default spider
spider

#It will give scrapy location
scrapy

#It will give crawler object location
crawler

#By default item object is empty
item

#It will give what type of request we have made and URl of website
request

#It will give the status code of response and URl of website
response

#It will give the url of website
response.url  

#It will give the status code
response.status

#It will open the response in a browser and copy the url of downloaded website, 
#we will be used in the end of this demo.
view(response) 

#to exit from scrapy shell
exit()  

#we can use downloaded html file also to scrape data(we have copied this url from view(response) output)
scrapy shell file:///private/var/folders/yd/1rlyjfk975d3bb98d7_nyt740000gn/T/tmpv_4uok6n.html

response.url

# Show this page in the browser: 'https://stackoverflow.com/'

fetch('https://stackoverflow.com/')

response.url

exit()


