app_name = "claro_car"
app_title = "Claro Car"
app_publisher = "Nasir Nasim"
app_description = "App for Car Wash and Cleaning"
app_email = "nasiransari97177@gmail.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "claro_car",
# 		"logo": "/assets/claro_car/logo.png",
# 		"title": "Claro Car",
# 		"route": "/claro_car",
# 		"has_permission": "claro_car.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/claro_car/css/claro_car.css"
# app_include_js = "/assets/claro_car/js/claro_car.js"

# include js, css files in header of web template
# web_include_css = "/assets/claro_car/css/claro_car.css"
# web_include_js = "/assets/claro_car/js/claro_car.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "claro_car/public/scss/website"

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
# app_include_icons = "claro_car/public/icons.svg"

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
# 	"methods": "claro_car.utils.jinja_methods",
# 	"filters": "claro_car.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "claro_car.install.before_install"
# after_install = "claro_car.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "claro_car.uninstall.before_uninstall"
# after_uninstall = "claro_car.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "claro_car.utils.before_app_install"
# after_app_install = "claro_car.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "claro_car.utils.before_app_uninstall"
# after_app_uninstall = "claro_car.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "claro_car.notifications.get_notification_config"

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
# 		"claro_car.tasks.all"
# 	],
# 	"daily": [
# 		"claro_car.tasks.daily"
# 	],
# 	"hourly": [
# 		"claro_car.tasks.hourly"
# 	],
# 	"weekly": [
# 		"claro_car.tasks.weekly"
# 	],
# 	"monthly": [
# 		"claro_car.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "claro_car.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "claro_car.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "claro_car.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["claro_car.utils.before_request"]
# after_request = ["claro_car.utils.after_request"]

# Job Events
# ----------
# before_job = ["claro_car.utils.before_job"]
# after_job = ["claro_car.utils.after_job"]

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
# 	"claro_car.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

