// Copyright (c) 2019, Mada and contributors
// For license information, please see license.txt

frappe.ui.form.on('Meeting', {
	send_emails: function(frm) {
		if (frm.doc.status==="Planned") {
			frappe.call({
				method:	"meeting.api.send_invitation_emails",
				args: {
					meeting: frm.doc.name
				},
				callback: function(r) {

				}
			})
		}

	}
});
