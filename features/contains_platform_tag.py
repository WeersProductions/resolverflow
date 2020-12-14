def contains_platform_tag(tags):
    platforms = {"windows", "linux", "apple"}
    return len(platforms.intersection(set(tags))) > 0
