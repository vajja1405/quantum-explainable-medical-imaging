import unittest
from benchmark_audit import audit
class AuditTests(unittest.TestCase):
    def runs(self):
        a=dict(model='CNN',dataset_version='v1',split_id='s1',hardware='same',sample_count=100,epochs=10,seed=1,training_seconds=10)
        return [a,{**a,'model':'QCNN','training_seconds':2}]
    def test_matched_comparison(self):
        self.assertEqual(audit({'runs':self.runs()})['speedup'],{'QCNN':5})
    def test_hardware_mismatch(self):
        r=self.runs();r[1]['hardware']='different';self.assertIsNone(audit({'runs':r})['speedup'])
    def test_missing_evidence(self): self.assertFalse(audit({'runs':[]})['comparable'])
    def test_invalid_runtime(self):
        for v in [0,-1,float('nan'),True]:
            r=self.runs();r[1]['training_seconds']=v;self.assertFalse(audit({'runs':r})['comparable'])
