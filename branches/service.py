from django.core.mail import send_mail

def send(user_email):
    send_mail(
        'Вы подписались на нашу рассылку!',
        'Мы будем присылать вам много сообщений',
        'suhomlinskylyceum@gmail.com',
        [user_email],
        fail_silently=False,
        )