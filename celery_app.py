from celery import Celery
import settings

celery_app = Celery('xtceleryapp',
                    broker=settings.CELERY_BROKER_URL,
                    backend=settings.CELERY_RESULT_BACKEND,
                    )

celery_app.conf.update(task_track_started=True)
celery_app.conf.update(redbeat_redis_url = settings.REDISURL)
#celery_app.conf.update(redis = settings.REDISURL)