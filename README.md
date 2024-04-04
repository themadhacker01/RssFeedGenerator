# RssFeedGenerator
## Goals

A16Z does not have an RSS feed for its blog. This is to crawl the web page, convert it into an RSS feed and add it to Feedly.

[Web Scraping - How to Scrape Data From A Website](https://www.freecodecamp.org/news/web-scraping-python-tutorial-how-to-scrape-data-from-a-website/)

## Docs

[How do I make an RSS feed URL for a website?](https://www.quora.com/How-do-I-make-an-RSS-feed-URL-for-a-website-that-does-not-have-an-RSS-feed-URL)

[PyPi guide for beautifulsoup4 package](https://pypi.org/project/beautifulsoup4/)

[Python BeautifulSoup - find all class](https://www.geeksforgeeks.org/python-beautifulsoup-find-all-class/)

[Find tags by CSS class using BeautifulSoup](https://www.geeksforgeeks.org/find-tags-by-css-class-using-beautifulsoup/)

## Results

A16Z has put anti-crawling mechanisms on its [news and content](https://a16z.com/news-content/) URL.
```html
<html>
<head><title>403 Forbidden</title></head>
<body>
<center><h1>403 Forbidden</h1></center>
<hr/><center>nginx</center>
</body>
</html>
```