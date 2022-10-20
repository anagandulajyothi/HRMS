class raiseticket:


     def __init__(self, page):
      self.page = page
      self.module = page.locator("//span[normalize-space()='Raise Ticket']")
      self.modulename = page.locator("#btnAddNewTicket")
      self.department = page.locator("#ddlDept")
      self.severity = page.locator("#ddlSeverity")
      self.Tickettype = page.locator("#txtProblemType")
      self.Ticketsummary = page.locator("#txtProblemSummary")
     
