import wikipedia

    def simplify(list):

        meaningList = []
        wikipedia.set_lang("tr")
        
        for word in list:    
            try:
                page = wikipedia.page(word)
                meaning = page.content
                parsedMeaning = meaning.split("\n")
                meaningList.append(parsedMeaning[0])
                return meaningList
            except:
                print("Can't found!")
                return 0


