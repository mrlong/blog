################################################
#
# 作者：龙仕云  2013－7－15
#  出于学习与工作的需要，自己创建的项目。
# 
# 语法规则：
#    1.关键字大写
#    2.表名与字段小写
#
##############################################


CREATE TABLE blog_entries (
    id INT AUTO_INCREMENT,
    class_id INT not null,
    title TEXT,
    content TEXT,
    posted_on DATETIME,
    primary key (id)
);

CREATE TABLE blog_class(
	id INT AUTO_INCREMENT,
	classname CHAR(200),
	primary key(id)
);

