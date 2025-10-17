import locale
from collections import defaultdict

input_file = "en-ru.txt"
output_file = "ru-en.txt"

ru_en_dict = defaultdict(list)

with open(input_file, encoding="utf-8") as f:
    for line in f:
        if " - " in line:
            en_word, ru_part = line.strip().split(" - ")
        elif " – " in line:
            en_word, ru_part = line.strip().split(" – ")
        else:
            continue

        ru_words = [word.strip() for word in ru_part.split(",")]
        for ru_word in ru_words:
            ru_en_dict[ru_word].append(en_word)

locale.setlocale(locale.LC_ALL,'ru_RU.utf8')

with open(output_file, "w", encoding="utf-8") as f:
    for ru_word in sorted(ru_en_dict, key=locale.strxfrm):
        translations = ", ".join(sorted(set(ru_en_dict[ru_word])))
        f.write(f"{ru_word} – {translations}\n")
