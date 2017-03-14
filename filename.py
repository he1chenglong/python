#-*-encoding:utf-8-*-
import os

rootdir =u"E:\BaiduNetdiskDownload\RKDocs\Platform-support-lists"

rootdir=u"E:\BaiduNetdiskDownload\RKDocs\Develop reference documents"

rootdir=u"E:\BaiduNetdiskDownload\RKDocs\RKTools-manuals"
for parent,dirnames,filenames in os.walk(rootdir): 
	 for filename in filenames: 
		print  filename