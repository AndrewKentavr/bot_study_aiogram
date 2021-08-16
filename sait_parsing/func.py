from math import ceil
from references_to_tasks import soup


def checking_quantity_start():
    number_tasks = int(soup.find(class_="componentboxcontents").find('p').text)
    number_start = ceil(number_tasks / 100)
    return number_start
