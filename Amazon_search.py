from autoscraper import AutoScraper

amazon_url="https://www.amazon.in/s?k=iphone&crid=3MLK1PLC89SVI&sprefix=iphone%2Caps%2C191&ref=nb_sb_noss_2"
wanted_list=["₹50,499","iPhone 13 (128GB) - (Product) RED"]

scraper=AutoScraper()
result=scraper.build(amazon_url,wanted_list)

print(scraper.get_result_similar(amazon_url,grouped=True))