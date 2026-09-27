import json, sys, unittest
from pathlib import Path
from unittest.mock import patch
ROOT=Path(__file__).resolve().parents[1]; sys.path.insert(0,str(ROOT))
from providers.http_json import NormalizedHTTPProvider
from providers.router import ProviderRouter
from scripts.validate_bic import validate_bic

class LiveLayerTests(unittest.TestCase):
    def test_router_unconfigured(self):
        r=ProviderRouter(); result=r.lookup_bic("ABCDUS33XXX")
        self.assertFalse(result.ok); self.assertIn("configured",result.error.lower())
    def test_http_provider(self):
        p=NormalizedHTTPProvider(base_url="https://data.example.test",api_key="secret")
        with patch("providers.http_json.urllib.request.urlopen") as urlopen:
            class Resp:
                def __enter__(self): return self
                def __exit__(self,*args): return False
                def read(self): return json.dumps({"bic":"ABCDUS33XXX","status":"active","source":{"source_tier":2,"source_type":"licensed_api","source_name":"Test Provider"}}).encode()
            urlopen.return_value=Resp()
            result=p.lookup_bic("ABCDUS33XXX")
            self.assertTrue(result.ok)
            req=urlopen.call_args.args[0]; self.assertIn("/bic/ABCDUS33XXX",req.full_url)
            self.assertEqual(req.get_header("Authorization"),"Bearer secret")
    def test_local_bic(self):
        self.assertTrue(validate_bic("abcd us33 xxx")["syntax_valid"])
