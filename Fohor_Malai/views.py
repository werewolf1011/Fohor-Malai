from django.http import HttpResponse
from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login

from django.core.mail import EmailMessage, send_mail
from django.conf import settings


from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str

# from django.utils.encoding import force_bytes, force_text
from .tokens import generate_token

from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as django_logout
from django.contrib.auth.decorators import login_required

from complaints.models import Complaints
from cards.models import News_Blog


def home(request):
    news_blog_data = News_Blog.objects.all().order_by("-created_at")[:3]
    data = {"cards": news_blog_data}

    return render(request, "index.html", data)


def news_blog(request):
    news_blog_details = News_Blog.objects.all()
    data = {"news_blog_details": news_blog_details}

    return render(request, "news_blog.html", data)


def preview(request):
    previews = Complaints.objects.all().order_by("-created_at")
    st = request.GET.get("search")
    
    if st:
        previews = Complaints.objects.filter(complainer_name__icontains=st)
        
    data = {"previews": previews}
        
    return render(request, "Complain-feed.html", data)



def contact(request):
    return HttpResponse("This is contact page")


def signup(request):

    if request.method == "POST":
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")
        confirmPassword = request.POST.get("confirmPassword")

        if User.objects.filter(username=username):
            messages.error(request, "User already exists")
            return redirect("signup")

        if User.objects.filter(email=email):
            messages.error(request, "Email already registered")
            return redirect("signup")

        if len(username) > 10:
            messages.error(
                request, "Username must be less than or equal to 10 characters"
            )
            return redirect("signup")

        if password != confirmPassword:
            messages.error(
                request, "Confirm Password does not match with the Password."
            )
            return redirect("signup")

        if not (any(c.isalpha() for c in username) and any(c.isdigit() for c in username)):
            messages.error(
                request, "Username should contain both alphabetic and numeric characters."
            )
            return redirect("signup")


        my_user = User.objects.create_user(username, email, password)
        my_user.first_name = firstname
        my_user.last_name = lastname
        my_user.is_active = False

        my_user.save()

        # Send email confirmation
        current_site = get_current_site(request)
        email_subject = "Confirm your Email @ फोहोर🚮मलाइ - User Login!!"
        message2 = render_to_string(
            "email_confirmation.html",
            {
                "name": my_user.first_name,
                "domain": current_site.domain,
                "uid": urlsafe_base64_encode(force_bytes(my_user.pk)),
                "token": generate_token.make_token(my_user),
            },
        )
        email = EmailMessage(
            email_subject,
            message2,
            settings.EMAIL_HOST_USER,
            [my_user.email],
        )
        email.fail_silently = True
        email.send()

        messages.success(
            request, "Please check your email to confirm your registration."
        )
        return redirect("home")

    return render(request, "signup.html")


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        my_user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        my_user = None

    if my_user is not None and generate_token.check_token(my_user, token):
        my_user.is_active = True
        my_user.save()
        my_user.backend = "django.contrib.auth.backends.ModelBackend"
        messages.success(request, "Your Account has been activated!!")
        return redirect("home")
    else:
        return render(request, "activation_failed.html")


def user_login(request):
    try:
        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return render(request, "Complaint.html")

            else:
                messages.error(request, "Bad credentials")
                return redirect("login")

    except Exception as e:
        print(e)
        pass

    return render(request, "login.html")


def my_logout(request):
    django_logout(request)
    # messages.success(request, "Successfully logged out")
    return redirect("home")


@login_required
def complaint(request):
    try:
        if request.method == "POST":
            name = request.POST.get("complainer_name")
            address = request.POST.get("complainer_address")
            phone = request.POST.get("complainer_phone")
            waste_type = request.POST.get("waste_type")
            image = request.FILES.get("image")
            complaint_desc = request.POST.get("complaint_desc")

            # Setting a default value for complaint status
            complain_status = "pending"

            details = Complaints(
                complainer_name=name,
                complainer_address=address,
                complainer_phone=phone,
                waste_type=waste_type,
                image=image,
                complaint_desc=complaint_desc,
                complain_status=complain_status,
            )
            details.save()
            messages.success(request, "Complaint submitted successfully!")
            return redirect("home")

    except Exception as e:
        print(e)

    # return render(request, "complain.html")

    return render(request, "Complaint.html")
