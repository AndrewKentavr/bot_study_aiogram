from handlers.cmd import register_handlers_start
from handlers.drinks import register_handlers_drinks
from handlers.food import register_handlers_food
from handlers.print_smt import register_handlers_print_smt


def reg_cmd(dp):
    register_handlers_drinks(dp)
    register_handlers_food(dp)
    register_handlers_start(dp)
    register_handlers_print_smt(dp)
