import ezgmail

# ezgmail.send('yukimargoulin@gmail.com', "coucou", 'tu vas bien?')

# GmailThread objects
# unread_threads: list = ezgmail.unread()
# function that display a summary
# ezgmail.summary(unread_threads)

# Searching mail
# result_threads: list = ezgmail.search('subject:coucou')
# ezgmail.summary(result_threads)

# Downloading attachments
threads = ezgmail.search("Claire")
print(threads[0].messages[1].attachments)
threads[0].messages[1].downloadAttachment(
    "p415 Al Sweigart - Automate The Boring Stuff With Python_ Practical"
    " Programming For Total Beginners-No Starch Press (2019).pdf"
)
