CELERY_TIMEZONE = 'Europe/Rome'

# The backend used to store task results
CELERY_RESULT_BACKEND = 'rpc://'

# If set to True, result messages will be persistent. This means the messages will not be lost after a broker restart
CELERY_RESULT_PERSISTENT = True

CELERY_ACCEPT_CONTENT=['json', 'pickle']

CELERY_TASK_SERIALIZER='json'

CELERY_RESULT_SERIALIZER='json'

# Broker settings.
BROKER_URL = 'amqp://guest:guest@localhost:5672//'

BROKER_HEARTBEAT = 10.0

BROKER_HEARTBEAT_CHECKRATE = 2.0

CELERY_IMPORTS = [ 'app_celery.tasks' ]

CELERYD_STATE_DB = '/var/celery/db/state'

# Enables error emails.
CELERY_SEND_TASK_ERROR_EMAILS = True

# Name and email addresses of recipients
ADMINS = (
    ('Administrator Name', 'admin@somedoamin.net'),
)

# Email address used as sender (From field).
SERVER_EMAIL = 'no-reply@somedomain.net'

# Mailserver configuration
EMAIL_HOST = 'localhost'
EMAIL_PORT = 25

# Send events so the worker can be monitored by tools like celerymon.
CELERY_SEND_EVENTS = True

# If enabled the worker pool can be restarted using the pool_restart remote control command.
CELERYD_POOL_RESTARTS = True
