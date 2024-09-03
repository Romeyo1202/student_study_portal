from django.urls import path
from . import views
    #register path in students(project)  la urls.py la irukku
    
urlpatterns = [
    #Home Page
    path('', views.home, name='home'),

    #Notes Page
    path('notes', views.notes, name='notes'),
    path('delete_note/<int:pk>', views.delete_note, name='delete_note'),
    path('notes_detail/<int:pk>', views.NotesDetailView.as_view(), name='notes_detail'),

    #Homework Page
    path('homework', views.homework, name='homework'),
    path('update_homework/<int:pk>', views.update_homework, name='update_homework'),
    path('delete_homework/<int:pk>', views.delete_homework, name='delete_homework'),

    #Youtube Page 
    path('youtube', views.youtube, name='youtube'),

    #ToDo Page
    path('todo', views.todo, name='todo'),
    path('update_todo/<int:pk>', views.update_todo, name='update_todo'),
    path('delete_todo/<int:pk>', views.delete_todo, name='delete_todo'),

    #Books Page 
    path('books', views.books, name='books'),

    #Dictionary Page 
    path('dictionary', views.dictionary, name='dictionary'),

    #Wikipidia Page
    path('wiki', views.wiki, name='wiki'),

    #Conversion Page 
    path('conversion', views.conversion, name='conversion'),

]
