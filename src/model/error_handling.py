from selenium.webdriver.common.by import By

def check_element(k,element):
   byDict = {
      1 : By.XPATH,
      2 : By.CLASS_NAME,
      3 : By.TAG_NAME
   }
   for x in xrange(1,3):
      if(x==k):
         try:
            driver.find_element(by=byDict.get(x),value=element)
         except NoSuchElementException:
            return False
   return True
