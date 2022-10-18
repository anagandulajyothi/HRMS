class Homepage:

     def __init__(self, page):
      self.page = page
      self.Username = page.locator("//input[@id='Email']")
      self.password = page.locator("//input[@id='Password']")
      self.login = page.locator("//input[@id='btnSubmitlogin']")