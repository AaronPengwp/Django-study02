from django.shortcuts import render, HttpResponse, redirect, render_to_response
import time


# Create your views here.


def show_time(requset):
    # return HttpResponse("Hello")
    t = time.ctime()

    return render(requset, "index.html", {"t": t})  # locals()


def article_year(request, y):
    return HttpResponse(y)


def article_year_month(request, year, month):
    return HttpResponse("year:%s  month:%s" % (year, month))


def register(request):
    print(request.path)
    print(request.get_full_path())  # 把后面的路径参数也带上

    if request.method == "POST":
        print(request.POST.get("user"))
        print(request.POST.get("age"))
        user = request.POST.get("user")
        if user == "Aaron":
            return redirect("/login/") #直接跳转,url已经发生了变化

            # return render(request,"login.html",locals())#url还是register,当你刷新时又回到原来的了

        return HttpResponse("success!")

    # return render(request,"register.html")
    return render_to_response("register.html")


def login(request):
    name = "Aaron"

    return render(request, "login.html", locals())
