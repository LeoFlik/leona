import pandas as pd
import requests as rq


morse_code_request = rq.get("https://morsecode.world/international/morse2.html")
