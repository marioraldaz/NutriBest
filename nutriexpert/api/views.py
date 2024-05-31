from ..models import Message
from ..Service.Chat import Chat
from rest_framework.views import APIView
from django.http import JsonResponse



class MessageView(APIView):

    def post(self, request):
        data = request.data
        user_input = data.get("user_input")
        previous = data.get("previous")
        if(user_input == ''):
            return JsonResponse({"message":"Please provide text"}, status=500)
        
        try:
            # Instantiate DatabaseChat
            chat = DatabaseChat()
            # Generate response
            response = chat.run(user_input, previous)

            # Save user input and response as a Message object
            message = Message.objects.create( input_text=user_input, response_text=response)
            
            return JsonResponse({'message': response})
        
        except Exception as e:
            print(e)
            # Handle exceptions such as database errors or chat generation issues
            return JsonResponse({'message': str(e)}, status=500)