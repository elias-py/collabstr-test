from django.shortcuts import HttpResponse, render
from django.template.loader import render_to_string

from content_creator.models import Content, Creator


def index(request):
	return render(request, 'content_creator/index.html')


def filter_content(request):
	MAX_NUMBER_OF_CONTENT = 30
	
	platform_dict = {name: code for code, name in Creator.PLATFORM_CHOICES}
	platform = platform_dict[request.GET.get('platform')]
	
	contents = Content.objects.select_related('creator').filter(
		creator__platform=platform
	)[:MAX_NUMBER_OF_CONTENT]

	html = render_to_string(
		'content_creator/partials/content_list.html',
		{'contents': contents}
	)
	return HttpResponse(html)