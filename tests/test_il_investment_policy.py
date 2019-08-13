from datetime import datetime
from os.path import dirname, join

import pytest
from city_scrapers_core.constants import BOARD
from city_scrapers_core.utils import file_response
from freezegun import freeze_time

from city_scrapers.spiders.il_investment_policy import IlInvestmentPolicySpider

# test_response = file_response(
#     join(dirname(__file__), "files", "il_investment_policy.html"),
#     url="https://www2.illinois.gov/sites/iipb/Pages/MeetingInformation.aspx",
# )

test_response = file_response(
    './tests/files/il_investment_policy.html', url='https://www2.illinois.gov/sites/iipb/Pages/MeetingInformation.aspx'
)

spider = IlInvestmentPolicySpider()

freezer = freeze_time("2019-07-23")
freezer.start()

parsed_items = [item for item in spider.parse(test_response)]
freezer.stop()


def test_title():
    assert parsed_items[0]["title"] == "2019 Board Meetings"


def test_description():
    assert parsed_items[0]["description"] == ""


def test_classification():
    assert parsed_items[0]["classification"] == BOARD


def test_status():
    assert parsed_items[0]["status"] == "EXPECTED STATUS"

    
def test_start():
    assert parsed_items[0]["start"] == datetime(2019, 9, 11, 0, 0)
    

def test_end():
    assert parsed_items[0]["end"] == None


def test_all_day(item):
    assert parsed_items[0]["all_day"] == False
    
    
def test_time_notes():
    assert parsed_items[0]["time_notes"] == 'Unless noted all meetings will take place at 1:30pm'


def test_location():
    assert parsed_items[0]["location"] == {
        "name": "James R. Thompson Center",
        "address": "100 W. Randolph St. Room 16-503 Chicago, Illinois"
    }


def test_links():
    assert parsed_items[0]["links"] == [{
      "href": "EXPECTED HREF",
      "title": "EXPECTED TITLE"
    }]


def test_source():
    assert parsed_items[0]["source"] == "https://www2.illinois.gov/sites/iipb/Pages/MeetingInformation.aspx"

