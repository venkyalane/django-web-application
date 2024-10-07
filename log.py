import logging

class LogClass:
    def get_the_logs(self):
        logger = logging.getLogger()
        filehandler = logging.FileHandler("register_login.log")  # mode="w"
        formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(module)s: %(funcName)s: %(message)s',
                                      datefmt='%d/%m/%Y %I:%M:%S %p')
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)
        logger.setLevel(logging.INFO)  # WARNING DEBUGE
        return logger