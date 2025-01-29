from selenium import webdriver
import pytest
from pytest_metadata.plugin import metadata_key

@pytest.fixture()
def setup(browser):
    if browser == "edge" :
        driver = webdriver.Edge()
    elif browser =="firefox":
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Chrome()
    return driver
def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

def pytest_configure(config):
     config.stash[metadata_key]["Tester"] = "Mohamed Abo Elenin"
     config.stash[metadata_key]["Project Name"] = "ORANGHERM"

pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("Plugins",None)