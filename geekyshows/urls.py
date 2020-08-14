"""geekyshows URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from course import views
from fees import views as feeViews
from fees.views import submit_fee
import course
# print('path', path('learnpy/', views.learn_py))
# used in small projects
# urlpatterns = [
#     path('learnpy/', views.learn_py),
#     path('admin/', admin.site.urls),
#     path('learndg/', views.learn_django),
#     path('', views.index),
#     path('fee/', feeViews.fee_home),
#     path('submitfee/', submit_fee)
# ]

# include function usage 1
# urlpatterns = [
#     path('',include('landing.urls')),
#     path('admin/', admin.site.urls),
#     path('cors/',include('course.urls'))
# ]

# include function usage 2

urlpatterns = [
    path('learnpy/', views.learn_py),
    path('admin/', admin.site.urls),
    path('cors/', include([
        path('', views.index),
        path('ld', views.learn_django),
        path('lp', views.learn_py)
    ]))

]


# include function usage 3

feepatterns=[
    path('',feeViews.fee_home),
    path('submit/',feeViews.submit_fee)
]

urlpatterns=[
    path('fee/',include(feepatterns))
]