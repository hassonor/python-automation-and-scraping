# m3-demo-02-SelectorUsingCSS


# SELECTORS using CSS Class

# starting the scrapy shell to show how selectors will work
# This url is represent the post which is having info about Static Website.
scrapy shell https://www.webnots.com/basics-of-a-static-website/
# response object holds the response of our request

# response object expose Selector object on .selector attribute
# response.selector.css().get()

# Normally we will quering responses by CSS and XPATH, responses include the 2 shortcuts
# response.css() 
# and 
# response.xpath()

# Using css selectors

# tag selectors

# selecting the title of the post

## INSPECT this with chrome before running the command

response.css('title')
# This is returning the response as selector object in list formate

# Here we are getting info from selector object but still we are getting the title with html tags
response.css('title').get() 

# To get actual data from title, we are using the css pseudo element, it will get only specific part from the html element. 
response.css('title::text').get()  

# to know type of the extracted data we will use type method
type(response.css('title').get())                              


## INSPECT this with chrome before running the command

# it will give the text which is present inside the first p tag
response.css('p::text').get() 

# This will get the text from all p tags
response.css('p::text').getall() 

# it will extract the text from all p tags
response.css('p::text').extract() 

# it will extract the text from first p tag
response.css('p::text').extract_first()                           

# attribute selectors 

## INSPECT this with chrome before running the command

# It will extract list of all images which are having attribute "src"
response.css('img ::attr(src)').extract() 

# getting logo of the webpage
response.css('img ::attr(src)').extract()[1]

# It will extract the image tag with src attribute 
response.css('img').attrib['src'] 

## INSPECT this with chrome before running the command

# we are getting the all subheadings of our page in list format
# While recording show this in the Chrome developer tools inspection
response.css('#post-149 > div > div > div > div > ol > li ::text').extract() 

response.css('#post-149 > div > div > div > div > ol > li ::text').extract_first()                               
## INSPECT this with chrome before running the command, show how you can copy the CSS path of an element

# extracting how many likes are there for webpage
response.css('#like-149>span::text').get()

response.css('.like-holder>span::text').get()

## INSPECT this with chrome before running the command, show how you can copy the CSS path of an element

# extracting the paticular image caption('Viewing Static Site in Chrome Browser') using id value
response.css('#caption-attachment-2247::text').get() 

## INSPECT this with chrome before running the command, show how you can copy the CSS path of an element

# extracting all the captions of images present in webpage with the help of class name
response.css('.wp-caption-text::text').getall()

## INSPECT this with chrome before running the command, show how you can copy the CSS path of an element

# extracting the information which is present in the 1st subheading and 1st paragraph
response.css('.su-list > ul:first-child > li:first-child::text').get()  

