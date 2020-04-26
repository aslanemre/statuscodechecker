import requests
print""
site = raw_input("[ ? ]  Enter Site : ")
print ""
reGet = requests.get(site)
rePost = requests.post(site)
rePut = requests.put(site)
reDel = requests.delete(site)
print "--------------------- Get Method Checked --------------------------- "
print "[ + ] Site : ",site
print "[ + ] Status Code : ",reGet.status_code
print "[ + ] Requestable : ",reGet.ok
print "[ + ] Timing : ",reGet.elapsed.total_seconds()
print "---------------------------------------------------------------------------"
print ""
print "-------------------- Post Method Checked --------------------------- "
print "[ + ] Site : ",site
print "[ + ] Status Code : ",rePost.status_code
print "[ + ] Requestable : ",rePost.ok
print "[ + ] Timing : ",rePost.elapsed.total_seconds()
print "---------------------------------------------------------------------------"
print ""
print "--------------------- Put Method Checked --------------------------- "
print "[ + ] Site : ",site
print "[ + ] Status Code : ",rePut.status_code
print "[ + ] Requestable : ",rePut.ok
print "[ + ] Timing : ",rePut.elapsed.total_seconds()
print "---------------------------------------------------------------------------"
print ""
print "------------------- Delete Method Checked -------------------------- "
print "[ + ] Site : ",site
print "[ + ] Status Code : ",reDel.status_code
print "[ + ] Requestable : ",reDel.ok
print "[ + ] Timing : ",reDel.elapsed.total_seconds()
print "---------------------------------------------------------------------------"
print ""
