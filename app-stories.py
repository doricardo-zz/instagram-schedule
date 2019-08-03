import time
from instapy_cli import client
from datetime import datetime
import sys
import os
from pathlib import Path

def main():
	username = sys.argv[1]
	password = sys.argv[2]
	minutos = sys.argv[3]

	image_files = liststories(username);

	print(image_files)

	with client(username, password) as cli:
		for i in range(0, len(image_files)):
			#print('image: ', image_files[i])
			folder = Path("stories")
			imagem = str(folder) + "/" + image_files[i]
			res = cli.upload(imagem, '#motivacional', story=True)
			#print('IG: >> ', res)
			print('{0} posted image {1} waiting {2} minutos ...'.format(datetime.today(), image_files[i], minutos))
			time.sleep(60*int(minutos))

def liststories(username='doricardo'):
	posts = [story.rstrip('\n') for story in open('stories-'+username+'.txt')]
	#for post in posts:
	#	imagem, minuto = post.split('|')
	return posts

main()