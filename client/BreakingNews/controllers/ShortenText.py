def ShortenText(text, size):
    words = text.split()
    print(len(words))
    if len(words) > size:
        return ' '.join(words[:size]) + '...'
    return text