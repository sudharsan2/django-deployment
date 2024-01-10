from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from .serializer import error_code_serializer
from l1_support.models import error_code
from rest_framework.response import Response
from django.http import JsonResponse
from django.db import connection
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
# import cx_Oracle

# @api_view(['GET'])
# def func1(request):
#     model = error_code.objects.all()
#     serializer = error_code_serializer(model,many=True)
#     return serializer.data

# Create your views here.

class ResumeQueryAPIView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        try:
            pk = kwargs.get('pk')
            models = error_code.objects.get(error_id = pk)
            # models = error_code.objects.all()
            serializer = error_code_serializer(instance=models)
            serialized_data = serializer.data
            results = {}
            # sql_query=[]

            # for i in serialized_data:
            for key, values in serialized_data.items():
                check_list = serialized_data.get('check_list')

                if isinstance(check_list, dict):
                    query_results = {}
                    sql_query=[]

                    for query_key, query_values in check_list.items():
                        if isinstance(query_values, list) and query_values and len(query_values) >= 2:
                            # sql_query = " ".join(query_values)
                            sql_query.append(query_values[1])
                            # sql_query.update({query_key: query_values[1]})
                    # return JsonResponse(sql_query, safe= False)

                            # try:
                            #     with connection.cursor() as cursor:
                            #         cursor.execute(sql_query)
                            #         columns = [col[0] for col in cursor.description]
                            #         query_results[query_key] = [dict(zip(columns, row)) for row in cursor.fetchall()]

                            # except cx_Oracle.DatabaseError as e:
                            #     error, = e.args
                            #     query_results[query_key] = {'error': f'Error executing SQL query: {error.message}'}

                    # results[model.id] = query_results
            return JsonResponse({'sql_query': sql_query})
            # sql_query=[]
        except json.JSONDecodeError:
            return JsonResponse({'message': 'Invalid JSON data'})

        # return JsonResponse({'data': results})
