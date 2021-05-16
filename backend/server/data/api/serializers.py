from rest_framework import serializers

from accounts.models import Account
from data.models import Data, Notification


class DataSerializer(serializers.ModelSerializer):
    colors = serializers.SerializerMethodField('get_colors')

    def get_colors(self, obj):
        # Set colors
        value = {}

        for barber in Account.objects.filter(is_admin=True).values_list('slug', 'color'):
            value[barber[0]] = barber[1]

        return value

    def to_internal_value(self, data):
        if 'start_work_sunday' in data and not(data['start_work_sunday']):
            data['start_work_sunday'] = None
        if 'end_work_sunday' in data and not(data['end_work_sunday']):
            data['end_work_sunday'] = None
        if 'end_work_saturday' in data and not(data['end_work_saturday']):
            data['end_work_saturday'] = None
        if 'start_work_saturday' in data and not(data['start_work_saturday']):
            data['start_work_saturday'] = None
        if 'end_work_friday' in data and not(data['end_work_friday']):
            data['end_work_friday'] = None
        if 'start_work_friday' in data and not(data['start_work_friday']):
            data['start_work_friday'] = None
        if 'end_work_thursday' in data and not(data['end_work_thursday']):
            data['end_work_thursday'] = None
        if 'start_work_thursday' in data and not(data['start_work_thursday']):
            data['start_work_thursday'] = None
        if 'end_work_wednesday' in data and not(data['end_work_wednesday']):
            data['end_work_wednesday'] = None
        if 'start_work_wednesday' in data and not(data['start_work_wednesday']):
            data['start_work_wednesday'] = None
        if 'end_work_tuesday' in data and not(data['end_work_tuesday']):
            data['end_work_tuesday'] = None
        if 'start_work_tuesday' in data and not(data['start_work_tuesday']):
            data['start_work_tuesday'] = None
        if 'end_work_monday' in data and not(data['end_work_monday']):
            data['end_work_monday'] = None
        if 'start_work_monday' in data and not(data['start_work_monday']):
            data['start_work_monday'] = None

        return super(DataSerializer, self).to_internal_value(data)

    class Meta:
        model = Data
        exclude = ('id',)
        extra_kwargs = {
            'end_work_sunday': {'allow_null': True},
            'start_work_sunday': {'allow_null': True},
            'end_work_saturday': {'allow_null': True},
            'start_work_saturday': {'allow_null': True},
            'end_work_friday': {'allow_null': True},
            'start_work_friday': {'allow_null': True},
            'end_work_thursday': {'allow_null': True},
            'start_work_thursday': {'allow_null': True},
            'end_work_wednesday': {'allow_null': True},
            'start_work_wednesday': {'allow_null': True},
            'end_work_tuesday': {'allow_null': True},
            'start_work_tuesday': {'allow_null': True},
            'end_work_monday': {'allow_null': True},
            'start_work_monday': {'allow_null': True},
        }


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        exclude = ('recivers',)
