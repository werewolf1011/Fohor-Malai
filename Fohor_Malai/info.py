EMAIL_USE_TLS = True
EMAIL_HOST = "smtp.gmail.com"
EMAIL_HOST_USER = "your_email@gmail.com"
EMAIL_HOST_PASSWORD = "<your_email_host_password>" # less secureapp password
EMAIL_PORT = 587
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
