import random
import urllib.request
def downloader(imagem_url):
	file_name=random.randrange(1,1000)
	full_file_name=str(file_name)+ '.jpg'
	urllib.request.urlretrieve('https://gshow.globo.com/artistas/faustao/',full_file_name)
url='https://gshow.globo.com/artistas/faustao/'
downloader(url)

