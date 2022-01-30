import requests
from flask import Flask, render_template
from scrapy.selector import Selector

app = Flask(__name__)


@app.route("/")
def index():
    titles = {"title": [], 'link': [], 'img': [], 'website': [], 'zero': []}

    titles['website'].append("Walla")
    titles['website'].append("Yent")
    titles['website'].append("Maariv")
    titles['website'].append("Mako")
    titles['website'].append("Haaretz")

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

    html = requests.get("https://walla.com", headers=headers)
    source = Selector(text=html.text)
    title = source.xpath('.//*[@class="with-roof "]//h2/text()').extract_first()
    link = source.xpath('.//*[@class="media-wrap"]//@href').extract_first()
    img = source.xpath('.//*[@class="desktop-16-9 mobile-16-9 main-media"]//img/@srcset').extract_first()

    titles['title'].append(title)
    titles['link'].append(link)
    titles['img'].append(img)

    html = requests.get("https://www.ynet.co.il/home/0,7340,L-8,00.html", headers=headers)
    source = Selector(text=html.text)
    title = source.xpath('.//*[@class="slotTitle"]/span/text()').extract_first()
    link = source.xpath('//*[@class="textDiv"]//@href').extract_first()
    img = source.xpath('.//*[@class="mediaItems"]//img/@src').extract_first()

    titles['title'].append(title)
    titles['link'].append(link)
    titles['img'].append(img)

    html = requests.get("https://www.maariv.co.il/", headers=headers)
    source = Selector(text=html.text)
    title = source.xpath('.//*[@class="top-story-title title-hover draft-title-cms"]/text()').extract_first()
    link = source.xpath('.//*[@class="top-story-text-wrap"]//@href').extract_first()
    img = source.xpath('.//*[@class="top-story-img"]/img/@src').extract_first()

    titles['title'].append(title)
    titles['link'].append(link)
    titles['img'].append(img)

    html = requests.get("https://www.mako.co.il", headers=headers)
    source = Selector(text=html.text)
    title = source.xpath('.//*[@class="headline"]/text()').extract_first()
    link = source.xpath('.//*[@class="small"]//@href').extract_first()
    img = source.xpath('.//*[@class="slider_image_inside"]/a/img/@src').extract_first()
    link = "https://www.mako.co.il/" + link
    titles['title'].append(title)
    titles['link'].append(link)
    titles['img'].append(img)

    html = requests.get("https://www.haaretz.co.il/")
    source = Selector(text=html.text)
    title = source.xpath(
        './/*[@class="hj bg cw kz la cu cs lb lc ld le kr ks kt ku kv kw kx ky"]/text()').extract_first()
    link = source.xpath('.//*[@class="kr ks kt ku kv kw kx ky"]//@href').extract_first()
    img = source.xpath('.//*[@class="kl f q km kn ko"]/picture/img/@src').extract_first()
    link = "https://www.haaretz.co.il/" + str(link)

    titles['title'].append(title)
    titles['link'].append(link)
    titles['img'].append(img)

    return render_template('index.html', titles=titles)


if __name__ == "__main__":
    app.run()

"""Daniel Fogel"""
