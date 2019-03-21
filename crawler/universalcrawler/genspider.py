import os

while True:
    _ = input()
    os.system('scrapy genspider ' + _.rsplit('.', 1)[0] + ' ' + _)
