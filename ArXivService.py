import requests
import xml.etree.ElementTree as ElementTree

class ArXivService:
    def get_search_results(self, search_query: str, start: str, max_results: str, sort_by: str, sort_order: str):
        api_url = 'http://export.arxiv.org/api/query?search_query={}&start={}&max_results={}&sortBy={}&sortOrder={}'
        resp = requests.get(api_url.format(search_query, start, max_results, sort_by, sort_order))
        root = ElementTree.fromstring(resp.content)
        ns = {'base_ns': 'http://www.w3.org/2005/Atom'}
        entries = []
        for index, entry in enumerate(root.findall('base_ns:entry', ns)):
            entries.append({
                'title': entry.find('base_ns:title', ns).text,
                'summary': entry.find('base_ns:summary', ns).text,
            })
        return entries


