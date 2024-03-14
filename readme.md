###################
# PROJECT DETAILS #
###################
By using hitting the API endpoint we can store the news details in the table
or
Just start the upload task to automatic it create task by celery in rabbitmq(msg broker)
and
Start the worker to execute the task stored in rabbitmq

==============================================================================================
Start api command

uvicorn api_rout:app --reload

==============================================================================================

Start upload task command

celery -A c_task beat --loglevel=info --logfile=celerybeat.log

==============================================================================================

Start worker

celery -A c_task worker --loglevel=info --concurrency=1

==============================================================================================

Check task upload log

sudo tail -f celerybeat.log

==============================================================================================

API endpoint

http://127.0.0.1:8000/
