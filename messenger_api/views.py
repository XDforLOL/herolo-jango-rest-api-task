import arrow
from django.db.models import Q
from rest_framework import generics, status
from rest_framework.response import Response

from abra_restapi_messenger.mixins import StaffEditorPermissionMixin, UserQuerySetMixin
from .models import Message
from .serializers import MessageSerializer


class MessageCreateAPIView(
    UserQuerySetMixin,
    StaffEditorPermissionMixin,
    generics.ListCreateAPIView
):
    serializer_class = MessageSerializer

    def perform_create(self, serializer):
        recipient = serializer.validated_data.get('recipient')
        body = serializer.validated_data.get('body')
        subject = serializer.validated_data.get('subject')

        serializer.save(
            sent_by=self.request.user,
            recipient=recipient,
            body=body, subject=subject,
            creation_date=arrow.utcnow().format('YYYY-MM-DD HH:mm:ss')
        )

    def get_queryset(self):
        return Message.objects.filter(
            Q(recipient__id=self.request.user.id) | Q(sent_by__id=self.request.user.id)
        )


create_message_view = MessageCreateAPIView.as_view()


class ListAllMessagesAPIView(
    UserQuerySetMixin,
    StaffEditorPermissionMixin,
    generics.ListAPIView
):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()


list_all_messages_view = ListAllMessagesAPIView.as_view()


class ListUnreadMessagesAPIView(
    UserQuerySetMixin,
    StaffEditorPermissionMixin,
    generics.ListAPIView
):
    serializer_class = MessageSerializer

    def get_queryset(self):
        queryset = Message.objects.filter(read=False)
        return queryset


unread_list_messages_view = ListUnreadMessagesAPIView.as_view()


class ReadMessageAPIView(
    generics.RetrieveAPIView,
    generics.UpdateAPIView,
    UserQuerySetMixin,
    StaffEditorPermissionMixin,
):

    def get_queryset(self):
        queryset = Message.objects.all()
        return queryset

    serializer_class = MessageSerializer
    lookup_field = 'pk'

    def retrieve(self, request, *args, **kwargs):
        if self.get_queryset().exists():
            content = self.get_object()
            content.read = True
            content.save()
            serializer = self.get_serializer(content)
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.read:
            instance.read = True


read_message_view = ReadMessageAPIView.as_view()


class MessageDestroyAPIView(
    UserQuerySetMixin,
    StaffEditorPermissionMixin,
    generics.RetrieveUpdateDestroyAPIView
):
    def get_queryset(self):
        queryset = Message.objects.all()
        return queryset
    serializer_class = MessageSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        super().perform_destroy(instance)


message_delete_view = MessageDestroyAPIView.as_view()
