import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def englishToFrench(englishText):
    """
        traduce da inglese a francese
    """
    if englishText == '':
        return ''
    frenchText= language_translator.translate(
        text=englishText,
        model_id='en-fr').get_result()

    return frenchText.get('translations')[0].get('translation')

def frenchToEnglish(frenchText):
    """
        traduce da francese a inglese
    """
    if frenchText == '':
        return ''
    englishText= language_translator.translate(
        text=frenchText,
        model_id='fr-en').get_result()

    
    return englishText.get('translations')[0].get('translation')