import requests
from requests import RequestException


def get_alerts(state_code, urgency, severity, certainty, max_results):
    """

    :param state_code: US 2 Alpha State Code
    :param urgency: immediate, expected, future, past, unknown
    :param severity: extreme, severe, moderate, minor, unknown
    :param certainty: observed, likely, possible, unlikely, unknown
    :param max_results: Maximum number of results to return
    :return: HTTP Status Code and List of Results
    """

    #  Create the NOAA URL
    url = f"https://api.weather.gov/alerts/active?" \
          f"area={state_code}&urgency={urgency}&severity={severity}&certainty={certainty}&limit={max_results}"

    headers = {'Accept': 'application/geo+json'}

    try:
        response = requests.get(url, headers=headers)
    except RequestException as re:
        return response.status_code, []

    #  If HTTP Status Code is not 200, we received an error
    if response.status_code != 200:
        return response.status_code, []

    #  Attempt to get the JSON Response
    try:
        response_body = response.json()
        #  Valid JSON was returned, format the response
        results = format_response(response_body, max_results)
        return response.status_code, results
    except:
        #  JSON wasn't returned, display an error for the user
        return response.status_code, []


def format_response(response, max_results):
    """

    :param response: JSON Response from NOAA API
    :param max_results: Maximum number of results to return
    :return: Formated response to display to the user
    """
    formatted_response = []
    #  Verify the features key is in the response
    if 'features' in response:
        #  Loop over each feature in the features list and build the response
        for feature in response['features']:
            #  Verify that the properties key is in the feature dictionary
            if 'properties' in feature:
                properties = feature['properties']
                #  Get the values to display to the user, if they don't exist in the JSON, default the values
                headline = properties.get('headline', '')
                description = properties.get('description', '')
                effective = properties.get('effective', '')
                expires = properties.get('expires', '')
                area_desc = properties.get('areaDesc', '')
                #  Verify that geocode is in properties
                if 'geocode' in properties:
                    geocode = properties['geocode']
                    same_list = geocode.get('SAME', [])
                else:
                    same_list = []

                #  Build feature dictionary and append to formatted response list
                feature_dict = {
                    'headline': headline,
                    'description': description,
                    'effective': effective,
                    'expires': expires,
                    'area_desc': area_desc,
                    'same_codes': ", ".join(same_list)
                }
                formatted_response.append(feature_dict)
                #  Only return the maximum number of results requested
                if len(formatted_response) == max_results:
                    return formatted_response
    return formatted_response

