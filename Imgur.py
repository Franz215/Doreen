import matplotlib
matplotlib.use('Agg')
import datetime
from imgurpython import ImgurClient
client_id = '518d1b40a39841f'
client_secret = '68b395efbfb5ff1f85ccaec5d5007c8e0b953e60'
album_id = 'R9E5P5x'
access_token = '18c05af7b28cd86a61b3bd76d5ddca0a3ebde005'
refresh_token = '42c042a450eb86f7f8699002137d841d5579c876'

def showImagur(fileName):
    client = ImgurClient(client_id, client_secret, access_token, refresh_token)

    config = {
        'album': album_id,
        'name': fileName,
        'title': fileName,
        'description': str(datetime.date.today())
        }
    
    try:
        print("[log:INFO]Done upload. ")
        imgurl = client.upload_from_path(fileName+'.png', config-config, anon=False)['link']
        print("[log:INFO]Done upload ! ")
    except:
        imgurl = 'https://imgur.com/RQUdSTk'
        print("[log:ERROR]Unable upload")
    