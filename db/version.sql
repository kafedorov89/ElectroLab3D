CREATE USER 'django'@'localhost' IDENTIFIED BY '31415926';
GRANT ALL PRIVILEGES ON * . * TO 'django'@'localhost';
FLUSH PRIVILEGES;

CREATE DATABASE electrolab;


drop table main_useranswer;
drop table main_answer;
drop table main_question;

drop table main_usercoursestate;
drop table main_userfieldparam;
drop table main_coursestate;
drop table main_coursefield;
drop table main_userallowance;
drop table main_method;
drop table main_course;

drop table main_fieldtype;
drop table main_standtask_data;
drop table main_standtaskstate;

drop table main_wpparam;
drop table main_wpparamtype;
drop table main_workplace;
drop table main_wptype;

