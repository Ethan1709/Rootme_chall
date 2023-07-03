from bs4 import BeautifulSoup
import requests
import operator

operator_dict = {
    '+': operator.add,
    '-': operator.sub,
}

url = 'http://challenge01.root-me.org/programmation/ch1/'
target_url = 'http://challenge01.root-me.org/programmation/ch1/ep1_v.php?result='

cookies = None

headers = {}
if cookies:
    headers['Cookie'] = cookies

response = requests.get(url, headers=headers)
html_content = response.text

# Extract and store the cookies from the initial response
if not cookies:
    cookies = response.headers.get('Set-Cookie')

soup = BeautifulSoup(html_content, 'html.parser')

text = soup.get_text()

text_split = text.split('\n')

suit = text_split[0]
second_line = text_split[1]
third_line = text_split[2]

suit_split = suit.split(' ')
first_number = int(suit_split[3])
print(first_number)
n = suit_split[9]
op = operator_dict.get(suit_split[7])
print(type(op))
second_number = int(suit_split[11])
print(n)
print(second_number)

U_O_split = second_line.split(' ')
U_0 = int(U_O_split[2])
print(U_0)

suit_find = third_line.split(' ')
numb_to_find = suit_find[3]
numb_to_find = int(numb_to_find[1:-3])
print(numb_to_find)

print(suit)
print(second_line)
print(third_line)

for i in range(1, numb_to_find + 1):
    res = op((first_number + U_0), ((i - 1) * second_number))
    U_0 = res
print(res)

params = {'result': res}

# Include cookies in the headers for subsequent requests
headers = {'Cookie': cookies}

final_response = requests.get(target_url, params=params, headers=headers)
print(final_response.text)
