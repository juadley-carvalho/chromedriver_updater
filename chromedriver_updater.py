from urllib.request import urlretrieve as download
import requests
import zipfile
import os


class AtualizadorChromeDriver(object):
    def __init__(self):
        return None

    # RETORNA ÚLTIMA VERSÃO DO SITE, DE ACORDO COM A VERSÃO DO CHROME INSTALADO
    def ultimaVersao(self, versao):
        url = 'https://chromedriver.storage.googleapis.com/LATEST_RELEASE_' + str(versao)
        return requests.get(url).text

    def atualizar(self, diretorio):
        # VERIFICA VERSÃO DO CHROME INSTALADO
        print('Verificando versão atual do Chrome...')

        chrome = os.popen(r'reg query "HKEY_CURRENT_USER\Software\Google\Chrome\BLBeacon" /v version').read()
        versao = chrome.split(' ')[-1].split('.')[0]

        print(f'Versão: {versao}')

        # BAIXA CHROMEDRIVER COMPATÍVEL COM A VERSÃO DO CHROME INSTALADO
        print('Baixando versão compatível do ChromeDriver...')

        download(f'https://chromedriver.storage.googleapis.com/{self.ultimaVersao(versao)}/chromedriver_win32.zip',
                 f'{diretorio}/chromedriver_win32.zip')

        # DESCOMPACTA EXECUTÁVEL DO CHROMEDRIVER (SUBSTITUI O ARQUIVO ANTIGO)
        print('Descompactando arquivo...')

        with zipfile.ZipFile(f'{diretorio}/chromedriver_win32.zip', 'r') as zip_ref:
            zip_ref.extractall(diretorio)

        # EXCLUI ARQUIVO ZIP
        print('Excluindo arquivo zip...')

        arquivos = os.listdir(diretorio)
        for arquivo in arquivos:
            if arquivo == 'chromedriver_win32.zip':
                os.remove(f'{diretorio}/{arquivo}')
                break

        print('Atualização finalizada!')


atualizador = AtualizadorChromeDriver()

atualizador.atualizar('./ChromeDriver_Directory')