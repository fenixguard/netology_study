from datetime import datetime
from django.shortcuts import render
from django.views.generic import TemplateView
from django.conf import settings
from django.http import HttpResponseNotFound
import os


class FileList(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, date=None):
        files_list = os.listdir(settings.FILES_PATH)
        result = {'files': [], 'date': date}
        for item in files_list:
            file_info = os.stat(os.path.join(settings.FILES_PATH, item))
            file_data = {
                'name': item,
                'ctime': datetime.utcfromtimestamp(file_info.st_ctime),
                'mtime': datetime.utcfromtimestamp(file_info.st_mtime)
            }
            if date:
                if file_data['ctime'].date() == datetime.strptime(date, '%Y-%m-%d').date():
                    result['files'].append(file_data)
            else:
                result['files'].append(file_data)
        return result


def file_content(request, name):
    file_path = os.path.join(settings.FILES_PATH, name)
    if os.path.exists(file_path):
        with open(file_path, mode='r', encoding='utf8') as contents:
            file_contents = contents.read()
            return render(
                request,
                'file_content.html',
                context={'file_name': name, 'file_content': file_contents}
            )
    else:
        return HttpResponseNotFound('404. Not found')

