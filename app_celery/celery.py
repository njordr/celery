from __future__ import absolute_import

from celery import Celery

app = Celery('app_celery', backend='rpc://',)

if __name__ == '__main__':
    app.start()
