def contains_programming_tag(tags):
    programming_languages = {"python", "ruby"}
    return len(programming_languages.intersection(set(tags))) > 0
