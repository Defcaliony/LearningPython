#Створили шаблон (Клас) | Created a template (class)
class LoginPage:

    def __init__(self, url):
            self.url = url #Запамятали адресу сторінки | Saved the page address

    def open_page(self):
        print(f"Відкриваємо браузер за адресою: {self.url}")


# Використовуємо шаблон (Створюємо обєкт) | We used a template and create an object
# Created an object for facebook
page1 = LoginPage("https://facebook.com")
# Created an object for Google
page2 = LoginPage("https://google.com")

# Coll an action/Triggering an action
page1.open_page() # It will output: Open the browser at the address: https://facebook.com
page2.open_page() # It will output: Open the browser at the address: https://google.com
