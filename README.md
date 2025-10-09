# crispy_examples  
> Repositorio de clase – Práctica Profesionalizante 1  
> Instituto Técnico Superior Córdoba (ITSC) – 2025

## 1. Objetivo del proyecto
Mostrar, en forma secuencial y didáctica, cómo construir formularios elegantes y funcionales con **Django + Bootstrap 4 + django-crispy-forms**.  
Está pensado para que el/la alumno/a pueda:
- copiar el código,
- levantar el servidor,
- *jugar* con los distintos "juguetes" que ofrece crispy-forms,
- y poder adaptarlo al proyecto final (o a cualquier otro).

## 2. Stack tecnológico
| Tecnología | Versión recomendada |
|------------|---------------------|
| Python     | 3.11+               |
| Django     | 4.2 LTS             |
| Bootstrap  | 4.6.x (vía django-bootstrap4) |
| django-crispy-forms | 2.x |
| WeasyPrint | 59+ (para PDF)      |

## 3. Instalación rápida
```bash
git clone https://github.com/luirro777/crispy_examples.git
cd crispy_examples
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
cd formus/
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
Abrir http://127.0.0.1:8000/courses/

## 4. Rutas 
| Ruta | Funcionalidad | ¿Qué se aprende? |
|------|---------|---------------|
| `/courses/new/` | Form clásico | Uso básico de CBV, bootstrap4 |
| `/courses/crispy/new/` | Crispy básico | `|crispy`, `FormHelper` |
| `/courses/tabs/new/` | TabHolder | Dividir form en pestañas |
| `/courses/accordion/new/` | AccordionGroup | Acordeón desplegable |
| `/courses/fieldset/new/` | Fieldset | Agrupación con leyenda || 
| `/courses/<id>/pdf/` | WeasyPrint | Exportar PDF |



## 5. Recursos adicionales
- [Documentación oficial django-crispy-forms](https://django-crispy-forms.readthedocs.io/)
- [Bootstrap 4 components](https://getbootstrap.com/docs/4.6/components/alerts/)
- [WeasyPrint docs](https://doc.courtbouillon.org/weasyprint/stable/)


## 6. Licencia

GNU General Public License v3.0 (GPL-3.0)  
© 2025 Luis Romano

Este material se publica bajo los términos de la **GNU GPL v3.0**. Podés usar, copiar, modificar y redistribuir este contenido, incluidos trabajos derivados, siempre que las obras resultantes se distribuyan bajo la misma licencia (copyleft).  
Para más detalles sobre los términos y las obligaciones (incluyendo el código fuente cuando aplique), consultá la licencia completa en <https://www.gnu.org/licenses/gpl-3.0.html>.
