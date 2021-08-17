""" APPLICATION DOCUMENTATION
    -------------------------

    Purpose:    To execute a secondart query call to the Google Jobs Listing API using the SerpAPI Wrapper API to retrieve all relavant apply_options associated with job_id from previous search results.

    Parameters: string of unique job_id

    Returns: All available application options (of unknown collection length) associated with job_id as a json file titled "apply_option_results.json", written out to the same filepath location in the following format:
        {
            "title":          // string application location (ie "apply on linkedin")
            "link":             // string application url
        }
    
        Dependencies:  A valid api_key must be obtained through https://serpapi.com/ and assigned as local api_key system variable.
"""


# *****************************************************************************************************************************************************
# *****************************************************************************************************************************************************
# IMPORTS
import pandas as pd
import sys
import json
#import api_config_file    #NOT INCLUDED in github repo


# *****************************************************************************************************************************************************
# SYSTEM VARIABLES
api_key = api_config_file.api_key

# *****************************************************************************************************************************************************
# *****************************************************************************************************************************************************
# *****************************************************************************************************************************************************

# MAIN APPLICATION

job_id_var = sys.argv[1]

from serpapi import GoogleSearch

params = {
  "engine": "google_jobs_listing",
  "q": job_id_var,
  "api_key": api_key
}

search = GoogleSearch(params)
results = search.get_dict()
apply_results = results['apply_options']

with open('apply_option_results.json', 'w') as write_file:
    json.dump(apply_results, write_file)
