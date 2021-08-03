from handlers.book import register_handlers_book
from handlers.cmd import register_handlers_start


def reg_cmd(dp):
    register_handlers_start(dp)
    register_handlers_book(dp)
