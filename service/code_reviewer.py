from azure_services import AzureSearch, AzureOpenAI

class CodeReviewer:
    def __init__(self, language="python"):
        self.search = AzureSearch(language=language)  # ⭐ AI Search
        self.openai = AzureOpenAI()                    # ⭐ OpenAI
    