import inspect
import logging


class Loggenerator:

    @staticmethod
    def loggen():

        name=inspect.stack()[1][3]

        logger=logging.getLogger(name)
        logfile=logging.FileHandler("C:\python projects\pythoncredkart\orangehrm\Logs\\orangehrm_automation.log")
        format=logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(funcName)s : %(lineno)s : %(message)s")
        logfile.setFormatter(format)
        logger.addHandler(logfile)
        logger.setLevel(logging.INFO)
        return logger


## get log-->logging.getlogger()
##logfile-->path and name
##format-->logs format
##setformat-->link file and format
##add handler-->maintain-->log file


















