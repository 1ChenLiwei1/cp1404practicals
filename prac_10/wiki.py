import wikipedia
title = input("Enter page title: ")
while title != "":
    try:
        page = wikipedia.page(title)
        print("Title", page.title)
        print("Summary", page.summary)
    except wikipedia.DisambiguationError as e:
        print("We need a more specific title. Try one of the following, or a new search:")
        print("(BeautifulSoup warning)")
        options = e.options
        for i, option in enumerate(options, start=1):
            print(f"{i}. {option}")
        print()
    except wikipedia.PageError:
        print(f"Page id {title} does not match any pages. Try another id!")
        print()
    title = input("Enter page title: ")
print("Thank you.")