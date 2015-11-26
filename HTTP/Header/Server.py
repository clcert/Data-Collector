# import json
#
# __author__ = 'eduardo'
#
# Example = '{"ip":"190.153.249.88","header":{"null":["HTTP/1.1 200 OK"],"X-Frame-Options":["SAMEORIGIN"],"Date":["Tue, 10 Nov 2015 21:12:07 GMT"],"Content-Length":["95"],"Expires":["Thu, 31 Dec 2037 23:55:55 GMT"],"Last-Modified":["Fri, 25 Sep 2015 16:05:02 GMT"],"Accept-Ranges":["bytes"],"Connection":["keep-alive"],"Content-Type":["text/html"],"Server":["BarracudaHTTP 4.0"],"Cache-Control":["public","max-age=315360000"]}}'
#
# json_data = json.loads(Example)
# header = json_data['header']
#
# response_status = header['null']
# server = header['Server']
#
# print response_status
# print server
