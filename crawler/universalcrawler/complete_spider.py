import glob
import pprint

for i in glob.glob('./universalcrawler/spiders/*.py'):
    if 'scrapy.Spider' not in open(i).read():
        continue
    lines = open(i).readlines()
    lines.insert(2, 'from readability import Document\n')
    lines.insert(9, "    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15"
                    " (KHTML, like Gecko) '\n                             'Version/12.0.3 Safari/605.1.15'}\n")
    lines[12] = '''        doc = Document(response.text)
        yield {
            'url': response.url,
            'short_title': doc.short_title(),
            'summary': doc.summary(html_partial=True),
        }
        for next_page in response.css('a::attr("href")'):
            yield response.follow(next_page, self.parse)
'''
    with open(i, 'w') as f:
        f.write(''.join(lines))
