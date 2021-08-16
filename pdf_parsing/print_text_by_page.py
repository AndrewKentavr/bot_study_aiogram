from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer

path = 'C:/Users/andrt/PycharmProjects/bot_study_aiogram/pdf_parsing/Evgeni_Onegin.pdf'
path_math = 'C:/Users/andrt/Desktop/Обушение/Матеша/своё/сборник задач по математике сканави.pdf'

count = 0
for page_layout in extract_pages(path_math, page_numbers=[3, 7]):
    for element in page_layout:
        if isinstance(element, LTTextContainer):
            print(element.get_text())
