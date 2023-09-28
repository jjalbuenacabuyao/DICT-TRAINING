englissh_to_spanish = {
    "hello": "hola",
    "goodbye": "adios",
    "cat": "gato",
    "dog": "perro",
    "food": "comida",
    "boy": "niño",
    "girl": "niña",
    "man": "hombre",
    "woman": "mujer",
    "I": "yo",
    "name": "llamo",
    "is": "es",
    "in": "en",
    "telephone": "telefono",
    "grandfather": "abuelo",
    "drink": "bebe",
    "milk": "leche",
    "orange": "naranja",
}


def translate_to_spanish(word: str):
    if word in englissh_to_spanish:
        return englissh_to_spanish[word]
    else:
        return "Translation not found"


word_to_translate = input("Enter an English word to translate to Spanish: ")

translation = translate_to_spanish(word_to_translate.lower())

print(f"The translation of {word_to_translate} is {translation}")
