# Given a blog post title like "My Journey to Python Web Development", build a URL slug from it.

url_slug = "My Journey to Python Web Development".lower().replace(" ", "-")

print(f"URL Slug: {url_slug}")