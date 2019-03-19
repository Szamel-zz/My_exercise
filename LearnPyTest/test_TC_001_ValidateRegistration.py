from selenium.webdriver import Chrome


def test_registration_valid_data():
    path = "C:\\Users\\Tamas_Szamel\\Downloads\\chromedriver.exe"
    driver = Chrome(executable_path=path)
    driver.get('http://www.thetestingworld.com/testings')




