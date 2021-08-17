# Google Jobs API Integration

**AUTHOR**: Rebecca Wright

**DATE**: 7/22/21

These documents represent an excerpt of personal contributions made to development of the TRKR App.

Files pertain to the integration of the Google Jobs and Google Jobs Listing API in conjunction with the SerpAPI Wrapper, into a localized application-specific search interface.
<br><br>
***
<br>

## File Index:

0. api_presentation_deck

    >A) api_presentation_deck.pdf [(Quick Link)](./0_api_presentation_deck/api_presentation_deck.pdf)
        >- API Integration Report: slide deck (PDF format)

    >B) api_presentation_deck.pptx [(Quick Link)](./0_api_presentation_deck/api_presentation_deck.pptx)
        >- API Integration Report: slide deck (Powerpoint format)


1. executed_code_output_examples

    >A) executed_demo_api_usage.pdf [(Quick Link)](./1_executed_code_output_examples/executed_demo_api_usage.pdf)
    
    >B) executed_dummy_api_search_results.pdf [(Quick Link)](./1_executed_code_output_examples/executed_dummy_api_search_results.pdf)
    
    >C) executed_dummy_trackerlog.pdf [(Quick Link)](./1_executed_code_output_examples/executed_dummy_trackerlog.pdf)
        >- File folder contains pdfs of executed notebook files with their corresponding output values for demo purposes.


2. python_notebooks

    >A) demo_api_usage.ipynb [(Quick Link)](./2_python_notebooks/demo_api_usage.ipynb)
        >- An overview of the API usage.
        
    >B) generate_dummy_api_search_results.ipynb [(Quick Link)](./2_python_notebooks/generate_dummy_api_search_results.ipynb)
        >- API query usage as part of sample query results dataset creation.

    >C) generate_dummy_trackerlog.ipynb [(Quick Link)](./2_python_notebooks/generate_dummy_trackerlog.ipynb)
        >- Extention of sample query results dataset to create dummy dataset of user trackerlog entries.


3. python_scripts

    >A) google_jobs_api_script.py [(Quick Link)](./3_python_scripts/google_jobs_api_script.py)
        >- The Google Jobs API can be called using the [Google Jobs API Script](./3_python_scripts/google_jobs_api_script.py).  To run script, use the following command, passing a string of query parameters.
        >- *For example:*
        ```bash
        python google_jobs_api_script.py "ux designer new york"
        ```

    >B)  google_jobs_listing_api_script.py [(Quick Link)](./3_python_scripts/google_jobs_listing_api_script.py)
        >- The Google Jobs Listing API can be called using the [Google Jobs Listing API Script](./3_python_scripts/google_jobs_listing_api_script.py).  To run script, use the following command, passing a valid job_id value parameter.
    > - *For example:*
        ```bash
        python google_jobs_listing_api_script.py "eyJqb2JfdGl0bGUiOiJCYXJpc3RhIiwiY29tcGFueV9uYW1lIjoiQmx1ZSBCb3R0bGUgQ29mZmVlIiwiY29tcGFueV9taWQiOiIvbS8wM3AxMnFkIiwiYWRkcmVzc19jaXR5IjoiIiwiYWRkcmVzc19zdGF0ZSI6Ik5ldyBZb3JrIiwiaHRpZG9jaWQiOiI2TXhSRFBCMHNHajZEMzE3QUFBQUFBPT0iLCJobCI6ImVuIiwiZmMiOiJFdmNCQ3JjQlFVNVZYMDV4VkhSSVlVaExaREV6UkRoVE5HTkljbEpLV1daVVpFeEJXVnBGV1VwUVpXZElTemxCUjJZMFpsZE9WVXRoVjBWa1kwdzFaMGxGTXpsc01IbDRiSGxwWjJwb1FsZDJXbWRJWkc5T1drbHNMVlp3YkVaVmVsOW9ZemxLWDJOTFZsWmFNMmhWVUVaU1ZuRXpabEZRZVVkcE9WbDNRMVJ2YkZGYVkwOHRUakkyVlVGTVdXVmFhM2RRYjNacGRFWndUWE5MWHpKblUxUlNVVmxXVlRaeVpGWm5UMWh0ZEdOYVV6bFhZekZSTTNOWVJsWTBFaGQzV2pNMFdWQllRMEpsUTNjMVRtOVFjM1pYYWpaQmN4b2lRVTlOV1ZKM1FWZGlWV3hqWVc5a04xRk1aa2wzYjNOUFdUUnpOMFJHYTNRMVp3IiwiZmN2IjoiMyIsImZjX2lkIjoiZmNfNjEiLCJhcHBseV9saW5rIjp7InRpdGxlIjoiQXBwbHkgb24gTGlua2VkSW4iLCJsaW5rIjoiaHR0cHM6Ly93d3cubGlua2VkaW4uY29tL2pvYnMvdmlldy9iYXJpc3RhLWF0LWJsdWUtYm90dGxlLWNvZmZlZS0yNjUzNDQ1MzY5P3V0bV9jYW1wYWlnbj1nb29nbGVfam9ic19hcHBseVx1MDAyNnV0bV9zb3VyY2U9Z29vZ2xlX2pvYnNfYXBwbHlcdTAwMjZ1dG1fbWVkaXVtPW9yZ2FuaWMifX0="
        ```






