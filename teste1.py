import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://gabrielecirulli.github.io/2048/")

print(driver.title)
score = driver.find_element_by_class_name("score-container")
best = driver.find_element_by_class_name("best-container")
gameover = driver.find_element_by_class_name("game-message")
container  = driver.find_element_by_class_name("tile-container")

n=4
grid_preview = [0]*n
grid = []*n
for i in range(n):
    grid_preview[i] = [0]*n

grid = [0]*n
for i in range(n):
    grid[i] = [0]*n

body = driver.find_element_by_tag_name("body")

while (gameover.text==""):
    body.send_keys(Keys.ARROW_DOWN)
    body.send_keys(Keys.ARROW_LEFT)
    body.send_keys(Keys.ARROW_UP)
    body.send_keys(Keys.ARROW_RIGHT)
    time.sleep(0)

print ("Score = " + score.text)
print ("Best = " + best.text)
print ("Game over = " + gameover.text)

lista  = container.find_elements_by_css_selector(".tile")
for val in lista :
    celula = val.get_attribute("class")
    row = int(celula[celula.find('position-')+9:celula.find('position-')+10])-1
    col = int(celula[celula.find('position-')+11:celula.find('position-')+12])-1
    valor =  int(celula[celula.find('tile-')+5:celula.find('tile-p')-1])

    grid[col][row]=valor

for i in range(n):
    print(grid[i][:])
time.sleep(10)
driver.quit()