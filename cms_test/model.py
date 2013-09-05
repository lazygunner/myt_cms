import MySQLdb

def get_data(pageName):

	try:

	    conn=MySQLdb.connect(host='192.168.77.104',user='myt_root',passwd='17097448ak',db='myt',port=3306)
	    cur=conn.cursor()
	    #pageName = "wc"
	    page_info = {}
	    count = cur.execute("select image, url, cmsplugin_picture.float from cmsplugin_picture where cmsplugin_ptr_id in (select id from cms_cmsplugin where placeholder_id in(select a.placeholder_id from cms_page_placeholders a, cms_placeholder b where page_id in(select id from cms_title where slug = '" + pageName + "') and slot = 'Products' and a.placeholder_id = b.id group by placeholder_id)) group by image")
	    if(count > 0):
	    	product = cur.fetchmany(count)
	    else:
	    	product = []
	    	
	    count = cur.execute("select image, url from cmsplugin_picture where cmsplugin_ptr_id in (select id from cms_cmsplugin where placeholder_id in(select a.placeholder_id from cms_page_placeholders a, cms_placeholder b where page_id in(select id from cms_title where slug = '" + pageName + "') and slot = 'Page_Describe' and a.placeholder_id = b.id group by placeholder_id)) group by image")
	    if(count > 0):
	    	desc = cur.fetchmany(count)
	    else:
	    	desc = []
	    page_info = {'product': product, 'desc': desc}
	    cur.close()
	    conn.close()
	    return page_info
	except MySQLdb.Error,e:
	     print "Mysql Error %d: %s" % (e.args[0], e.args[1])
