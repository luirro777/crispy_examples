# courses/views.py
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from .models import Course
from .forms import CourseForm, CourseColumnForm, CourseHelpForm, CourseAccordionForm, CourseTabForm, CourseFieldsetForm

class CourseListView(ListView):
    model = Course
    template_name = "courses/course_list.html"
    context_object_name = "courses"

class CourseCreateView(CreateView):
    model = Course
    form_class = CourseForm
    template_name = "courses/course_form.html"    
    success_url = reverse_lazy("courses:list")

class CourseUpdateView(UpdateView):
    model = Course
    form_class = CourseForm
    template_name = "courses/course_form.html"
    success_url = reverse_lazy("courses:list")

# Nueva vista para la visualización con columnas
class CourseColumnCreateView(CreateView):
    model = Course
    form_class = CourseColumnForm
    template_name = "courses/course_columns.html"
    success_url = reverse_lazy("courses:list")

class CourseHelpView(UpdateView):   # UpdateView sirve para ambos casos
    model = Course
    form_class = CourseHelpForm
    template_name = "courses/help_crispy.html"

    def get_object(self, queryset=None):
        # Si no hay pk → crear nueva instancia (CREATE)
        if "pk" not in self.kwargs:
            return None
        return super().get_object(queryset)

    def get_success_url(self):
        if "save_continue" in self.request.POST:
            return self.request.path          # mismo form
        return reverse_lazy("courses:list")   # o lista
    
class CourseAccordionCreateView(CreateView):
    model = Course
    form_class = CourseAccordionForm
    template_name = "courses/accordion_crispy.html"
    success_url = reverse_lazy("courses:list")

class CourseTabCreateView(CreateView):
    model        = Course
    form_class   = CourseTabForm
    template_name = "courses/course_tabs.html"   # mismo template
    success_url   = reverse_lazy("courses:list")

class CourseTabUpdateView(UpdateView):
    model        = Course
    form_class   = CourseTabForm
    template_name = "courses/course_tabs.html"   # reutilizamos
    success_url   = reverse_lazy("courses:list")

class CourseFieldsetCreateView(CreateView):
    model = Course
    form_class = CourseFieldsetForm
    template_name = "courses/course_fieldset.html"
    success_url = reverse_lazy("courses:list")

