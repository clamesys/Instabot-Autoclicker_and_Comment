from instapy import InstaPy

session = InstaPy(username="d.sen17", password="clameclame") #headless_browser=True)
session.login()

comments = ['Truly Loved Your Post', 'Its awesome', 'Your Post Is inspiring']
session.set_do_comment(enabled=False, percentage=100)
session.set_comments(comments)

session.like_by_users(['spandan.spams'], amount=12)

session.end()