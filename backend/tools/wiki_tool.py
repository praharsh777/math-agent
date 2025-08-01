from langchain.tools import Tool
from langchain.utilities import WikipediaAPIWrapper

# Wikipedia search wrapper
wiki = WikipediaAPIWrapper()

# Create LangChain tool
wikipedia_tool = Tool(
    name="Wikipedia Search",
    func=wiki.run,
    description="Use this tool to search for general knowledge or factual questions when not found in the Knowledge Base"
)
