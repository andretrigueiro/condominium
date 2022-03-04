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
        'birthdate': '00/00/0000',
        'first_login': False
    },
]

RESIDENT = [
    {
        'user': 'condominium',
        'password': 'test',
        'name': 'condominium',
        'email': 'condominium@email.com',
        'type': 'resident',
        'birthdate': 'test',
        'house': '3',
        'first_login': False
    },
    {
        'user': 'jose.cond',
        'password': '1234',
        'name': 'Jose',
        'email': 'jose@email.com',
        'type': 'resident',
        'birthdate': '11/11/1111',
        'house': '1',
        'first_login': False
    },
    {
        'user': 'maria.cond',
        'password': '12345',
        'name': 'Maria',
        'email': 'maria@email.com',
        'type': 'resident',
        'birthdate': '22/22/2222',
        'house': '2',
        'first_login': True
    },
]

HOUSES = [
    {
        'number': '1',
        'onwer': 'condominium',
        'residents': [],
        'condominium price': 111.00,
        'payments': [
            {
                'january': 'paid',
            },
            {
                'february': 'paid',
            },
            {
                'march': 'paid'
            },
        ],
        'fines': []
    },
    {
        'number': '2',
        'onwer': '621fc9f0e1d5f250cadbf4d0',
        'residents': [],
        'condominium price': 222.00,
        'payments': [
            {
                'january': 'paid',
            },
            {
                'february': 'paid',
            },
            {
                'march': 'paid'
            },
        ],
        'fines': []
    },
    {
        'number': '3',
        'onwer': 'condominium',
        'residents': [],
        'condominium price': 333.00,
        'payments': [
            {
                'january': 'paid',
            },
            {
                'february': 'paid',
            },
            {
                'march': 'paid'
            },
        ],
        'fines': []
    },
    {
        'number': '4',
        'onwer': 'condominium',
        'residents': [],
        'condominium price': 444.00,
        'payments': [
            {
                'january': 'paid',
            },
            {
                'february': 'paid',
            },
            {
                'march': 'paid'
            },
        ],
        'fines': []
    },
    {
        'number': '5',
        'onwer': 'condominium',
        'residents': [],
        'condominium price': 555.00,
        'payments': [
            {
                'january': 'paid',
            },
            {
                'february': 'paid',
            },
            {
                'march': 'paid'
            },
        ],
        'fines': []
    },
    {
        'number': '6',
        'onwer': 'condominium',
        'residents': [],
        'condominium price': 666.00,
        'payments': [
            {
                'january': 'paid',
            },
            {
                'february': 'paid',
            },
            {
                'march': 'paid'
            },
        ],
        'fines': []
    },
]