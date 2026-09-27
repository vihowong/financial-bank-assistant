import sys, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
from validate_bic import validate_bic
from normalize_bank_name import normalize
from parse_transfer_data import parse
from mask_sensitive_data import mask_text

class TestSkillScripts(unittest.TestCase):
    def test_bic_11_valid(self):
        r=validate_bic("hsbcHKhhxxx"); self.assertTrue(r["syntax_valid"]); self.assertEqual(r["country_code"],"HK")
    def test_bic_invalid(self): self.assertFalse(validate_bic("TOO-SHORT")["syntax_valid"])
    def test_bank_alias(self):
        r=normalize("BofA"); self.assertEqual(r["canonical_name"],"Bank of America")
    def test_transfer_parse(self):
        r=parse("Bank Name: Example Bank\nSWIFT: ABCDUS33XXX\nAccount Number: 1234567890\nRouting Number: 021000021")
        self.assertEqual(r["bic_swift"],["ABCDUS33XXX"]); self.assertEqual(r["routing_number"],["021000021"])
    def test_mask(self):
        out=mask_text("Account: 1234567890123456"); self.assertIn("************3456",out)
