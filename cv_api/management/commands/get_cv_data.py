from pathlib import Path

from django.core.management.base import BaseCommand

from cv_api.services.pdf_service import PDFService


file_path = Path().parent.joinpath('dummy_resume.pdf')


class Command(BaseCommand):
    help = """Get data about a CV"""

    def add_arguments(self, parser):
        parser.add_argument('section', nargs='+', type=str)

    def handle(self, *args, **options):
        pdf_service = PDFService(file_path)
        for section in options["section"]:
            cv_section = pdf_service.get_appropriate_section(section)
            section_data = pdf_service.resume_dict.get(cv_section)
            if section_data:
                self.stdout.write(self.style.SUCCESS(f'  -{section_data}'), ending='\n\n')
            else:
                self.stderr.write(self.style.ERROR(f'Section "{section}" not found.'))
