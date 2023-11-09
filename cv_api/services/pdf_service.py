import re

from pypdf import PdfReader
from pathlib import Path


class PDFService():
    '''Service class for working with PDF file'''

    def __init__(self, path):
        self.reader = PdfReader(path)
        self.resume_dict = self.extract_data_as_dict()

    def extract_data_as_dict(self):
        '''Extract data from pdf file and group it into dict having section paragrapgh as keys'''
        reg_ex = r'\b[A-Z]+(?:[\s|&]+[A-Z]+)*\b'
        result = {}
        pages = self.reader.pages
        for page in pages:
            text = page.extract_text()
            paragraphs = [p for p in re.findall(reg_ex, text) if len(p) > 6] # generic paragraph length filter to omit abbreviations
            for index, paragraph in enumerate(paragraphs):
                start = text.index(paragraph)
                end = text.index(paragraphs[index + 1]) if index < len(paragraphs) - 1 else -1
                result[paragraph.lower()] = re.sub('\s+', ' ', text[start:end])
        return result

    def list_resume_sections(self):
        '''List all available sections from CV'''
        return self.resume_dict.keys() if self.resume_dict else None

    def get_appropriate_section(self, section_to_search):
        '''Get section info by given section name'''
        for section in self.list_resume_sections():
            if section_to_search in section:
                return section
        return None
