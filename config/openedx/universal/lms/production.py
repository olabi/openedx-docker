import os
from ..aws import *

update_module_store_settings(MODULESTORE, doc_store_settings=DOC_STORE_CONFIG)

MEDIA_ROOT = "/openedx/data/uploads/"

# Deactivate syslog-based loggers which don't work inside docker containers
LOGGING['handlers'].pop('local')
LOGGING['handlers'].pop('tracking')
LOGGING['loggers'].pop('tracking')
LOGGING['loggers']['']['handlers'] = ['console']

# Create folders if necessary
for folder in [LOG_DIR, MEDIA_ROOT, STATIC_ROOT_BASE]:
    if not os.path.exists(folder):
        os.makedirs(folder)

ALLOWED_HOSTS = [
    ENV_TOKENS.get('LMS_BASE'),
    FEATURES['PREVIEW_LMS_BASE'],
]

DEFAULT_FROM_EMAIL = 'registration@' + ENV_TOKENS['LMS_BASE']
DEFAULT_FEEDBACK_EMAIL = 'feedback@' + ENV_TOKENS['LMS_BASE']
SERVER_EMAIL = 'devops@' + ENV_TOKENS['LMS_BASE']
TECH_SUPPORT_EMAIL = 'technical@' + ENV_TOKENS['LMS_BASE']
CONTACT_EMAIL = 'info@' + ENV_TOKENS['LMS_BASE']
BUGS_EMAIL = 'bugs@' + ENV_TOKENS['LMS_BASE']
UNIVERSITY_EMAIL = 'university@' + ENV_TOKENS['LMS_BASE']
PRESS_EMAIL = 'press@' + ENV_TOKENS['LMS_BASE']
PAYMENT_SUPPORT_EMAIL = 'payment@' + ENV_TOKENS['LMS_BASE']
BULK_EMAIL_DEFAULT_FROM_EMAIL = 'no-reply@' + ENV_TOKENS['LMS_BASE']
API_ACCESS_MANAGER_EMAIL = 'api-access@' + ENV_TOKENS['LMS_BASE']
API_ACCESS_FROM_EMAIL = 'api-requests@' + ENV_TOKENS['LMS_BASE']
