letter_scores = {
    1: "АВЕИНОРСТ",
    2: "ДКЛМПУ",
    3: "БГЁЬЯ",
    4: "ЙЫ",
    5: "ЖЗХЦЧ",
    8: "ШЭЮ",
    10: "ФЩЪ"
}

score_map = {}
for points, letters in letter_scores.items():
    for letter in letters:
        score_map[letter] = points

word = input("Введите слово: ").upper()
total_score = 0

for letter in word:
    total_score += score_map.get(letter, 0)

print("Стоимость слова:", total_score)
