# 19. Kutubxona xabari
def library_message(name, book="Noma’lum kitob"):
    return f"{name}, sizning kitobingiz: {book}"

# 20. Matnni qisqartirish
def shorten_text(text, limit=10):
    if len(text) > limit:
        return text[:limit] + "..."
    return text

# 21. Valyuta konvertatsiyasi
def convert_currency(amount, rate=1.0):
    return round(amount * rate, 2)

# 22. Foydalanuvchi darajasi
def get_level(name, score=0):
    if score >= 80:
        level = "Professional"
    elif score >= 40:
        level = "O‘rta"
    else:
        level = "Boshlovchi"
    return f"{name} - Daraja: {level}"

# 23. Matnni takrorlash
def repeat_text(text, times=2, separator=", "):
    return separator.join([text] * times)

# 24. Sana formatlash
def format_date(day, month, year=2025):
    return f"{day:02d}.{month:02d}.{year}"

# Testlar
print(library_message("Aziz", "Python for Beginners"))
print(shorten_text("Bu juda uzun matn bo'lib qoldi", 15))
print(convert_currency(100, 12.5))
print(get_level("Olim", 85))
print(repeat_text("Salom", 4, " | "))
print(format_date(17, 4))
