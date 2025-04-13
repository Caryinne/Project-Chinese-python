def get_words_for_table():
    words = []
    with open("./data/words.csv", "r", encoding="utf-8") as f:
        cnt = 1
        for line in f.readlines()[1:]:
            word, transcription, translation, source = line.split(";")
            words.append([cnt, word, transcription, translation])
            cnt += 1
    return words


def write_word(new_word, new_transcription, new_translation):
    new_word_line = f"{new_word};{new_transcription};{new_translation};user"
    with open("./data/words.csv", "r", encoding="utf-8") as f:
        existing_words = [l.strip("\n") for l in f.readlines()]
        title = existing_words[0]
        old_words = existing_words[1:]
    words_sorted = old_words + [new_word_line]
    words_sorted.sort()
    new_words = [title] + words_sorted
    with open("./data/words.csv", "w", encoding="utf-8") as f:
        f.write("\n".join(new_words))


def get_words_stats():
    db_words = 0
    user_words = 0
    words_len = []
    with open("./data/words.csv", "r", encoding="utf-8") as f:
        for line in f.readlines()[1:]:
            word, transcription, translation, added_by = line.split(";")
            words_len.append(len(word))
            if "user" in added_by:
                user_words += 1
            elif "db" in added_by:
                db_words += 1

    characters_all = 0
    db_chars = 0
    user_chars = 0

    with open("./data/characters.csv", "r", encoding="utf-8") as f:
        for line in f.readlines()[1:]:
            character, pinyin, tone, meaning, source = line.split(";")
            characters_all += 1
            if "user" in source:
                user_chars += 1
            elif "db" in source:
                db_chars += 1
    stats = {
        "words_all": db_words + user_words,
        "words_own": db_words,
        "words_added": user_words,
        "characters_all": characters_all,
        "characters_own": db_chars,
        "characters_added": user_chars,
    }
    return stats
