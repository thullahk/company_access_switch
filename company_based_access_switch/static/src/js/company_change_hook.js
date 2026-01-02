/** @odoo-module */

import { companyService } from "@web/webclient/company_service";
import { patch } from "@web/core/utils/patch";

patch(companyService, {
    start(env, { user, router, cookie, action }) {
        // Initialize the original service
        const service = super.start(...arguments);

        // Keep a reference to the original 'setCompanies' function
        const originalSetCompanies = service.setCompanies.bind(service);

        // Overwrite 'setCompanies' with our wrapper
        service.setCompanies = async (companyIds, includeChildCompanies = true) => {

            // The first ID is the company we are switching TO
            const newCompanyId = companyIds[0];

            if (newCompanyId) {
                try {
                    console.log("Triggering Python Company Switch Logic...");

                    // Call Python and WAIT for it to finish
                    await env.services.orm.call(
                        "res.users",
                        "run_action_on_company_change",
                        [],
                        { new_company_id: newCompanyId }
                    );

                } catch (error) {
                    console.error("Error: Failed to update groups on switch:", error);
                }
            }

            // Call the original Odoo logic
            return originalSetCompanies(companyIds, includeChildCompanies);
        };

        return service;
    }
});