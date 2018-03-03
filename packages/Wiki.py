import wikipedia

class Wiki:
 
    def search_wiki(self, text=''):
        searchResults = wikipedia.search(text)
        
        # If there is no result, print no result
        if not searchResults:
            return ""
        # Search for page... try block 
        try:
            page = wikipedia.page(searchResults[0])
        except wikipedia.DisambiguationError as err:
            # Select the first item in the list
            page = wikipedia.page(err.options[0])
        
        #encoding the response to utf-8
        wikiTitle = str(page.title.encode('utf-8'))
        wikiSummary = str(page.summary.encode('utf-8'))
        # printing the result
        return wikiSummary