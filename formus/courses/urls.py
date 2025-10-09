from django.urls import path
from .views import CourseListView, CourseCreateView, CourseUpdateView, CourseColumnCreateView, CourseHelpView, CourseAccordionCreateView, CourseTabCreateView, CourseTabUpdateView,  CourseFieldsetCreateView, CoursePDFView

app_name = "courses"

urlpatterns = [
    path("", CourseListView.as_view(), name="list"),
    path("new/", CourseCreateView.as_view(), name="create"),
    path("<int:pk>/edit/", CourseUpdateView.as_view(), name="update"),
    path("columnas/new/", CourseColumnCreateView.as_view(), name="columnas"),
    path("help/new/", CourseHelpView.as_view(), name="help_create"),
    path("help/<int:pk>/", CourseHelpView.as_view(), name="help_update"),
    path("accordion/new/", CourseAccordionCreateView.as_view(), name="accordion"),
    path("tabs/new/", CourseTabCreateView.as_view(), name="tabs_create"),
    path("tabs/<int:pk>/edit/", CourseTabUpdateView.as_view(), name="tabs_update"),    
    path("fieldset/new/", CourseFieldsetCreateView.as_view(), name="fieldset_create"),
    path("<int:pk>/pdf/", CoursePDFView.as_view(), name="pdf"),
    
]