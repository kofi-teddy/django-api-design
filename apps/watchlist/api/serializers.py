from apps.watchlist.models import StreamPlatform, WatchList
from rest_framework import serializers


class WatchListSerializer(serializers.ModelSerializer):

    class Meta:
        model = WatchList
        fields = '__all__'


class StreamPlatformSerializer(serializers.ModelSerializer):
    watchlist = WatchListSerializer(many=True, read_only=True)
    class Meta:
        model = StreamPlatform
        fields = '__all__'
    


# def name_length(value):
#     if len(value) < 2:
#         raise serializers.ValidationError('Name is too short!')    


# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_length])
#     description = serializers.CharField()
#     active = serializers.BooleanField()

#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance

#     def validate(self, data):
#         '''
#         Check if Name and Description have different values
#         '''
#         if data['name'] == data['description']:
#             raise serializers.ValidationError('Name and Description should be different')
#         return data

    # def validate_name(self, value):
    #     '''
    #     Check if Name not equal to 2 values
    #     '''
    #     if len(value) < 2:
    #         raise serializers.ValidationError('Name is too short!')
    #     else:
    #         return value
