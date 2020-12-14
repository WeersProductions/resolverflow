def feature_contains_platform_tag(tags):
    platforms = ["windows", "linux", "apple"]
    for tag in tags:
        if tag in platforms:
            return True
    return False
