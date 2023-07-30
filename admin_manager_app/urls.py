#path関数をインポート
from django.urls import path
# 同ディレクトリからview.pyをインポート
from . import views

#path関数(アクセスするアドレス、呼び出す処理)を追記
urlpatterns = [
    path('views', views.index, name='index'),
    path('', views.index, name='index'),
    path('form', views.FormView.as_view(), name='form'),
    path('register', views.AccountRegistration.as_view(), name='register'),
    path("logout",views.Logout,name="logout"),
    path('login',views.Login,name='login'),
    
]