import webbrowser


def validator(func):        #декоратор\decorator<
    def wrapper(url):
        #print("Before")
        if "." in url:     #chek for the "."
            func(url)
        #func(url)
        #print("After")
        else:
            print("The link is incorrect") #url invalid
    return wrapper          # >decorator


@validator  #vrite to active decorator
def open_url(url):
    webbrowser.open(url)


open_url('https://itproger.com/ua')
