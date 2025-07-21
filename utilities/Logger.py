
import logging
class log_generator_class:
    @staticmethod
    def loggen_method():
        logger = logging.getLogger(__name__)
        log_file = logging.FileHandler(r"X:\Automation Testing\04. CredKart_Pytest_Framework\Logs\CredKart_Automation.log")
        log_formate = logging.Formatter("%(asctime)s - %(levelname)s - %(funcName)s - %(lineno)d - %(message)s")
        log_file.setFormatter(log_formate)
        logger.addHandler(log_file)
        logger.setLevel(logging.DEBUG)
        return logger


''''
What is log level ?
Debug
Info
Warning
Error
Critical
'''

'''
log file
log format
on every run, logs should add(append in same file
log level
'''

