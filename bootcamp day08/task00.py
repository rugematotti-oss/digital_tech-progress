from __future__ import annotations
DEFAULT_AU= "EpitechDataBootcamp/1.0 (+https://epitech.eu)"


def build_headers(user_agent: str | None = None) -> dict:
 if user_agent is not None and not isinstance(user_agent, str):
    raise TypeError("user_agent should be string")
 ua= DEFAULT_AU if user_agent is None else user_agent
 return{
   "User-Agent": ua
 }

def normalize_url(url: str) -> str:
  if not isinstance(url, str):
    raise TypeError("url must be a string")
  r= url.strip()
  if r == "":
    raise ValueError("the url can't be empty")
  if not (r.startswith("http://") or r.startswith("https://")):
    r= "https://"+ r
  return r
