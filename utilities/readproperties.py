import configparser

configuration=configparser.RawConfigParser()

configuration.read("C:\\python projects\\pythoncredkart\\orangehrm\\configurations\\config.ini")


class Readconfig():

    @staticmethod
    def geturl():
        url=configuration.get("common info","url")
        return url

    @staticmethod
    def getusername():
        username=configuration.get("common info","username")
        return username

    @staticmethod
    def getpassword():
        password=configuration.get("common info","password")
        return password








