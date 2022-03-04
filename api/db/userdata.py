"""
Test data to populate the DATABASE.
"""

ADM = [
    {
        'user': 'syndicate.cond',
        'password': '123',
        'name': 'Andre',
        'email': 'adm@email.com',
        'type': 'adm',
        'birthdate': '00/00/0000'
    },
]

RESIDENT = [
    {
        'user': 'condominium',
        'password': 'test',
        'name': 'condominium',
        'email': 'condominium@email.com',
        'type': 'resident',
        'birthdate': 'test'
    },
    {
        'user': 'jose.cond',
        'password': '1234',
        'name': 'Jose',
        'email': 'jose@email.com',
        'type': 'resident',
        'birthdate': '11/11/1111'
    },
    {
        'user': 'maria.cond',
        'password': '12345',
        'name': 'Maria',
        'email': 'maria@email.com',
        'type': 'resident',
        'birthdate': '22/22/2222'
    },
]

HOUSES = [
    {
        'number': '1',
        'onwer': 'condominium',
        'residents': [],
        'condominiumprice': 111.00,
        'debts': [],
        'payments': [],
        'fines': []
    },
    {
        'number': '2',
        'onwer': '621fc9f0e1d5f250cadbf4d0',
        'residents': [],
        'condominiumprice': 222.00,
        'debts': [],
        'payments': [],
        'fines': []
    },
    {
        'number': '3',
        'onwer': 'condominium',
        'residents': [],
        'condominiumprice': 333.00,
        'debts': [],
        'payments': [],
        'fines': []
    },
    {
        'number': '4',
        'onwer': 'condominium',
        'residents': [],
        'condominiumprice': 444.00,
        'debts': [],
        'payments': [],
        'fines': []
    },
    {
        'number': '5',
        'onwer': 'condominium',
        'residents': [],
        'condominiumprice': 555.00,
        'debts': [],
        'payments': [],
        'fines': []
    },
    {
        'number': '6',
        'onwer': 'condominium',
        'residents': [],
        'condominiumprice': 666.00,
        'debts': [],
        'payments': [],
        'fines': []
    },
]