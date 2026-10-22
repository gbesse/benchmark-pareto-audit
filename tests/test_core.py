import unittest
from benchmark_pareto_audit import run
class DomainTests(unittest.TestCase):
 def test_robust_dominance_with_intervals(self):
  r=run({'objectives':{'quality':'max','cost':'min'},'candidates':[{'id':'a','metrics':{'quality':[.9,1],'cost':[1,2]}},{'id':'b','metrics':{'quality':[.7,.8],'cost':[3,4]}}]});self.assertEqual(r['candidates'][1]['definitely_dominated_by'],['a'])
 def test_overlap_not_definite_dominance(self):
  r=run({'objectives':{'cost':'min'},'candidates':[{'id':'a','metrics':{'cost':[1,3]}},{'id':'b','metrics':{'cost':[2,4]}}]});self.assertEqual(r['candidates'][1]['definitely_dominated_by'],[]);self.assertEqual(r['candidates'][1]['possibly_dominated_by'],['a'])
 def test_missing_metric_not_zero(self):
  r=run({'objectives':{'cost':'min'},'candidates':[{'id':'a','metrics':{}}]});self.assertEqual(r['candidates'],[]);self.assertEqual(len(r['excluded_missing_measurements']),1)
 def test_equal_points_both_efficient(self):
  r=run({'objectives':{'x':'min'},'candidates':[{'id':id,'metrics':{'x':1}} for id in 'ab']});self.assertTrue(all(x['certainly_efficient_within_complete_rows'] for x in r['candidates']))
 def test_tradeoff_not_total_ranking(self):
  r=run({'objectives':{'cost':'min','quality':'max'},'candidates':[{'id':'a','metrics':{'cost':1,'quality':1}},{'id':'b','metrics':{'cost':2,'quality':2}}]});self.assertTrue(all(x['not_definitely_dominated'] for x in r['candidates']))