<br><br>
***
<br>

## API Integration in Action:

- ### API Integration Report: slide deck
>[Integration Report slide deck (pdf format)](./0_api_presentation_deck/api_presentation_deck.pdf)<br>
>[Integration Report slide deck (pptx format)](./0_api_presentation_deck/api_presentation_deck.pptx)

- ### API Usage Demo
>An overview of the API usage can be found in the [Demo API Usage Notebook](./2_python_notebooks/demo_api_usage.ipynb).

- ### API Queries to Create Dummy Datasets
>The API was used to generate a collection of sample query results in the [Dummy API Search Results Notebook](./2_python_notebooks/generate_dummy_api_search_results.ipynb).<br>
>Those results were then used to generate a dummy dataset of user trackerlog entry data in the [Dummy Trackerlog Notebook](./2_python_notebooks/generate_dummy_trackerlog.ipynb).

- ### API Queries as Executable Python Script
>The Google Jobs API can be called using the [Google Jobs API Script](./3_python_scripts/google_jobs_api_script.py).  To run script, use the following command, passing a string of query parameters.  *For example:*
    ```bash
    python google_jobs_api_script.py "ux designer new york"
    ```
>The Google Jobs Listing API can be called using the [Google Jobs Listing API Script](./3_python_scripts/google_jobs_listing_api_script.py).  To run script, use the following command, passing a valid job_id value parameter.   *For example:*
    ```bash
    python google_jobs_listing_api_script.py "eyJqb2JfdGl0bGUiOiJCYXJpc3RhIiwiY29tcGFueV9uYW1lIjoiQmx1ZSBCb3R0bGUgQ29mZmVlIiwiY29tcGFueV9taWQiOiIvbS8wM3AxMnFkIiwiYWRkcmVzc19jaXR5IjoiIiwiYWRkcmVzc19zdGF0ZSI6Ik5ldyBZb3JrIiwiaHRpZG9jaWQiOiI2TXhSRFBCMHNHajZEMzE3QUFBQUFBPT0iLCJobCI6ImVuIiwiZmMiOiJFdmNCQ3JjQlFVNVZYMDV4VkhSSVlVaExaREV6UkRoVE5HTkljbEpLV1daVVpFeEJXVnBGV1VwUVpXZElTemxCUjJZMFpsZE9WVXRoVjBWa1kwdzFaMGxGTXpsc01IbDRiSGxwWjJwb1FsZDJXbWRJWkc5T1drbHNMVlp3YkVaVmVsOW9ZemxLWDJOTFZsWmFNMmhWVUVaU1ZuRXpabEZRZVVkcE9WbDNRMVJ2YkZGYVkwOHRUakkyVlVGTVdXVmFhM2RRYjNacGRFWndUWE5MWHpKblUxUlNVVmxXVlRaeVpGWm5UMWh0ZEdOYVV6bFhZekZSTTNOWVJsWTBFaGQzV2pNMFdWQllRMEpsUTNjMVRtOVFjM1pYYWpaQmN4b2lRVTlOV1ZKM1FWZGlWV3hqWVc5a04xRk1aa2wzYjNOUFdUUnpOMFJHYTNRMVp3IiwiZmN2IjoiMyIsImZjX2lkIjoiZmNfNjEiLCJhcHBseV9saW5rIjp7InRpdGxlIjoiQXBwbHkgb24gTGlua2VkSW4iLCJsaW5rIjoiaHR0cHM6Ly93d3cubGlua2VkaW4uY29tL2pvYnMvdmlldy9iYXJpc3RhLWF0LWJsdWUtYm90dGxlLWNvZmZlZS0yNjUzNDQ1MzY5P3V0bV9jYW1wYWlnbj1nb29nbGVfam9ic19hcHBseVx1MDAyNnV0bV9zb3VyY2U9Z29vZ2xlX2pvYnNfYXBwbHlcdTAwMjZ1dG1fbWVkaXVtPW9yZ2FuaWMifX0="
    ```