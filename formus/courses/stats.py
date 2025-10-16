from datetime import date, timedelta
from django.db.models import Count
from django.db.models.functions import TruncDate
from django.utils import timezone # <--- Nueva importación
from dateutil.rrule import rrule, DAILY
from .models import Course

def courses_per_day(since_days=30):
    # Usar timezone.localdate() para obtener la fecha local correcta
    today = timezone.localdate() 
    start = today - timedelta(days=since_days - 1)
    
    # Obtener la zona horaria local configurada en settings.py
    current_tz = timezone.get_current_timezone() 

    qs = (Course.objects
          .filter(created_at__date__gte=start)
          # APLICAR EL CAMBIO AQUÍ: Usar tzinfo para truncar en la hora local
          .annotate(day=TruncDate('created_at', tzinfo=current_tz)) 
          .values('day')
          .annotate(count=Count('id'))
          .order_by('day'))

    counts = {str(row['day']): row['count'] for row in qs}

    # CAMBIO: Usamos rrule para obtener la lista de fechas.
    # El rango 'until=today' incluye el día de hoy.
    fechas_del_rango = list(rrule(DAILY, dtstart=start, until=today))

    return [
        {'day': d.strftime('%Y-%m-%d'), 'count': counts.get(d.isoformat(), 0)}
        for d in fechas_del_rango
    ]