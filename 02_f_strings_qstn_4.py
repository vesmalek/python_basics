# Given a comma-separated string of tags like "python, django , fastapi, web ", split them into a clean list with no extra spaces.

tags = "python, django, , fastapi, web "
tags_formatted = [tag.strip() for tag in tags.split(",") if tag.strip()]

print(tags_formatted)
