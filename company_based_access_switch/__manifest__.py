{
    'name': "Company Based Access Switch",
    "category": "Technical / Security",
    'summary': "Dynamically switch user access groups when changing company",
    "description": """
        This module enables dynamic user access control in multi-company environments.
        
        When a user switches the active company from the company selector, their access
        groups are automatically updated based on the target company's configuration.
        
        Key Features:
        - Hooks into Odoo's company switch mechanism (OWL / JavaScript)
        - Triggers server-side group updates before reload
        - Company-driven role assignment using boolean flags
        - No core overrides
        - Upgrade-safe and modular design
        
        Use Case:
        - Same user, different roles per company
        - Technician vs Manager access per company
        - Multi-company environments with dynamic permissions
    """,
    'author': "Rahmathullah K / Digitz Technologies",
    "website": "https://github.com/thullahk",
    'version': '18.0.1.0.0',
    'depends': ['web', 'base'],
    'data': ['security/security.xml',
             'views/res_company.xml'],
    'assets': {
        'web.assets_backend': [
            'company_based_access_switch/static/src/js/company_change_hook.js',
        ],
    },
    'installable': True,
    'application': True,
    'license': 'OEEL-1',
}
