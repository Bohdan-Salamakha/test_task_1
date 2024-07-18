from django.db import models


class Country(models.Model):
    country_id = models.IntegerField(primary_key=True)
    alpha2_code = models.CharField(max_length=2)
    alpha3_code = models.CharField(max_length=3)
    country_name = models.CharField(max_length=100)
    numeric_code = models.CharField(max_length=3)

    def __str__(self):
        return self.country_name


class Company(models.Model):
    full_name = models.CharField(max_length=255)
    short_name = models.CharField(max_length=255)

    def __str__(self):
        return self.short_name


class Manager(models.Model):
    manager_id = models.IntegerField(primary_key=True)
    enabled = models.BooleanField(default=True)
    email = models.EmailField()
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    create_time = models.DateTimeField()

    def __str__(self):
        return self.name


class ClientType(models.Model):
    type_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class VerificationLevel(models.Model):
    level_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Account(models.Model):
    account_id = models.IntegerField(primary_key=True)
    account_number = models.BigIntegerField()
    create_time = models.DateTimeField()

    def __str__(self):
        return str(self.account_number)


class Client(models.Model):
    client_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255)
    nickname = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    birthday = models.DateTimeField()
    city = models.CharField(max_length=255)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    internal_type = models.CharField(max_length=50)
    locale = models.CharField(max_length=50)
    manager = models.ForeignKey(Manager, on_delete=models.CASCADE)
    risk_level = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    client_type = models.ForeignKey(ClientType, on_delete=models.CASCADE)
    verification_level = models.ForeignKey(VerificationLevel, on_delete=models.CASCADE)
    logged_at = models.DateTimeField()
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()
    accounts = models.ManyToManyField(Account)
    tags = models.JSONField()
    analytics = models.JSONField()

    def __str__(self):
        return self.name
