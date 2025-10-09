# courses/forms.py
from django import forms
from .models import Course
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field, Row, Column, ButtonHolder, HTML, Fieldset
from crispy_forms.bootstrap import Accordion, AccordionGroup, TabHolder, Tab
from .helpers import BaseFormHelper

class CourseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()        
        self.helper.layout = Layout(
            Field("code", css_class="mb-3"),
            Field("title", css_class="mb-3"),
            #"description",
            Field("description", rows="3"),
            ButtonHolder(
                Submit("save", "Guardar", css_class="btn-success"),
                HTML('<a href="{% url \'courses:list\' %}" class="btn btn-outline-secondary">Cancelar</a>')
            )
        )

    class Meta:
        model = Course
        fields = ("code","title", "description")

class CourseColumnForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ("title", "code", "description")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column("title", css_class="form-group col-md-6 mb-0"),
                Column("code",  css_class="form-group col-md-6 mb-0"),
            ),
            #"description",
            Field("description", rows="3"),
            ButtonHolder(
                Submit("save", "Guardar", css_class="btn-success"),
                HTML('<a href="{% url \'courses:list\' %}" class="btn btn-outline-secondary">Cancelar</a>')
            )
        )

class CourseHelpForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ("code","title", "description")
        help_texts = {
            "title": "Crea un título atractivo para tu curso.",
            "code": "Codigo del curso"
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        # Texto dinámico del botón principal
        submit_text = "Actualizar" if self.instance.pk else "Crear curso"
        self.helper.add_input(Submit("save", submit_text, css_class="btn-primary"))
        # Botón extra solo en update
        if self.instance.pk:
            self.helper.add_input(
                Submit("save_continue", "Guardar y seguir editando",
                       css_class="btn-outline-info")
            )


        
class CourseAccordionForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ("title", "code", "description")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Accordion(
                AccordionGroup("Datos básicos",
                               "title", "code"),
                AccordionGroup("Descripción completa",
                               "description"),
            ),
            ButtonHolder(
                Submit("save", "Guardar", css_class="btn-success")
            )
        )

class CourseTabForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ("title", "code", "description")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            TabHolder(
                Tab("Identificación",
                    Field("title", placeholder="Ej. Django básico"),
                    Field("code",  placeholder="Ej. DJ-101")),
                Tab("Descripción",
                    Field("description", rows=5)),
            ),
            ButtonHolder(
                Submit("save", "Guardar curso", css_class="btn-success")
            )
        )


class CourseFieldsetForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ("title", "code", "description")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = BaseFormHelper()
        self.helper.layout = Layout(
            Fieldset(
                "Identificación del curso",
                "title",
                "code",
                css_id="fieldset-id"
            ),
            Fieldset(
                "Detalles",
                "description"
            )
        )

