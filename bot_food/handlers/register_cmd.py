from bot_food.handlers.cmd import register_handlers_start
from bot_food.handlers.drinks import register_handlers_drinks
from bot_food.handlers.food import register_handlers_food


def reg_cmd(dp):
    register_handlers_drinks(dp)
    register_handlers_food(dp)
    register_handlers_start(dp)
