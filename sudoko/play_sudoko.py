from advanced_sudoko import Advanced_Sudoko
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get("http://www.sudoku.com/")
#htmlElement = browser.find_element_by_tag_name("body")

#input("Press enter to begin.")

cells = browser.find_elements_by_class_name("cell")
board = []
temp = []
for i in range(len(cells)):
    if i % 9 == 0:
        board.append(temp)
        temp = []
    try:
        temp.append(int(cells[i].text))
    except:
        temp.append(cells[i].text)
board.append(temp)
board = board[1:]
s = Advanced_Sudoko(board)
#print(s)
s.play_game()
#print(s)
for i in range(len(cells)):
    a = i//9
    b = i-(9*a)
    if cells[i].text == " ":
        cells[i].click()
        cells[i].send_keys(str(s.board[a][b]))

