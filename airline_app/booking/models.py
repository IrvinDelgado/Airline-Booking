from django.db import models
from uuid import uuid4
# Create your models here.


class Airport(models.Model):
    iata = models.CharField(primary_key=True, max_length=5)
    country = models.CharField(max_length=30, blank=True, null=True)
    state = models.CharField(max_length=20, blank=True, null=True)
    longitude = models.CharField(max_length=15, blank=True, null=True)
    latitude = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.iata
    class Meta:
        db_table = 'airport'


class Airline(models.Model):
    airline_code = models.CharField(primary_key=True, max_length=5)
    airline_name = models.CharField(max_length=20)
    origin_country = models.CharField(max_length=30, blank=True, null=True)
    airport = models.ForeignKey(Airport, on_delete = models.CASCADE)

    class Meta:
        db_table = 'airline'
        unique_together = (('airline_code', 'airline_name'),)


class Flight(models.Model):
    flight_number = models.CharField(primary_key=True, max_length=10)
    flight_in = models.ForeignKey(Airport, on_delete = models.CASCADE)
    airline_code = models.ForeignKey(Airline, models.DO_NOTHING, db_column='airline_code', blank=True, null=True)
    airline_name = models.CharField(max_length=20, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    departure_airport = models.CharField(max_length=5, blank=True, null=True)
    destination_airport = models.CharField(max_length=5, blank=True, null=True)
    departure_time = models.TimeField(blank=True, null=True)
    destination_time = models.TimeField(blank=True, null=True)
    first_max_seats = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    economy_max_seats = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    
    class Meta:
        db_table = 'flight'


class Customer(models.Model):
    email = models.CharField(primary_key=True, max_length=50)
    name = models.CharField(max_length=20, blank=True, null=True)
    iata = models.ForeignKey(Airport, models.DO_NOTHING, db_column='iata', blank=True, null=True)

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'customer'



class Booked(models.Model):
    flight_number = models.OneToOneField('Flight', models.DO_NOTHING, db_column='flight_number', primary_key=True)
    email = models.ForeignKey('Customer', models.DO_NOTHING, db_column='email')
    class_type = models.CharField(db_column='class_type', max_length=10)  

    class Meta:
        db_table = 'booked'
        unique_together = (('flight_number', 'email', 'class_type'),)


class PaymentOptions(models.Model):
    payment_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    email = models.ForeignKey(Customer, models.DO_NOTHING, db_column='email', blank=True, null=True)

    def __str__(self):
        return self.payment_id

    class Meta:
        db_table = 'payment_options'


class AddressTable(models.Model):
    address_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    payment = models.ForeignKey('PaymentOptions', models.DO_NOTHING, blank=True,null=True)
    address = models.CharField(max_length=35)

    def __str__(self):
        return self.address

    class Meta:
        db_table = 'address_table'


class CreditCardTable(models.Model):
    card_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    payment = models.ForeignKey('PaymentOptions', models.DO_NOTHING, blank=True,null=True)
    credit_card = models.DecimalField(max_digits=15, decimal_places=0)

    def __str__(self):
        return str(self.credit_card)

    class Meta:
        db_table = 'credit_card_table'



class Booking(models.Model):
    booking_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    credit_card = models.DecimalField(max_digits=15, decimal_places=0, blank=True, null=True)
    payment = models.ForeignKey('CreditCardTable', models.DO_NOTHING, blank=True, null=True)
    email = models.ForeignKey('Customer', models.DO_NOTHING, db_column='email', blank=True, null=True)

    class Meta:
        db_table = 'booking'


class FlightNumbers(models.Model):
    #flight_number_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    to_booking = models.ForeignKey('Booking', models.DO_NOTHING, blank =True, null=True)
    flight_number = models.OneToOneField(Flight, models.DO_NOTHING, db_column='flight_number')

    class Meta:
        db_table = 'flight_numbers'


class MilProgram(models.Model):
    program_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    airline_code = models.ForeignKey(Airline, models.DO_NOTHING, db_column='airline_code', blank=True, null=True)
    airline_name = models.CharField(max_length=20, blank=True, null=True)
    mileage = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    email = models.ForeignKey(Customer, models.DO_NOTHING, db_column='email', blank=True, null=True)

    class Meta:
        db_table = 'mil_program'


        
class BillingInfo(models.Model):
    billing_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    address = models.ForeignKey('AddressTable', models.DO_NOTHING, blank=True, null=True)
    credit_card = models.ForeignKey('CreditCardTable', models.DO_NOTHING, blank=True, null=True)
    payment = models.ForeignKey('PaymentOptions', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'billing_info'




