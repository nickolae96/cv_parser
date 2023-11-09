from rest_framework import serializers


class CVSerializer(serializers.Serializer):
    '''Serializer for CV data'''

    def __init__(self, *args, **kwargs):
        data = kwargs.get('data', {})
        super().__init__(*args, **kwargs)

        for key in data.keys():
            self.fields[key] = serializers.CharField()
