Once build is success, access web app through localhost:8085 and submit the records
access the contain db and check the database list from below query
docker exec -it hwpygitjendocodb_db_1 psql -U satish -d postgres -c "\l"
switch to the relevent database with below query
docker exec -it hwpygitjendocodb_db_1 psql -U satish -d hwpygitjendocodb_db 
list the tables with \dt
check the inserted data with select * from messages;
