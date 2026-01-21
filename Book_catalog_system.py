books = []

def add_book():
    title = input("Enter book title: ")
    author = input("Enter author: ")
    books.append({"title": title, "author": author})
    print("Book added")

def view_books():
    if not books:
        print("No books available")
    else:
        for book in books:
            print("Title:", book["title"], "| Author:", book["author"])

def main():
    while True:
        print("1. Add Book")
        print("2. View Books")
        print("3. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            break
        else:
            print("Invalid option")

main()
