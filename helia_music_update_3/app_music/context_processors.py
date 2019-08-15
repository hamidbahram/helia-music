from django.conf import settings

'''baray inke qabls az address file music {media} qarar bgire va
dar settings.py ('app_music.context_processors.get_settings_value',) 
dar qesmt context nvshte mishavd'''

def get_settings_value(request):
    return {'MEDIA_URL': settings.MEDIA_URL}