from pathlib import Path

from rest_framework import views
from rest_framework import status
from rest_framework.response import Response

from cv_api.serializers import CVSerializer
from cv_api.services.pdf_service import PDFService


file_path = Path().parent.joinpath('dummy_resume.pdf')

class CVDataAPIView(views.APIView):
    '''Api view which displays CV data depending on url'''

    def get(self, request, *args, **kwargs):
        get_section = request.get_full_path().strip('/').split('/')[-1]
        pdf_service = PDFService(file_path)

        if get_section == 'all':
            if not pdf_service.list_resume_sections():
                # return not found error when no sections where found in the CV
                return Response({'message': 'CV data not found'}, status=status.HTTP_404_NOT_FOUND)
            serializer = CVSerializer(data=pdf_service.resume_dict)
        else:
            cv_section = pdf_service.get_appropriate_section(get_section)
            if not cv_section:
                # return not found error when requested section was not found
                return Response({'message': 'Section info not found'}, status=status.HTTP_404_NOT_FOUND)
            section_data = pdf_service.resume_dict.get(cv_section)
            serializer = CVSerializer(data={cv_section: section_data})

        serializer.is_valid()

        return Response(serializer.data, status=status.HTTP_200_OK)
