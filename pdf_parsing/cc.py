import io

from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage

path = 'C:/Users/andrt/PycharmProjects/bot_study_aiogram/pdf_parsing/Evgeni_Onegin.pdf'

"""Первое, что мы делаем, это создаем экземпляр ресурсного менеджера. Далее, мы создаем файловый объект через модуль io 
в Python. Если вы работаете в Python 2, то вам может понадобиться модуль StringIO. Наш следующий шаг – создание 
конвертера. В данном случае, мы выберем TextConverter, однако вы можете также использовать HTMLConverter или 
XMLConverter, если  захотите. Наконец, мы создаем объект интерпретаторв PDF, который использует наш диспетчер
ресурсов, объекты конвертера и извлечет текст.

Последний шаг, это открыть PDF и ввести цикл через каждую страницу. В конце мы захватим весь текст, закроем несколько
обработчиков и выведем текст в stdout."""


def extract_text_from_pdf(pdf_path):
    resource_manager = PDFResourceManager()
    fake_file_handle = io.StringIO()
    converter = TextConverter(resource_manager, fake_file_handle)
    page_interpreter = PDFPageInterpreter(resource_manager, converter)

    with open(pdf_path, 'rb') as fh:
        for page in PDFPage.get_pages(fh,
                                      caching=True,
                                      check_extractable=True):
            page_interpreter.process_page(page)

        text = fake_file_handle.getvalue()

    # close open handles
    converter.close()
    fake_file_handle.close()

    if text:
        return text


if __name__ == '__main__':
    print(extract_text_from_pdf(path))
