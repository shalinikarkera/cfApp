"""creating_futures URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from user_admin import views
from user_student import views as s_views
from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    #path('',auth_views.LoginView.as_view(template_name='admin_login.html'),name='admin_login'),
    path('home/',views.home,name='home'),
    path('add_program/',views.add_program,name='add_program'),
    path('view_program/<int:pk>/add_module',views.add_module,name='add_module'),
    path('view_program/<int:pk>/add_module/<int:pk1>/add_level',views.add_level,name='add_level'),

    path('view_student/<int:pk>',views.view_student,name='view_student'),
    path('view_batch/<int:pk>',views.view_batch,name='view_batch'),
    path('view_center/<int:pk>',views.view_center,name='view_center'),
    path('view_questions/<int:pk>',views.view_questions,name='view_questions'),
    path('view_image_questions/<int:pk>',views.view_image_questions,name='view_image_questions'),
    path('view_images_questions/<int:pk>',views.view_images_questions,name='view_images_questions'),
    path('view_av_questions/<int:pk>',views.view_av_questions,name='view_av_questions'),
    path('view_av_questions/<int:pk>/view_av_sub_questions/<int:pk1>',views.view_av_sub_questions,name='view_av_sub_questions'),

    path('add_facilitator/',views.add_facilitator,name='add_facilitator'),
    path('add_center/',views.add_center,name='add_center'),
    path('add_student/',views.add_student,name='add_student'),
    path('add_program/',views.add_program,name='add_program'),
    path('add_batch/',views.add_batch,name='add_batch'),
    path('add_question/',views.add_question,name='add_question'),
    path('add_image_question/',views.add_image_question,name='add_image_question'),
    path('add_images_question/',views.add_images_question,name='add_images_question'),
    path('add_av_question/',views.add_av_question,name='add_av_question'),

    path('view_av_questions/<int:pk>/add_av_sub_question/',views.add_av_sub_question,name='add_av_sub_question'),
    path('view_av_questions/<int:pk>/edit_av_sub_question/<int:pk1>',views.edit_av_sub_question,name='edit_av_sub_question'),

    path('ajax/load_modules/',views.load_modules,name='load_modules'),
    path('ajax/load_levels/',views.load_levels,name='load_levels'),

    path('ajax/load_modules_home/',views.load_modules_home,name='load_modules_home'),
    path('ajax/load_fac_home/',views.load_fac_home,name='load_fac_home'),
    path('ajax/student_search/',views.student_search,name='student_search'),
    path('ajax/batch_search/',views.batch_search,name='batch_search'),



    path('delete_program/<int:pk>',views.delete_program,name='delete_program'),
    path('delete_module/<int:pk>',views.delete_module,name='delete_module'),
    path('delete_level/<int:pk>',views.delete_level,name='delete_level'),
    path('delete_facilitator/<int:pk>',views.delete_facilitator,name='delete_facilitator'),
    path('delete_student/<int:pk>',views.delete_student,name='delete_student'),
    path('delete_center/<int:pk>',views.delete_center,name='delete_center'),
    path('delete_batch/<int:pk>',views.delete_batch,name='delete_batch'),
    path('delete_question/<int:pk>',views.delete_question,name='delete_question'),
    path('delete_image_question/<int:pk>',views.delete_image_question,name='delete_image_question'),
    path('delete_images_question/<int:pk>',views.delete_images_question,name='delete_images_question'),
    path('delete_av_question/<int:pk>',views.delete_av_question,name='delete_av_question'),
    path('view_av_questions/<int:pk>/delete_av_sub_question/<int:pk1>',views.delete_av_sub_question,name='delete_av_sub_question'),


    path('password/',views.password,name='password'),
    path('centers/',views.centers,name='centers'),
    path('students/',views.students,name='students'),
    path('facilitators/',views.facilitators,name='facilitators'),
    path('batches/',views.batches,name='batches'),
    path('questions/',views.questionss,name='questions'),



    path('view_program/<int:pk>/view_module/<int:pk1>',views.view_module,name='view_module'),
    path('view_facilitator/<int:pk>',views.view_facilitator,name='view_facilitator'),
    path('view_program/<int:pk>/edit_module/<int:pk1>/view_level/<int:pk2>',views.view_level,name='view_level'),



    path('edit_batch/<int:pk>',views.edit_batch,name='edit_batch'),
    path('edit_question/<int:pk>',views.edit_question,name='edit_question'),
    path('edit_image_question/<int:pk>',views.edit_image_question,name='edit_image_question'),
    path('edit_images_question/<int:pk>',views.edit_images_question,name='edit_images_question'),
    path('edit_av_question/<int:pk>',views.edit_av_question,name='edit_av_question'),
    path('edit_facilitator/<int:pk>',views.edit_facilitator,name='edit_facilitator'),
    path('edit_center/<int:pk>',views.edit_center,name='edit_center'),
    path('edit_student/<int:pk>',views.edit_student,name='edit_student'),
    path('edit_program/<int:pk>',views.edit_program,name='edit_program'),
    path('view_program/<int:pk>/edit_module/<int:pk1>',views.edit_module,name='edit_module'),
    path('view_program/<int:pk>/edit_module/<int:pk1>/edit_level/<int:pk2>',views.edit_level,name='edit_level'),




    path('password_management_facilitators',views.password_management_facilitators,name='password_management_facilitators'),
    path('password_management_facilitator/<int:pk>',views.password_management_facilitator,name='password_management_facilitator'),
    path('password_management_students',views.password_management_students,name='password_management_students'),
    path('password_management_student/<int:pk>',views.password_management_student,name='password_management_student'),
    path('admin_login',views.LoginView1.as_view(),name='admin_login'),
    path('logout/',views.LogoutView1.as_view(),name='admin_logout'),





    path('',s_views.login,name='student_login'),
    path('s_home/<int:pk>/batch/<int:pk1>',s_views.s_home,name="s_home"),
    path('s_home/<int:pk>/batch/<int:pk1>/program/<int:pk2>',s_views.spoken_english,name="spoken_english"),
    path('video',s_views.video,name="video"),
    path('s_home/<int:pk>/batch/<int:pk1>/program/<int:pk2>/module/<int:pk3>/',s_views.module_view,name="module_view"),



    path('s_home/<int:pk>/batch/<int:pk1>/program/<int:pk2>/module/<int:pk3>/level/<int:pk4>/lesson/',s_views.lesson,name="lesson"),






    path('s_home/<int:pk>/batch/<int:pk1>/program/<int:pk2>/module/<int:pk3>/level/<int:pk4>/btest/',
    s_views.before_test,name="before_test"),

    path('s_home/<int:pk>/batch/<int:pk1>/program/<int:pk2>/module/<int:pk3>/level/<int:pk4>/standard_test/',
    s_views.standard_test,name="standard_test"),

        path('s_home/<int:pk>/batch/<int:pk1>/program/<int:pk2>/module/<int:pk3>/level/<int:pk4>/standard_test/ajax/test/',
        s_views.ajax_standard_test,name='ajax_standard_test'),

    path('s_home/<int:pk>/batch/<int:pk1>/program/<int:pk2>/module/<int:pk3>/level/<int:pk4>/image_test/',
    s_views.image_test,name="image_test"),

        path('s_home/<int:pk>/batch/<int:pk1>/program/<int:pk2>/module/<int:pk3>/level/<int:pk4>/image_test/ajax/test/',
        s_views.ajax_image_test,name='ajax_image_test'),

    path('s_home/<int:pk>/batch/<int:pk1>/program/<int:pk2>/module/<int:pk3>/level/<int:pk4>/av_test/',
    s_views.av_test,name="av_test"),

        path('s_home/<int:pk>/batch/<int:pk1>/program/<int:pk2>/module/<int:pk3>/level/<int:pk4>/av_test/ajax/test/',
        s_views.ajax_av_test,name='ajax_av_test'),

    path('s_home/<int:pk>/batch/<int:pk1>/program/<int:pk2>/module/<int:pk3>/level/<int:pk4>/test/submit/',
    s_views.test_submit,name="test_submit"),



]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

urlpatterns+=static(settings.MEDIA_URL2,document_root=settings.MEDIA_ROOT)
urlpatterns+=static(settings.MEDIA_URL4,document_root=settings.MEDIA_ROOT)
