@echo off
cd /d %~dp0\crawler
echo 크롤링 시작...
python crawl_listings.py
python crawl_prices.py
echo 크롤링 완료!
pause