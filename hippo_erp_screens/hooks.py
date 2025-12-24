app_name = "hippo_erp_screens"
app_title = "hippo_erp_screens"
app_publisher = "saikumar parla"
app_description = "hippoclouds official site for hr management ui customized by saikumar parla mern stack developer hippocloud technologies pvt ltd"
app_email = "saiparla@hippoclouds.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "hippo_erp_screens",
# 		"logo": "/assets/hippo_erp_screens/logo.png",
# 		"title": "hippo_erp_screens",
# 		"route": "/hippo_erp_screens",
# 		"has_permission": "hippo_erp_screens.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
app_include_css = "/assets/hippo_erp_screens/css/sidebaricons.css"
app_include_js = [
    "/assets/hippo_erp_screens/js/login.js",
    "/assets/hippo_erp_screens/js/navbar.js",
    "/assets/hippo_erp_screens/js/deskpage.js",
    "/assets/hippo_erp_screens/js/sidebar.js",
    "/assets/hippo_erp_screens/js/list.js",
    "/assets/hippo_erp_screens/js/mobile.js",
    "/assets/hippo_erp_screens/js/form.js",
    "/assets/hippo_erp_screens/js/dialog.js"

]

# include js, css files in header of web template
web_include_css = "/assets/hippo_erp_screens/css/sidebaricons.css"
web_include_js = [
    "/assets/hippo_erp_screens/js/login.js",
    "/assets/hippo_erp_screens/js/navbar.js",
    "/assets/hippo_erp_screens/js/deskpage.js",
    "/assets/hippo_erp_screens/js/sidebar.js",
    "/assets/hippo_erp_screens/js/list.js",
    "/assets/hippo_erp_screens/js/mobile.js",
    "/assets/hippo_erp_screens/js/form.js",
    "/assets/hippo_erp_screens/js/dialog.js"

]

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "hippo_erp_screens/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "hippo_erp_screens/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "hippo_erp_screens.utils.jinja_methods",
# 	"filters": "hippo_erp_screens.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "hippo_erp_screens.install.before_install"
# after_install = "hippo_erp_screens.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "hippo_erp_screens.uninstall.before_uninstall"
# after_uninstall = "hippo_erp_screens.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "hippo_erp_screens.utils.before_app_install"
# after_app_install = "hippo_erp_screens.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "hippo_erp_screens.utils.before_app_uninstall"
# after_app_uninstall = "hippo_erp_screens.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "hippo_erp_screens.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"hippo_erp_screens.tasks.all"
# 	],
# 	"daily": [
# 		"hippo_erp_screens.tasks.daily"
# 	],
# 	"hourly": [
# 		"hippo_erp_screens.tasks.hourly"
# 	],
# 	"weekly": [
# 		"hippo_erp_screens.tasks.weekly"
# 	],
# 	"monthly": [
# 		"hippo_erp_screens.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "hippo_erp_screens.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "hippo_erp_screens.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "hippo_erp_screens.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["hippo_erp_screens.utils.before_request"]
# after_request = ["hippo_erp_screens.utils.after_request"]

# Job Events
# ----------
# before_job = ["hippo_erp_screens.utils.before_job"]
# after_job = ["hippo_erp_screens.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"hippo_erp_screens.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

