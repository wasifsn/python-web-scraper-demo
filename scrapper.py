from bs4 import BeautifulSoup
import requests
from csv import writer
from random import choice
import pdb


response = requests.get("http://quotes.toscrape.com")

soup = BeautifulSoup(response.text, "html.parser")
quotes = soup.find_all(class_="quote")

quote_data = []
for quote in quotes:
    quote_text = quote.find(class_="text").get_text()
    quote_author = quote.find(class_="author").get_text()
    quote_url = quote.find("a")["href"]
    quote_url_final = f"http://quotes.toscrape.com{quote_url}"
    quote_data.append([quote_text, quote_author, quote_url_final])


def get_bio(url):
    response = requests.get(url)
    # response = requests.get("http://quotes.toscrape.com/author/Andre-Gide/")
    soup = BeautifulSoup(response.text, "html.parser")
    author_born_date = soup.find(class_="author-born-date").get_text()
    author_born_location = soup.find(class_="author-born-location").get_text()
    print(
        f"the first hint is: the Author was born {author_born_location} and on {author_born_date}")


def quit2():
    exit()


def continue_quiz():
    # breakpoint()
    continue_play = str(input("Do you want to continue, Press: y/n"))
    print(continue_play)
    if continue_play == "n":
        quit()
    elif continue_play == "y":
        quote_quiz()
    else:
        quit()


def quote_quiz():
    count = 4
    random_quote = choice(quote_data)
    print(random_quote)
    answer = input("Guess the Author of the quote!!")

    if answer == random_quote[1]:
        print("you guessed the correct answer")
        continue_quiz()
    elif answer != random_quote[1]:
        while answer != random_quote[1] or count > 0:
            # breakpoint()
            answer = input("Guess the Author of the quote!!")
            count -= 1
            print(count)
            if answer == random_quote[1]:
                print("you guessed the correct answer")
                continue_quiz()
            elif answer != random_quote[1] and count == 3:
                print("the answer is incorrect")
                print(f"you have {count} chances left")
                get_bio(random_quote[2])
            elif answer != random_quote[1] and count == 2:
                print("the answer is incorrect")
                print(f"you have {count} chances left")
                print(
                    f'the first letter of the author"s "first name is" {random_quote[1][0]}')
            elif answer != random_quote[1] and count == 1:
                print("the answer is incorrect")
                print(f"you have {count} chance left")
                print(
                    f'the total no of characters in the author"s "name is" {len(random_quote[1])}')
            else:
                continue_quiz()

    else:
        continue_quiz()


quote_quiz()
# quit2()

# print(continue_play)
# while continue_play == "y" or "Y":
#     print(continue_play)


# else:
# if continue_play == "y" or "Y":
#     print(continue_play)
#     quote_quiz()
# else:
#     quit()
