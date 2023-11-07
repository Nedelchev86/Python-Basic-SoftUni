
book = input()
count = 0
is_book_found = False

search_for = input()
while search_for != "No More Books":
    if search_for == book:
        is_book_found = True
        print(F"You checked {count} books and found it.")
        break
    count += 1
    search_for = input()
if not is_book_found:
    print(F"The book you search is not here!")
    print(F"You checked {count} books.")