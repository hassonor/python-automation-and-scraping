
# m3-demo-03-SelectorsUsingXpath


scrapy shell https://www.webnots.com/basics-of-a-static-website/
# response object holds the response of our request

# Using xpath selectors

# xpath is not relative to selectors, xpath is absolute the document
# xpath is starts with '//' it works like .descendant (it will consider children and its grand children and soon)
# in xpath will use '/' it works like .child (it will consider only immediate child)

# getting title 
## INSPECT this with chrome before running the command, show how you can copy the XPath of an element

response.xpath('/html/head/title/text()').get()  


# This will get the text from all p tags
response.xpath('//p/text()').get() 

# it will extract the text from first p tag
response.xpath('//p/text()').extract_first() 

# attribute selectors 

# It will extract list of all images which are having attribute "src"
response.xpath('//img/@src').extract() 

## INSPECT this with chrome before running the command, show how you can copy the XPath of an element

# extracting all sub-headings present in the webpage
response.xpath('//*[@id="post-149"]/div/div[3]/div[1]/div/ol/li/text()').extract() 

## INSPECT this with chrome before running the command, show how you can copy the XPath of an element
# extracting how many likes are there for webpage
response.xpath('//*[@id="like-149"]/span/text()').extract() 

## INSPECT this with chrome before running the command, show how you can copy the XPath of an element
# extracting all the captions of images present in webpage with the help of class name
response.xpath('//*[@class="wp-caption-text"]/text()').extract()

# Include a few regular expressions examples here
response.xpath("//*[contains(text(), 'static')]/text()") 

response.xpath("//*[contains(text(), 'static')]/text()").extract()

response.xpath("//*[contains(text(), 'static')]/text()").extract()[2]

