from googletrans import Translator

def translator_func(lang, text):
    translator = Translator()
    translated_text = translator.translate(text, dest=lang)
    return translated_text.text
