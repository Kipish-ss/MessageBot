def convert_text(text: str, dict):
    if text.isnumeric():
        new_word = []
        for num in text:
            new_word.append(dict[num])
        return "".join(new_word)
    list_index: list[int] = []
    for i in range(len(text)):
        if text[i].isupper():
            list_index.append(i)
    text = text.lower()
    new_word = list(dict[text])
    for i in list_index:
        if i < len(new_word):
            new_word[i] = new_word[i].upper()
    new_word = "".join(new_word)
    return new_word
