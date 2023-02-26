import requests
import time
#IMPORTAR O BS4
#REALIZAR MODIFICAÇÕES

def download_image_jpg(parse_url):
    img_bytes = requests.get(listas_url).content
    img_name = listas_url.split('/')[3]
    img_name = f'{img_name}.jpg'
    if img_name == '.jpg':
        print("Not Found")
    else:
         with open(img_name, 'wb') as img_file:
          img_file.write(img_bytes)
          print('Found')
          print(f'{img_name} was downloaded...')
def download_image_png(parse_url):
     img_bytes = requests.get(listas_url).content
    img_name = listas_url.split('/')[3]
    img_name = f'{img_name}.png'
    if img_name == '.png':
        print("Not Found")
    else:
         with open(img_name, 'wb') as img_file:
          img_file.write(img_bytes)
          print('Found')
          print(f'{img_name} was downloaded...')
    
def verify_dir(parse_url):
    dir_name_spli = parse_url.split('m/')[0]
    dir_name = dir_name_spli+'m'
    print(dir_name)
verify_dir('https://images.unsplash.com/photo-1516117172878-fd2c41f4a759')





