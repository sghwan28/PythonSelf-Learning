from functools import wraps
from datetime import datetime
import logging
from os import getcwd, path


def log_it(a_func):
    @wraps(a_func)
    def add_to_log(filename = 'my_log.txt'):
        site = path.join(filename,getcwd(),filename)
        print(site)
        logging.basicConfig(filename = site, level=logging.DEBUG,filemode='a', format= "%(asctime)s %(filename)s[line:%(lineno)d]%(levelname)s - %(message)s")
        a_func()
        logging.warning('warning')

    return add_to_log


@log_it
def foo():
    print(datetime.now())


foo()