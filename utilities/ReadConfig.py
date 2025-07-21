import configparser

config = configparser.RawConfigParser()
#config.read(".\\Configurations\\config.ini")
config.read(r"X:\Automation Testing\04. CredKart_Pytest_Framework\Configurations\config.ini")



class ReadConfigClass:
    @staticmethod
    def get_data_for_email():
        email = config.get("login data", "email")
        return email # credencejune01@credence.in


    @staticmethod
    def get_data_for_password():
        password = config.get("login data", "password")
        return password  # cCredence@123


    @staticmethod
    def get_data_for_login_url():
        Login_url = config.get("Application URL", "Login_url")
        return Login_url

    @staticmethod
    def get_data_for_register_url():
        register_url = config.get("Application URL", "registration_url")
        return register_url