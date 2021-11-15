from django.urls import path


from .views import (homepageview,ContactCreateView,XabarPageView,
AdminPanelView,
BarchaXaridorlarView,
XaridorCreateView,
XaridorXaqida,
XaridorUpdateView,
XaridorDeleteView,
CreateTovar,
TovarXaqida,
CreateCategory,
KategoriyalarView,
KategoriyaUpdateView,
KategoriyaDeleteView,
TovarUpdateView,
TovarDeleteView,
CreateTolov,
XisobotlarView)

urlpatterns = [
    path('adminpanel/Tolovlar/Xisobot/',XisobotlarView.as_view(),name='xisobot'),
    path('adminpanel/Tolovlar/tolovqilish/',CreateTolov.as_view(),name='createTolov'),
    path('adminpanel/Tovarlar/tovar/<int:pk>/delete',TovarDeleteView.as_view(),name='tovarDelete'),
    path('adminpanel/Tovarlar/tovar/<int:pk>/tahrirlash',TovarUpdateView.as_view(),name='tovarEdit'),
    path('adminpanel/Tovarlar/tovar/<int:pk>/',TovarXaqida.as_view(),name='tovarXaqida'),
    path('adminpanel/Tovarlar/tovar/new',CreateTovar.as_view(),name='createTovar'),
    path('adminpanel/Kategoriyalar/Kategoriya/<int:pk>/delete',KategoriyaDeleteView.as_view(),name='kategoriyaDelete'),
    path('adminpanel/Kategoriyalar/Kategoriya/<int:pk>/tahrirlash',KategoriyaUpdateView.as_view(),name='kategoriyaEdit'),
    path('adminpanel/Kategoriyalar/Kategoriya/new',CreateCategory.as_view(),name='createCategory'),
    path('adminpanel/Kategoriyalar/',KategoriyalarView.as_view(),name='Kategoriyalar'),
    path('adminpanel/Xaridorlar/xaridor/<int:pk>/delete',XaridorDeleteView.as_view(),name='xaridorDelete'),
    path('adminpanel/Xaridorlar/xaridor/<int:pk>/tahrirlash',XaridorUpdateView.as_view(),name='xaridorEdit'),
    path('adminpanel/Xaridorlar/xaridor/<int:pk>/',XaridorXaqida.as_view(),name='xaridorXaqida'),
    path('adminpanel/Xaridorlar/xaridor/new/',XaridorCreateView.as_view(),name='createXaridor'),
    path('adminpanel/BarchaXaridorlar/',BarchaXaridorlarView.as_view(),name='BarchaXaridorlar'),
    path('adminpanel/',AdminPanelView.as_view(),name='adminpanel'),
    path('adminpanel/xabarlar/',XabarPageView.as_view(),name='xabarlar'),
    path('',ContactCreateView.as_view(), name='home'),

    
]
