# company_access_switch
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
