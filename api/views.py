from rest_framework.response import Response
from rest_framework.decorators import api_view
from datetime import datetime
from django.http import JsonResponse


@api_view(['GET'])
def getData(request):
    # Get the 'name' and 'track' query parameters from the request
    name = request.GET.get('slack_name')
    track = request.GET.get('track')

        # Validate the 'name' and 'track' parameters
    if not name or not track:
        return JsonResponse({'error': 'Both name and track parameters are required.'}, status=400)

    #Current date and time
    utc_time = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
    current_day = datetime.now().strftime('%A')


    # Prepare the response JSON
    response_data = {
        'slack_name': name,

        'current_day': current_day,
        'utc_time':utc_time ,
        'track': track,
        'github_file_url':'https://github.com/AkanEdwin/stage-one/blob/main/endpoint', 
        'github_repo_url':'https://github.com/AkanEdwin/stage-one', 
        'status_code':'200'
        }

    return JsonResponse(response_data)
