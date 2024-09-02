from plyer import notification
import time
import random

quoteList = ["Quote 1", "Quote 2", "Quote 3", "Quote 4", "Quote 5"]

for i in range(5):

    #generates a random quote index
    pick = random.randint(0, len(quoteList)-1)
    quote = quoteList[pick]
    #notification generator
    notification.notify(
        title = "Daily Quote",
        message = quote,
        app_name = "Quote Notifier",
        timeout = "5"
    )
    time.sleep(5)