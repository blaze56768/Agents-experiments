from llama_index.core.tools import FunctionTool
from llama_index.tools.duckduckgo import DuckDuckGoSearchToolSpec
from huggingface_hub import list_models
import random

# ----------------------------
# Weather Info Tool
# ----------------------------

class WeatherInfoTool:
    def __init__(self):
        def get_weather(location: str) -> str:
            weather_conditions = [
                {"condition": "Rainy", "temp_c": 15},
                {"condition": "Clear", "temp_c": 25},
                {"condition": "Windy", "temp_c": 20}
            ]
            data = random.choice(weather_conditions)
            return f"Weather in {location}: {data['condition']}, {data['temp_c']}°C"

        self.tool = FunctionTool.from_defaults(
            fn=get_weather,
            name="weather_info",
            description="Fetches dummy weather information for a given location."
        )

    def get_tool(self):
        return self.tool

# ----------------------------
# Hub Stats Tool
# ----------------------------

class HubStatsTool:
    def __init__(self):
        def get_hub_stats(author: str) -> str:
            try:
                models = list(list_models(author=author, sort="downloads", direction=-1, limit=1))
                if models:
                    model = models[0]
                    return f"The most downloaded model by {author} is {model.id} with {model.downloads:,} downloads."
                else:
                    return f"No models found for author {author}."
            except Exception as e:
                return f"Error fetching models for {author}: {str(e)}"

        self.tool = FunctionTool.from_defaults(
            fn=get_hub_stats,
            name="hub_stats",
            description="Fetches the most downloaded model from a specific author on Hugging Face Hub."
        )

    def get_tool(self):
        return self.tool

# ----------------------------
# DuckDuckGo Search Tool
# ----------------------------

class DuckDuckGoTool:
    def __init__(self):
        tool_spec = DuckDuckGoSearchToolSpec()
        self.tool = FunctionTool.from_defaults(
            fn=tool_spec.duckduckgo_full_search,
            name="web_search",
            description="Searches the web using DuckDuckGo."
        )

    def get_tool(self):
        return self.tool













# from llama_index.tools.duckduckgo import DuckDuckGoSearchToolSpec
# from llama_index.core.tools import FunctionTool
# import random
# from huggingface_hub import list_models


# # Initialize the DuckDuckGo search tool
# #search_tool = DuckDuckGoSearchTool()
# # class DuckDuckGoSearchTool(Tool):

# #     tool_spec = DuckDuckGoSearchToolSpec()
# #     search_tool = FunctionTool.from_defaults(tool_spec.duckduckgo_full_search)

# #     return search_tool

# class WeatherInfoTool(FunctionTool):
#     name = "weather_info"
#     description = "Fetches dummy weather information for a given location."
#     inputs = {
#         "location": {
#             "type": "string",
#             "description": "The location to get weather information for."
#         }
#     }
#     output_type = "string"

#     def forward(self, location: str):
#         # Dummy weather data
#         weather_conditions = [
#             {"condition": "Rainy", "temp_c": 15},
#             {"condition": "Clear", "temp_c": 25},
#             {"condition": "Windy", "temp_c": 20}
#         ]
#         # Randomly select a weather condition
#         data = random.choice(weather_conditions)
#         return f"Weather in {location}: {data['condition']}, {data['temp_c']}°C"

# class HubStatsTool(FunctionTool):
#     name = "hub_stats"
#     description = "Fetches the most downloaded model from a specific author on the Hugging Face Hub."
#     inputs = {
#         "author": {
#             "type": "string",
#             "description": "The username of the model author/organization to find models from."
#         }
#     }
#     output_type = "string"

#     def forward(self, author: str):
#         try:
#             # List models from the specified author, sorted by downloads
#             models = list(list_models(author=author, sort="downloads", direction=-1, limit=1))
            
#             if models:
#                 model = models[0]
#                 return f"The most downloaded model by {author} is {model.id} with {model.downloads:,} downloads."
#             else:
#                 return f"No models found for author {author}."
#         except Exception as e:
#             return f"Error fetching models for {author}: {str(e)}"

