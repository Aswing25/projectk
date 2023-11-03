from django.contrib import admin
from django.urls import path

from kapp import views

urlpatterns = [
    path('indexpage/',views.indexpage,name="indexpage"),
    path('studentpage/',views.studentpage,name="studentpage"),
    path('employepage/',views.employepage,name="employepage"),
    path('employesave/',views.employesave,name="employesave"),
    path('disdisplayemploy',views.displayemploy,name="displayemploy"),
    path('displaystudent/',views.displaystudent,name="displaystudent"),
    path('studentsave/',views.studentsave,name="studentsave"),
    path('categorypage/',views.categorypage,name="categorypage"),
    path('displaycategory/',views.displaycategory,name="displaycategory"),
    path('categorysave/',views.categorysave,name="categorysave"),
    path('edit_category/<int:dataid>',views.edit_category,name="edit_category"),
    path('addproductpage/',views.addproductpage,name="addproductpage"),
    path('displayproduct/',views.displayproduct,name="displayproduct"),
    path('productsave/',views.productsave,name="productsave"),
    path('delete_category/<int:dataid>/',views.delete_category,name="delete_category"),
    path('edit_product/<int:productid>/',views.edit_product,name="edit_product"),
    path('update_categorydata/<int:dataid>',views.update_categorydata,name="update_categorydata")
]
