from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render
from .models import error_code
import json

# Create your views here.
def function1(request):
    json_path =  "/Users/smartass/coding/python/django/L1_phase1/l1_automation/l1_support/validated_sql.json"
    with open(json_path, 'r') as file:
        json_data = json.load(file)

    for Error_code, details in json_data.items():
            # last_update_str = details.get('Last Update', '')
            # last_update = datetime.strptime(last_update_str, '%Y-%m-%d %H:%M:%S') if last_update_str and last_update_str.lower() != 'nothing' else None
            new_instance = error_code(
                error_id=Error_code,
                module=details.get('Module'),
                url=details.get('URL'),
                applies_to=details.get('Applies To'),
                symptoms=details.get('Symptoms'),
                cause=details.get('Cause'),
                solution=details.get('Solution'),
                last_update= details.get('Last Update'),
                check_list=details.get('check_list'),
                place_holder=details.get('place_holder')
            )
            new_instance.save()

    return HttpResponse("Data inserted successfully.")
