#!/usr/bin/python
# coding=utf-8

import web,datetime

#表名列表
TB_BLOG_ENTRIES = 'blog_entries';   #博客内容表




db = web.database(dbn='mysql', db='test', user='root' , pw='7895123')

def get_posts():
	return db.select(TB_BLOG_ENTRIES, order='id DESC')


def get_post(id):
	try:
		return db.select(TB_BLOG_ENTRIES, where='id=$id',vars=locals())[0]
			
	except IndexError:
		return None


def new_post(title,text,classid):
	db.insert(TB_BLOG_ENTRIES,title=title,content=text,
		posted_on=datetime.datetime.utcnow(),
		class_id=classid)

def del_post(id):
	db.delete(TB_BLOG_ENTRIES,where="id=$id",vars=locals())

def update_post(id,title,text,classid):
	db.update(TB_BLOG_ENTRIES,where="id=$id",vars=locals(),
		title=title,content=text,class_id=classid)

