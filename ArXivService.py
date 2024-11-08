import requests
import xml.etree.ElementTree as ElementTree

class ArXivService:
    def get_search_results(self, search_query: str, start: str, max_results: str):
        api_url = 'http://export.arxiv.org/api/query?search_query={}&start={}&max_results={}'
        resp = requests.get(api_url.format(search_query, start, max_results))
        root = ElementTree.fromstring(resp.content)
        ns = {'base_ns': 'http://www.w3.org/2005/Atom'}
        entries = []
        for entry in root.findall('base_ns:entry', ns):
            authors = []
            for author in entry.findall('base_ns:author', ns):
                authors.append(author.find('base_ns:name', ns).text)
            entries.append({
                'id': entry.find('base_ns:id', ns).text,
                'title': entry.find('base_ns:title', ns).text,
                'summary': entry.find('base_ns:summary', ns).text,
                'authors': authors,
                'link': entry.find('base_ns:link', ns).attrib['href'],
            })
        return entries


