def count_vowels(text):
    count = 0
    for char in text.lower():
        if char in "aeiou":
            count += 1
    return count

def count_consonants(text):
    count = 0
    for char in text.lower():
        if char.isalpha() and char not in "aeiou":
            count += 1
    return count

# ---- Funciones a implementar ----

def total_letters(text):
    vowels = count_vowels(text)
    consonants = count_consonants(text)
    return vowels + consonants

def vowel_percentage(text):
    vowels = count_vowels(text)
    total = total_letters(text)

    if total == 0:
        return 0.0

    percentage = (vowels / total) * 100
    return round(percentage, 1)

def analyze_text(text):
    vowels = count_vowels(text)
    consonants = count_consonants(text)
    total = total_letters(text)
    percentage = vowel_percentage(text)

    return f"V:{vowels} C:{consonants} T:{total} P:{percentage}%"
