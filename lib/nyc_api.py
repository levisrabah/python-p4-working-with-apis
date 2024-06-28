import requests
import json

class GetPrograms:
    def get_programs(self):
        URL = "http://data.cityofnewyork.us/resource/uvks-tn5n.json"
        response = requests.get(URL)
        return response.content
    def program_agencies(self):
        
        # We can use the json library to parse the API response into nocely formated JSON
        programs_list = []
        programs = json.loads(self.get_programs())
        for program in programs:
            programs_list.append(program['ageny'])
        return programs_list
    
programs = GetPrograms()
agencies = programs.program_agencies()
for agency in agencies:
    print (agency)