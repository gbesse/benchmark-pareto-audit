from .common import number,identifier,unique_ids

def run(data):
    objectives=data['objectives'];candidates=data['candidates']
    if not 1<=len(objectives)<=20 or len(candidates)>500:raise ValueError('size')
    unique_ids(candidates)
    for key,direction in objectives.items():
        identifier(key)
        if direction not in ('min','max'):raise ValueError('direction')
    complete={};excluded=[]
    for c in candidates:
        missing=[k for k in objectives if k not in c['metrics'] or c['metrics'][k] is None]
        if missing:excluded.append({'id':c['id'],'missing_metrics':missing});continue
        row=[]
        for k,direction in objectives.items():
            value=c['metrics'][k];lo,hi=value if isinstance(value,list) and len(value)==2 else (value,value);number(lo,-1e12,1e12);number(hi,lo,1e12);row.append((lo,hi) if direction=='min' else (-hi,-lo))
        complete[c['id']]=row
    def certain(a,b):return all(x[1]<=y[0] for x,y in zip(a,b)) and any(x[1]<y[0] for x,y in zip(a,b))
    def possible(a,b):return all(x[0]<=y[1] for x,y in zip(a,b)) and any(x[0]<y[1] for x,y in zip(a,b))
    rows=[]
    for key,value in complete.items():
        dominators=[k for k,v in complete.items() if k!=key and certain(v,value)];potential=[k for k,v in complete.items() if k!=key and possible(v,value)]
        rows.append({'id':key,'definitely_dominated_by':dominators,'possibly_dominated_by':potential,'certainly_efficient_within_complete_rows':not potential,'not_definitely_dominated':not dominators})
    return {'candidates':rows,'excluded_missing_measurements':excluded,'comparison_scope':'complete rows and declared rectangular metric bounds; missing measurements are unknown, not zero; no general SOTA claim'}
