def feature_contains_programming_tag(tags):
    programming_languages = ["python", "ruby"]
    for tag in tags:
        if tag in programming_languages:
            return True
    return False
