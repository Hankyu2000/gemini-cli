import requests
import sys
import json
import os
import google.generativeai as genai
from rich.console import Console
from rich.markdown import Markdown

def main():

    console = Console()
    key = os.getenv('GEMINI_API_KEY')
    if key is None:
        print("Please set the GEMINI_API_KEY environment variable. If you don't have one, go get it.")
        sys.exit(1)

    genai.configure(api_key=os.environ["GEMINI_API_KEY"])
    args = sys.argv
    query = ""
    if len(args) > 1:
        print("Too many arguments: 1 expected\n")
        sys.exit(1)
    elif len(args) == 1:
        is_query_entry_completed = False
        while(not is_query_entry_completed):
            print("Query:", end=" ")
            query = input()
            if query == "":
                print("Please enter a query.")
            else:
                is_query_entry_completed = True
                break

    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(query)
    response_data = response.text
    md = Markdown(response_data)
    console.print(md)
    sys.exit(0)

if __name__ == '__main__':
    main()