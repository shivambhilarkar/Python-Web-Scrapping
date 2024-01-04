import requests
from bs4 import BeautifulSoup


web_url = "https://realpython.github.io/fake-jobs/"


web_response = requests.get(web_url)
# print(web_response)
# print(web_response.content)

soup = BeautifulSoup(web_response.content, "html.parser")
# print soup object
# print(soup) 
# print in formatted lines
# print(soup.prettify())

# find() method return single element / node
result_container = soup.find(id = "ResultsContainer")
# print(result_container.prettify())

# find_all() method return array of elements / nodes
all_cards = result_container.find_all(class_ = "card")
for card in all_cards:
    job_title = card.find(class_ ="title is-5").text.strip()
    company_title = card.find(class_ ="subtitle is-6 company").text.strip()
    location = card.find(class_ ="location").text.strip()

    # access elements using css selectors
    card_footer = card.find_all("a")
    apply_here = card_footer[1]["href"]

    print(f"Company : {company_title} | Job Title : {job_title} | Location : {location} ")
    print(f"Apply here : {apply_here}")
    print("-------------------------------------------------------------------------------")

    
    