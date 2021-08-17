""" APPLICATION DOCUMENTATION
    -------------------------

    Purpose:    To execute a search query call to the Google Jobs API using the SerpAPI Wrapper API.

    Parameters: string of query parameter terms

    Returns: Search result object of 10 listings as a json file titled "api_search_results.json", written out to the same filepath location in the following format:
        {
            "title":                    // string of job position
            "company_name":             // string of company name
            "location":                 // string of job location
            "via":                      // string of job posting source
            "description":              // strings of job description
            "thumbnail":                // string of url location of thumbnail image location.  can be null value.
            "extensions":               // array of strings of job details
            "detected_extensions":      // array of key value pairs of same job details
            "job_id":                   // unique string identifier
        }​
    
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

param_var = sys.argv[1]

from serpapi import GoogleSearch

params = {
  "engine": "google_jobs",
  "q": param_var,
  "hl": "en",
  "api_key": api_key
}

search = GoogleSearch(params)
results = search.get_dict()
jobs_results = results['jobs_results']

with open('api_search_results.json', 'w') as write_file:
    json.dump(jobs_results, write_file)
