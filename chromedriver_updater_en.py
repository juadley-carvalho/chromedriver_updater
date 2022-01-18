from urllib.request import urlretrieve as download
import requests
import zipfile
import os


class ChromeDriverUpdater(object):
    def __init__(self):
        return None

    # RETURNS THE LAST VERSION FROM CHROMEDRIVER WEBSITE, BASED ON INSTALLED CHROME BROWSER VERSION
    def lastVersion(self, version):
        url = 'https://chromedriver.storage.googleapis.com/LATEST_RELEASE_' + str(version)
        return requests.get(url).text

    def update(self, directory):
        # CHECKS INSTALLED CHROME BROWSER VERSION
        print('Checking Chrome Browser version...')

        chrome = os.popen(r'reg query "HKEY_CURRENT_USER\Software\Google\Chrome\BLBeacon" /v version').read()
        version = chrome.split(' ')[-1].split('.')[0]

        print(f'Version: {version}')

        # DOWNLOAD CHROMEDRIVER COMPATIBLE WITH INSTALLED CHROME BROWSER VERSION
        print('Downloading compatible ChromeDriver...')

        download(f'https://chromedriver.storage.googleapis.com/{self.lastVersion(version)}/chromedriver_win32.zip',
                 f'{directory}/chromedriver_win32.zip')

        # UNPACK CHROMEDRIVER EXE (REPLACES THE OLD ONE)
        print('Unpacking file...')

        with zipfile.ZipFile(f'{directory}/chromedriver_win32.zip', 'r') as zip_ref:
            zip_ref.extractall(directory)

        # DELETE ZIP FILE
        print('Deleting zip file...')

        files = os.listdir(directory)
        for file in files:
            if file == 'chromedriver_win32.zip':
                os.remove(f'{directory}/{file}')
                break

        print('Update finished!')


updater = ChromeDriverUpdater()

updater.update('./ChromeDriver_Directory')