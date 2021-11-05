import sys
import requests
from urllib3.exceptions import InsecureRequestWarning
args=sys.argv
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

def downloadFile2folder(file,folder):
    with open(file,'r') as file:
        for line in file:
            line=line.replace('\n','')
            line=line.split(' ')
            link=line[-1:][0]
            name="".join(line[:-1])+".pdf"
            name=name.replace(':','')
            try:
                response=requests.get(link, verify=False)
                if response.status_code==200:
                    if response.content[:4]==b'%PDF':
                        with open(folder+'/'+name,'wb') as pdf:
                            pdf.write(response.content)
                    else:
                        print(f"Error: No PDF {name} {response.status_code}: {link}")
                else:
                    print(f"Algo saló mal con {name} {response.status_code}: {link}")
            except:
                print(f"Algo saló mal con {name} {response.status_code}: {link}")

downloadFile2folder(args[1],args[2])
