# problem 1

scraped_categories = ["Electronics", "Books", "electronics", "CLOTHING", "books", "Books"]

'''
the data contains the categories of products in an e-commerce store. 
The goal is to create a set comprehension that extracts unique categories from the list.
'''

scraped_categories_unique = {prod.lower() for prod in scraped_categories}
print(scraped_categories_unique)

# problem 2

messy_tags = [" #Python", "SQL", " python ", "data", "#sql", "AI", " ai "]

'''
Write a set comprehension that creates a set of unique, lowercase tags. 
It should remove the spaces and the # symbol.
'''

cleaned_tags = {tags.replace("$","").strip().lower() for tags in messy_tags if len(tags)>2}
print(cleaned_tags)


# problem 3

file_names = ["script.py", "data.CSV", "image.png", "report.csv", "MAIN.PY", "notes.txt"]

'''
Write a set comprehension that extracts just the unique, lowercase file extensions 
(e.g., 'py', 'csv', 'png', 'txt').
'''

extension_names = {extention.split(".")[-1] for extention in file_names}
print(extension_names)

