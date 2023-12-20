import json

from django.core.management.base import BaseCommand

from content_creator.models import Content, Creator


class Command(BaseCommand):
	help = 'Load a list of creators and their content from a JSON file.'

	def add_arguments(self, parser):
		parser.add_argument('json_file', type=str, help="Path to JSON file containing the data")

	def handle(self, *args, **kwargs):
		json_file = kwargs['json_file']
		platform_dict = {name: code for code, name in Creator.PLATFORM_CHOICES}

		with open(json_file, 'r') as file:
			creators_data = json.load(file)

			for creator_data in creators_data:
				creator, created = Creator.objects.get_or_create(
					name=creator_data['name'],
					username=creator_data['username'],
					defaults={
						'rating': creator_data['rating'],
						'platform': platform_dict[creator_data['platform']]
					}
				)

				Content.objects.create(
					creator=creator,
					url=creator_data['content']
				)
		self.stdout.write(self.style.SUCCESS('Successfully populated data from JSON file.'))