import eel
from translations import translator_func


@eel.expose
def result_search(text, lang):
    translated_text = translator_func(lang, text)
    return translated_text


eel.init("web")
eel.start("main.html", size=(1920, 1080), resizable=False)