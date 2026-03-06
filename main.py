from search import search_news
from analyze import analyze
from mail import send_mail

articles = search_news()

trend = analyze(articles)

send_mail(trend)

print("Trend mail sent")
