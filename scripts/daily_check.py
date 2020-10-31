from datetime import date, timedelta
from django.core.mail import send_mail
from maintenance.models import Car


def run(carlist=Car.objects.all()):
    for car in carlist:
        inspection_due = car.last_inspection
        inspection_due = inspection_due.replace(year=inspection_due.year +
                                                1, day=inspection_due.day-1)
        insurance_due = car.last_insurance
        months = insurance_due.month + int(car.insurance_duration)
        years = 1 if months > 12 else 0
        insurance_due = insurance_due.replace(year=insurance_due.year +
                                              years, month=(months-1) % 12+1, day=insurance_due.day-1)
        today = date.today()
        time_to_inspection, time_to_insurance = None, None
        if inspection_due - today < timedelta(days=15):
            time_to_inspection = inspection_due - today
        if insurance_due - today < timedelta(days=15):
            time_to_insurance = insurance_due - today
        if time_to_inspection or time_to_insurance:
            if time_to_inspection:
                what_ends = 'przegląd'
                if time_to_insurance:
                    what_ends += ' i ubezpieczenie'
            else:
                what_ends = 'ubezpieczenie'

            message = f'Niestety, ale czas zajrzeć do dokumentów Twojego samochodu { car }. Niedługo kończy Ci się { what_ends }. Aby ten upierdliwy mail nie przychodził do Ciebie codziennie, załatw formalności i zmień dane samochodu na "Serwisuj, nie naprawiaj!!!".'
            send_mail(
                f'Czas zadbać o samochód.',
                f'{message}',
                'kowalkem2@gmail.com',
                [f'{car.owner.email}'],
                fail_silently=False,
            )
