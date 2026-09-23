"""Validate benchmark comparison metadata before reporting a speedup.

No training data or model predictions are invented by this audit.
Usage: python benchmark_audit.py manifest.json
"""
import json
import math
import sys

def audit(manifest):
    required=['dataset_version','split_id','hardware','sample_count','epochs','seed','training_seconds']
    runs=manifest.get('runs',[])
    errors=[]
    for i,r in enumerate(runs):
        for k in ['model',*required]:
            if k not in r or r[k] is None or r[k]=='': errors.append(f"run {i}: missing {k}")
        for k in ['training_seconds','sample_count','epochs']:
            v=r.get(k)
            if isinstance(v,bool) or not isinstance(v,(int,float)) or not math.isfinite(v) or v<=0:
                errors.append(f"run {i}: invalid {k}")
    if len(runs)<2: errors.append('Need at least two measured model runs')
    if errors: return {'comparable':False,'issues':errors,'speedup':None}
    base=runs[0]
    for r in runs[1:]:
        for k in ['dataset_version','split_id','hardware','sample_count','epochs','seed']:
            if r[k]!=base[k]: errors.append(f"{r['model']}: unmatched {k}")
    return {'comparable':not errors,'issues':errors,
            'speedup': None if errors else {r['model']:base['training_seconds']/r['training_seconds'] for r in runs[1:]},
            'scope':'Recorded runtime comparison only; not evidence of quantum advantage or clinical usefulness'}

if __name__=='__main__':
    result=audit(json.load(open(sys.argv[1])))
    print(json.dumps(result,indent=2));sys.exit(0 if result['comparable'] else 2)
