### ✅ **Solution: Favorite Books Organizer**

```python
# 1. Create a list of favorite books
favorite_books = ["The Hobbit", "1984", "To Kill a Mockingbird", "Pride and Prejudice", "The Great Gatsby"]

# 2. Print the first and last book
print("First book:", favorite_books[0])
print("Last book:", favorite_books[-1])

# 3. Add a new book to the list
favorite_books.append("Moby Dick")
print("After append:", favorite_books)

# 4. Insert a book at the second position
favorite_books.insert(1, "Brave New World")
print("After insert:", favorite_books)

# 5. Remove one book from the list
favorite_books.remove("1984")
print("After removal:", favorite_books)

# 6. Sort the list alphabetically
favorite_books.sort()
print("Sorted list:", favorite_books)

# 7. Convert the list to a tuple
books_tuple = tuple(favorite_books)
print("Books tuple:", books_tuple)

# 8. Try to change one element in the tuple (this will raise an error if uncommented)
# books_tuple[0] = "New Title"  # ❌ TypeError: 'tuple' object does not support item assignment

# 9. Loop through the tuple and print each book
print("Books in tuple:")
for book in books_tuple:
    print("-", book)
```

---

### ⭐ **Bonus Challenge:**

```python
# Count how many books contain "the" (case-insensitive)
count = 0
for book in books_tuple:
    if "the" in book.lower():
        count += 1
print('Books containing "the":', count)

# Slice the tuple to get the middle 3 books (if available)
mid_books = books_tuple[2:5]  # Adjust based on length if needed
print("Middle 3 books:", mid_books)
```

---
