#type: ignore
import json
import re
def table2dict(table,ignorerequired=False):
    result=[]
    for n, line in enumerate(table.split('\n')):
        data = {}
        if n == 0:
            pass
        if n > 1:
            #print(line)
            values = [t.strip() for t in line[0:-1].split('|')]
            if not ignorerequired:
                result.append({'name':values[0],'type':values[1],'required':values[2],'Sample':values[3],'description':values[4]})
            else:
                result.append({'name': values[0], 'type': values[1], 'Sample': values[2],
                               'description': values[3]})
    return result
def parser(document_id):
    with open(f'data/{document_id}.json','r',encoding='utf-8') as f:
        data=json.loads(f.read())
        data=data['data']
        print('dataL',document_id)
        content=data['content']
        dic={}
        dic['title']=data['title']
        #print('conent:',content)
        dic['path']=re.findall(r'Path:  (.*?)\n',content)[0]
        dic['method']=re.findall(r'Method: \[(.*?)\]',content)[0]
        dic['description']=re.findall(r'Function Description\n(.*?)\n\n',content,re.DOTALL)[0]
        table=re.findall(r'Common Parameters\n(\|  Prope.*?)\n\n\n# Request',content,re.DOTALL)[0]
        dic['parameters'] = table2dict(table)
        table = re.findall(r'Request Parameters\n(\|  Prope.*?)\n\n\n# Request', content, re.DOTALL)[0]
        dic['request']=table2dict(table)
        dic['content']=data['content']
        table= re.findall(r'Response Parameters\n(\|  Prope.*?)\n\n\n# Res', content, re.DOTALL)[0]
        print('???')
        dic['response']=table2dict(table,ignorerequired=True)
        print(dic)
        return dic
def getparams(parameters,typename='otherere'):

    result=[]
    for param in parameters:
        #print('param:',param)
        item={'name':param['name'],'required':True if 'required' in param and param['required'].lower()=='y' else False,
              'description':param['description'] if 'description' in param else '',

              }
        if typename == 'parameters':
            item['in']='query'
        result.append(item)
    return result
typedic={'int':'integer','string':'string','bool':'boolean','timestamp':'integer'}
def getshema(itemlist,parent,i,parentstart):
    stopbreak = True
    while i<len(itemlist):

        name=itemlist[i]['name'];
        realname=name.strip('^')
        positions=name.rfind('^')+1
        try:

            lastposition=itemlist[i-1 if i-1>=0 else 0]['name'].rfind('^')+1
        except Exception as e:
            lastposition=0
        print('i:',i,'realnaem:',realname,'positions:',positions,'pastname:',itemlist[i-1 if i-1>=0 else 0]['name'],'lastposition:',lastposition)
        print('parentpo::',parentstart)
        if positions<lastposition and (positions-1)!=parentstart:
            return i-1
        if itemlist[i]['type'] in ['int','string','bool','timestamp']:

            parent["properties"][realname]={
                "description": "" if 'description' not in itemlist[i] else itemlist[i]['description'],
                'type':typedic[itemlist[i]['type']],

            }
        elif itemlist[i]['type']=='object':
            parent["properties"][realname]={'type':'object','properties':{},'required':[]}
            i=getshema(itemlist,parent["properties"][realname],i+1,positions)

        elif itemlist[i]['type']=='[]object':
            parent["properties"][realname]={'type':'array','items':{'type':'object','properties':{},'required':[]}}
            i = getshema(itemlist, parent["properties"][realname]['items'], i + 1,positions)

        elif itemlist[i]['type'] in ['[]string','[]int','[]bool']:
            parent["properties"][realname]={'type':'array','items':{'type':typedic[itemlist[i]['type'].replace('[]','')]}}
        if 'required' in itemlist[i] and itemlist[i]['required'].lower()=='y':
            parent["required"].append(realname)

        i+=1
    return i-1
if __name__ =='__main__':
    docuemnt=parser('237485')
    #print('docuemnt:',docuemnt)
    #print(docuemnt['request'])
    if '**Body**' in docuemnt['content']:
        t=getparams(docuemnt['parameters'],'parameters')
        requestbody = {'type': 'object', 'properties': {}, 'required': []}
        getshema(docuemnt['request'],requestbody ,0,-1)
        #print('tt',docuemnt['request'])
        print('request:',json.dumps(requestbody))
    else:
        t=getparams(docuemnt['parameters']+docuemnt['request'],'parameters')
    #rootshema={'type':'object','properties':{},'required':[]}
    #print('content:',docuemnt['response'])
    #response=getshema(docuemnt['response'],rootshema,0)
    #print(json.dumps(rootshema))