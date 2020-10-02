from django.urls import path, include
from . import views

app_name = 'home'
urlpatterns = [
        # *******************************************************	
    # begin Project	
    path('create_data_project', views.create_data_project, name='create_data_project'), 	
    path('read_data_project', views.read_data_project, name='read_data_project'), 	
    path('update_data_project', views.update_data_project, name='update_data_project'), 	
    path('delete_data_project', views.delete_data_project, name='delete_data_project'),  	
    path('find_data_project', views.find_data_project, name='find_data_project'),  	
    # end Project	
    # *******************************************************	

    # *******************************************************	
    # begin Class	
    path('create_data_class', views.create_data_class, name='create_data_class'), 	
    path('read_data_class', views.read_data_class, name='read_data_class'), 	
    path('update_data_class', views.update_data_class, name='update_data_class'), 	
    path('delete_data_class', views.delete_data_class, name='delete_data_class'),  	
    path('find_data_class', views.find_data_class, name='find_data_class'),  	
    # end Class	
    # *******************************************************	

    # *******************************************************	
    # begin CRUD	
    path('create_data_c_r_u_d', views.create_data_c_r_u_d, name='create_data_c_r_u_d'), 	
    path('read_data_c_r_u_d', views.read_data_c_r_u_d, name='read_data_c_r_u_d'), 	
    path('update_data_c_r_u_d', views.update_data_c_r_u_d, name='update_data_c_r_u_d'), 	
    path('delete_data_c_r_u_d', views.delete_data_c_r_u_d, name='delete_data_c_r_u_d'),  	
    path('find_data_c_r_u_d', views.find_data_c_r_u_d, name='find_data_c_r_u_d'),  	
    # end CRUD	
    # *******************************************************	 
]
