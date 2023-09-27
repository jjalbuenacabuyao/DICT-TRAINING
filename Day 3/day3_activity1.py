programming_languages = ["C", "C++", "C#", "Python", "Java", "JavaScript", "Pascal", "Haskel", "Erlang", "F#", "Go"]

programming_languages.append("Carbon")
programming_languages.append("TypeScript")

def ProgrammingLanguagePrinter():
    count = 0
    for programming_language in programming_languages:
        print(f"Programming language #{count}: {programming_language}")

ProgrammingLanguagePrinter()
ProgrammingLanguagePrinter()