
import webbrowser
import time


import random
while True:
    sites= random.choice(["xvideos.com", "Pornhub.com", "xnxx.com",'Fish4hoes.com', 'www.zzcartoon.com', 'hentaigames.porn', 'sitesofporn.com/virtualrealporn.com'])
    visit = "http://{}".format(sites)
    webbrowser.open(visit)
    seconds = random.randrange(5, 10,)
    time.sleep(seconds)
