from city_scrapers_core.constants import BOARD
from city_scrapers_core.items import Meeting
from city_scrapers_core.spiders import CityScrapersSpider
from datetime import datetime

class IlInvestmentPolicySpider(CityScrapersSpider):
    name = "il_investment_policy"
    agency = "Illinois Investment Policy"
    timezone = "America/Chicago"
    allowed_domains = ["www2.illinois.gov"]
    start_urls = ["https://www2.illinois.gov/sites/iipb/Pages/MeetingInformation.aspx"]

    def parse(self, response):
        """
        `parse` should always `yield` Meeting items.

        Change the `_parse_title`, `_parse_start`, etc methods to fit your scraping
        needs.
        """
        for item in response.css(".meetings"):
            meeting = Meeting(
                title=self._parse_title(item),
                description='',
                classification=BOARD,
                start=self._parse_start(item),
                end=None,
                all_day=False,
                time_notes=None,
                location=self._parse_location(item),
                links=self._parse_links(item),
                source=self._parse_source(response),
            )

            meeting["status"] = self._get_status(meeting)
            meeting["id"] = self._get_id(meeting)

            yield meeting
    
    def _parse_title(self, item):
        """Parse or generate meeting title.""" 
        return ""

    def _parse_start(self, item): 
        """
        Parse start datetime as a naive datetime object.
        Function will pull all relevant dates, and return the next available 
        date after current datetime.
        """
        str_dates = response.css('ul.list-unstyled > li::text').getall()
        dates = [datetime.strptime(x.strip(), '%m/%d/%y') for x in str_dates]
        next_date = min([x for x in dates if x > datetime.now()])
        
        return next_date

    def _parse_location(self, item):
        """Parse or generate location."""
        return {
            "address": "",
            "name": "",
        }

    def _parse_links(self, item):
        """Parse or generate links."""
        return [{"href": "", "title": ""}]

    def _parse_source(self, response):
        """Parse or generate source."""
        return response.url
