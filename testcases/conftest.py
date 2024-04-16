import pytest
from selenium import webdriver

##The pytest_configure function is a hook function in pytest that is called once the
## configuration object has been created and all plugins and initial confest files have been loaded..

##The pytest addoption  function is a hook function in pytest that is used to add custom command-line options to the
##pytest command. it takes a single argument,parser which is an instance of the argparse.Argumentparser class.

def pytest_addoption(parser):
    parser.addoption("--browser")

##define the browser fixture function with a single argument,request.
##within the browser function,use the request.config.getoption() method to get the value of the --browser
##option passed to the pytest on the command line.

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture()
def setup(browser):

    if browser == "chrome":
        driver = webdriver.Chrome()
        print("Launching Chrome Browser")

    elif browser == "firefox":
        driver = webdriver.Firefox()

    elif browser == "edge":
        driver = webdriver.Edge()

    else:
        print("Headless Mode")
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("headless")
        # driver=webdriver.Chrome(options=chrome_options)
        driver = webdriver.Chrome()

    driver.implicitly_wait(5)
    # driver.maximize_window()
    return driver

##the pytest _metadata function in a hook function in pytest that allows you to
##addd custom metadata to the test report.this metadata can be used to provide
## additional information about the test run ,such as the environment. the test data.
## or any other relevant information.



def pytest_metadata(metadata):
    ##To Add

    metadata["Environment"]="Test"
    metadata["Project Name"]="orangeHRM"
    metadata["Module Name"]="Employee"
    metadata["Tester"]="Credence"

    ##Remove
    metadata.pop("Packages",None)
    metadata.pop("Plugins",None)


@pytest.fixture(params=[
    ("Admin","admin123","Pass"),
    ("Admin1","admin123","Fail"),
    ("Admin","admin1234","Fail"),
    ("Admin1","admin1234","Pass")        ###intentionaly pass kiya hay to check the output...
                                         ##actual output=expected output then condition is true and result is pass otherwise fail..
])
def getData_for_login(request):
    return request.param


@pytest.fixture(params=[
    ("credence","credence","credence","Pass"),
    ("rohit","kk","jj","Pass")

])
def getData_for_Name(request):
    return request.param







########################## before

# import pytest
# from selenium import webdriver
#
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("headless")
#
# @pytest.fixture()
# def setup():
#     # driver=webdriver.Chrome()
#     driver = webdriver.Chrome(options=chrome_options)
#     driver.implicitly_wait(5)
#     driver.maximize_window()
#     # driver.get('https://opensource-demo.orangehrmlive.com/')


