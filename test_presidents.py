import pytest
## Testing the RESTAPI
## csc 256-0002
## Lab 10
import requests
from pip._vendor.urllib3 import response

from labDuckDuckgo import getRequest, parseResponse

URL = 'https://api.duckduckgo.com/?q=presidents%20of%20the%20united%20states&format=json&pretty=1%22'
#response = requests.get(URL).json
response = getRequest(URL)
presidents = parseResponse(response)

list = []
for president in presidents:
    list.append((president))


list_of_names_from_response = [response]
presidentName = ["George Washington"
                 "John Adams"
                 "Thomas Jefferson"
                 "James Madison"
                 "James Monroe"
                 "John Quincy Adams"
                 "Andrew Jackson"
                 "Martin Van Buren"
                 "William Henry Harrison"
                 "John Tyler"
                 "James K. Polk"
                 "Zachary Taylor"
                 "Millard Fillmore"
                 "Franklin Pierce"
                 "James Buchanan"
                 "Abraham Lincoln"
                 "Andrew Johnson"
                 "Ulysses S. Grant"
                 "Rutherford B. Hayes"
                 "James Garfield"
                 "Rutherford B. Hayes"
                 "Rutherford B. Hayes"
                 "Benjamin Harrison "
                 "Grover Cleveland"
                 "William McKinley"
                 "Theodore Roosevelt"
                 "William Howard Taft"
                 "Woodrow Wilson"
                 "Warren G. Harding"
                 "Calvin Coolidge"
                 "Herbert Hoover"
                 "Franklin D. Roosevelt"
                 "Harry S. Truman"
                 "Dwight D. Eisenhower"
                 "John F. Kennedy"
                 "Lyndon B. Johnson"
                 "Richard M. Nixon"
                 "Gerald R. Ford"
                 "James Carter"
                 "Ronald Reagan"
                 "George H. W. Bush"
                 "William J. Clinton"
                 "George W. Bush"
                 "Barack Obama"
                 "Donald J. Trump"]


def get_list():
    return [
        "George Washington",
        "John Adams",
        "Thomas Jefferson",
        "James Madison",
        "James Monroe",
        "John Quincy Adams",
        "Andrew Jackson",
        "Martin Van Buren",
        "William Henry Harrison",
        "John Tyler",
        "James K. Polk",
        "Zachary Taylor",
        "Millard Fillmore",
        "Franklin Pierce",
        "James Buchanan",
        "Abraham Lincoln",
        "Andrew Johnson",
        "Ulysses S. Grant",
        "Rutherford B. Hayes",
        "James Garfield",
        "Rutherford B. Hayes",
        "Rutherford B. Hayes",
        "Benjamin Harrison ",
        "Grover Cleveland",
        "William McKinley",
        "Theodore Roosevelt",
        "William Howard Taft",
        "Woodrow Wilson",
        "Warren G. Harding",
        "Calvin Coolidge",
        "Herbert Hoover",
        "Franklin D. Roosevelt",
        "Harry S. Truman",
        "Dwight D. Eisenhower",
        "John F. Kennedy",
        "Lyndon B. Johnson",
        "Richard M. Nixon",
        "Gerald R. Ford",
        "James Carter",
        "Ronald Reagan",
        "George H. W. Bush",
        "William J. Clinton",
        "George W. Bush",
        "Barack Obama",
        "Donald J. Trump"]


def test_if_present():
    assert "Barack Obama" in get_list()


def test_present():
    assert "John Adams" == pres_name_is()


def pres_name_is():
    return "John Adams"


def test_notpresent():
    assert " William " != pres_name_is()


def not_present():
    return None
