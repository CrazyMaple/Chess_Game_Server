from scrapy.cmdline import execute
# scrapy crawl douban_movie_top250 -o douban.csv
# Debug Scrapy In VS code,run this file at F5 https://stackoverflow.com/questions/49201915/debugging-scrapy-project-in-visual-studio-code
try:
    execute(
        [
            'scrapy',
            'crawl',
            'douban_movie_top250',
            '-o',
            'douban.csv',
        ]
    )
except SystemExit:
    pass
