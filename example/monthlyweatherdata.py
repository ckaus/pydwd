import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pydwd.crawler.monthlycrawler import MonthlyCrawler

crawler = MonthlyCrawler()
print crawler.by_city('Berlin-Tempelhof')