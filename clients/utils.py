import logging

import requests
from django.utils.dateparse import parse_datetime

from .models import (
    Client,
    Country,
    Company,
    Manager,
    Account,
    ClientType,
    VerificationLevel
)


def fetch_clients_data(token: str):
    url: str = "https://api.b2broker.com/api/v2/clients"
    headers: dict = {
        'Authorization': f'Bearer {token}',
    }
    response = requests.get(url, headers=headers)
    return response.json()


def save_clients_data(data: dict):
    for client_data in data['data']:
        # Country
        country_data: dict = client_data['country']
        country, _ = Country.objects.get_or_create(
            country_id=country_data['countryId'],
            defaults={
                'alpha2_code': country_data['alpha2Code'],
                'alpha3_code': country_data['alpha3Code'],
                'country_name': country_data['countryName'],
                'numeric_code': country_data['numericCode'],
            }
        )

        # Company
        company_data: dict = client_data['company']
        company, _ = Company.objects.get_or_create(
            full_name=company_data['fullName'],
            short_name=company_data['shortName']
        )

        # Manager
        manager_data: dict = client_data['manager']
        manager, _ = Manager.objects.get_or_create(
            manager_id=manager_data['id'],
            defaults={
                'enabled': manager_data['enabled'],
                'email': manager_data['email'],
                'name': manager_data['name'],
                'title': manager_data['title'],
                'phone': manager_data['phone'],
                'create_time': parse_datetime(manager_data['createTime'])
            }
        )

        # Type
        type_data: dict = client_data['client_type']
        client_type, _ = ClientType.objects.get_or_create(
            type_id=type_data['id'],
            defaults={'name': type_data['name']}
        )

        # Verification Level
        verification_level_data: dict = client_data['verificationLevel']
        verification_level, _ = VerificationLevel.objects.get_or_create(
            level_id=verification_level_data['id'],
            defaults={'name': verification_level_data['name']}
        )

        # Client
        client, created = Client.objects.update_or_create(
            client_id=client_data['clientId'],
            defaults={
                'first_name': client_data['firstName'],
                'last_name': client_data['lastName'],
                'middle_name': client_data.get('middleName', ''),
                'name': client_data['name'],
                'nickname': client_data.get('nickname', ''),
                'email': client_data['email'],
                'phone': client_data['phone'],
                'birthday': parse_datetime(client_data['birthday']),
                'city': client_data['city'],
                'country': country,
                'company': company,
                'internal_type': client_data['internalType'],
                'locale': client_data['locale'],
                'manager': manager,
                'risk_level': client_data['riskLevel'],
                'status': client_data['status'],
                'client_type': client_type,
                'verification_level': verification_level,
                'logged_at': parse_datetime(client_data['loggedAt']),
                'create_time': parse_datetime(client_data['createTime']),
                'update_time': parse_datetime(client_data['updateTime']),
                'tags': client_data['tags'],
                'analytics': client_data['analytics'],
            }
        )

        # Client Accounts
        for account_data in client_data['accounts']:
            account, _ = Account.objects.update_or_create(
                account_id=account_data['accountId'],
                defaults={
                    'account_number': account_data['accountNumber'],
                    'create_time': parse_datetime(account_data['createTime'])
                }
            )
            client.accounts.add(account)

        client.save()

    logging.info("Client data saved successfully")
