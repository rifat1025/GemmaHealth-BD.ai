from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView



class chat_view(APIView):
    def post(self, request):
        message = request.data.get("message", "").lower()

        if not message:
            return Response({"reply": "Please write something."})

        # Simple health intelligence (rule-based system)

        if "fever" in message or "জ্বর" in message:
            reply = "আপনার জ্বর হলে বেশি পানি পান করুন, বিশ্রাম নিন এবং প্রয়োজন হলে প্যারাসিটামল নিতে পারেন।"

        elif "headache" in message or "মাথা ব্যথা" in message:
            reply = "মাথা ব্যথা হলে পানি পান করুন, বিশ্রাম নিন এবং অতিরিক্ত স্ক্রিন টাইম কমান।"

        elif "back pain" in message or "পিঠ ব্যথা" in message:
            reply = "পিঠ ব্যথার জন্য সঠিক ভঙ্গিতে বসুন এবং হালকা স্ট্রেচিং করুন।"

        else:
            reply = "আমি আপনার সমস্যাটি বুঝতে চেষ্টা করছি। দয়া করে একটু বিস্তারিত বলুন।"

        return Response({"reply": reply})


