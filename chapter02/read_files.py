import os
import codecs


def read_text_files(directory: str) -> list[str]:
    files = os.listdir(directory)
    text_list = []
    for filename in files:
        if not filename.startswith("."):
            f = codecs.open(
                directory + filename, "r", encoding="ISO-8859-1", errors="ignore"
            )
            text_list.append(f.read())
            f.close()

    return text_list
