
from pageobjects.Raiseticket_element import raiseticket

from pageobjects.homepage import Homepage
from time import sleep
#from Login import login

from playwright.sync_api import Playwright, sync_playwright, expect

with sync_playwright () as p:
 browser = p.chromium.launch(headless=False)
 page = browser.new_page()
 page.goto('https://hrmsdev1.azurewebsites.net/')
 home_page = Homepage(page)
 sleep(5)
 home_page.Username.click()
 home_page.Username.fill("dotnetemployee@intonenetworks.com")
 sleep(10)
 home_page.password.fill("Password1!")
 sleep(15)
 home_page.login.click()
 sleep(10)
 page.locator('input:has-text("No")').click()
 sleep(10)
 menu = raiseticket(page)
 menu.module.click()
 menu.modulename.click()
 


