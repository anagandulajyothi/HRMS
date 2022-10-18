from homepage import Homepage

from time import sleep

from playwright.sync_api import Playwright, sync_playwright, expect

with sync_playwright () as p:
 browser = p.chromium.launch(headless=False)
 page = browser.new_page()
 page.goto('https://hrmsdev1.azurewebsites.net/')
 home_page = Homepage(page)
 sleep(5)
 home_page.Username.click()
 home_page.Username.fill("dotnethod@intonenetworks.com")
 sleep(10)
 home_page.password.fill("Password1!")
 sleep(15)
 home_page.login.click()
 sleep(20)

 browser.close()