from bot_time.handlers.cmd import register_handlers_start
from bot_time.handlers.lessons import register_handlers_lesson
from bot_time.handlers.time import register_handlers_time


def reg_cmd(dp):
    register_handlers_start(dp)
    register_handlers_lesson(dp)
    register_handlers_time(dp)