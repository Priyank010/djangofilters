from mainApp.models import *
from mainApp.serializers import *
from rest_framework import viewsets

class StudentsViewSet(viewsets.ModelViewSet):
    # queryset = Students.objects.all()
    serializer_class = StudentsSerializer

    def get_queryset(self):
        first_name = self.request.query_params.get('first_name', None)
        first_name_contains = self.request.query_params.get('first_name_contains', None)
        first_name_starts_with = self.request.query_params.get('first_name_starts_with', None)
        first_name_exact = self.request.query_params.get('first_name_exact', None)
        last_name_icontains = self.request.query_params.get('last_name_icontains', None)
        last_name_ends_with = self.request.query_params.get('last_name_ends_with', None)
        last_name_iexact = self.request.query_params.get('last_name_iexact', None)
        last_name_null = self.request.query_params.get('last_name_null', None)
        roll_number_in = self.request.query_params.get('roll_number_in', None)
        marks_greater_than = self.request.query_params.get('marks_greater_than', None)
        marks_greater_or_equals_to = self.request.query_params.get('marks_greater_or_equals_to', None)
        marks_lesser_than = self.request.query_params.get('marks_lesser_than', None)
        marks_lesser_or_equals_to = self.request.query_params.get('marks_lesser_or_equals_to', None)
        exam_passed = self.request.query_params.get('exam_passed', None)
        roll_number_range = self.request.query_params.get('roll_number_range', None)
        first_name_range = self.request.query_params.get('first_name_range', None)
        birth_date = self.request.query_params.get('birth_date', None)
        birth_year = self.request.query_params.get('birth_year', None)
        birth_iso_year = self.request.query_params.get('birth_iso_year', None)
        birth_month = self.request.query_params.get('birth_month', None)
        birth_week = self.request.query_params.get('birth_week', None) #4
        birth_week_day = self.request.query_params.get('birth_week_day', None) #4
        birth_iso_week_day = self.request.query_params.get('birth_iso_week_day', None) #3
        birth_day = self.request.query_params.get('birth_day', None)
        birth_hour = self.request.query_params.get('birth_hour', None)
        birth_minute = self.request.query_params.get('birth_minute', None)
        birth_second = self.request.query_params.get('birth_second', None) #00
        queryset = Students.objects.all()

        # Exact match
        if first_name is not None:
            queryset = queryset.filter(first_name=first_name)
        
        # Contains
        if first_name_contains is not None:
            queryset = queryset.filter(first_name__contains=first_name_contains)

        # Starts_with
        if first_name_starts_with is not None:
            queryset = queryset.filter(first_name__startswith=first_name_starts_with)
        
        # Exact match
        if first_name_exact is not None:
            queryset = queryset.filter(first_name__exact=first_name_exact)

        # icontains
        if last_name_icontains is not None:
            queryset = queryset.filter(last_name__icontains=last_name_icontains)

        # Ends_with
        if last_name_ends_with is not None:
            queryset = queryset.filter(last_name__endswith=last_name_ends_with)

        # iexact
        if last_name_iexact is not None:
            queryset = queryset.filter(last_name__iexact=last_name_iexact)

        # isnull
        if last_name_null is not None:
            queryset = queryset.filter(last_name__isnull=True)

        # Number_in
        if roll_number_in is not None:
            queryset = queryset.filter(roll_number__in=roll_number_in)

        # Greater_than
        if marks_greater_than is not None:
            queryset = queryset.filter(marks__gt=marks_greater_than)

        # Greater_than_or_euqals_to
        if marks_greater_or_equals_to is not None:
            queryset = queryset.filter(marks__gte=marks_greater_or_equals_to)

        # Lesser_then
        if marks_lesser_than is not None:
            queryset = queryset.filter(marks__lt=marks_lesser_than)

        # Lesser_then_or_equals_to
        if marks_lesser_or_equals_to is not None:
            queryset = queryset.filter(marks__lte=marks_lesser_or_equals_to)

        # Boolean
        if exam_passed is not None:
            queryset = queryset.filter(exam_passed=exam_passed)

        # Range
        if roll_number_range is not None:
            queryset = queryset.filter(roll_number__range=roll_number_range)

        # Range (Character)
        if first_name_range is not None:
            queryset = queryset.filter(first_name__range=first_name_range)

        # Date
        if birth_date is not None:
            queryset = queryset.filter(birth_date__date=birth_date)

        # Year
        if birth_year is not None:
            queryset = queryset.filter(birth_date__year=birth_year)

        # Ios_year
        if birth_iso_year is not None:
            queryset = queryset.filter(birth_date__iso_year=birth_iso_year)

        # Month
        if birth_month is not None:
            queryset = queryset.filter(birth_date__month=birth_month)
        
        # Week
        if birth_week is not None:
            queryset = queryset.filter(birth_date__week=birth_week)

        # Week_day
        if birth_week_day is not None:
            queryset = queryset.filter(birth_date__week_day=birth_week_day)
        
        # Iso_week_day
        if birth_iso_week_day is not None:
            queryset = queryset.filter(birth_date__iso_week_day=birth_iso_week_day)

        # Day
        if birth_day is not None:
            queryset = queryset.filter(birth_date__day=birth_day)

        # Hour
        if birth_hour is not None:
            queryset = queryset.filter(birth_date__hour=birth_hour)

        # Minute
        if birth_minute is not None:
            queryset = queryset.filter(birth_date__minute=birth_minute)

        # Second
        if birth_second is not None:
            queryset = queryset.filter(birth_date__second=birth_second)
        return queryset