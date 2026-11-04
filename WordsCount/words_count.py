def word_counter():

    file = open("sample.txt", "r", encoding="utf-8")
    content = file.read()
    file.close()

    words = content.split()
    word_count = len(words)

    character_count = len(content)

    character_without_spaces = len(content.replace(" ", "").replace("\n", ""))

    sentence_count = 0

    for char in content:
        if char == "." or char == "!" or char == "?":
            sentence_count += 1

    longest_word = ""

    for word in words:
        word = word.strip(".,!?;:")

        if len(word) > len(longest_word):
            longest_word = word

    print("\n WORD COUNTER ")
    print(f"Total Words: {word_count}")
    print(f"Total Characters: {character_count}")
    print(f"Characters Without Spaces: {character_without_spaces}")
    print(f"Total Sentences: {sentence_count}")
    print(f"Longest Word: {longest_word}")

word_counter()
