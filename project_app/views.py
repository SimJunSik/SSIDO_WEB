from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from django.core import serializers
from datetime import datetime
from django.core.files.storage import FileSystemStorage

# Create your views here.

def index(request) :

	pdfs = PDF.objects.filter(class_id = 'A')

	context = { 'pdfs' : pdfs }

	return render(request, './chat+viewer.html', context)



def cc_test(request) :

	return render(request, './create_class.html')


def joinClass(request) :

	if request.method == 'GET' :

		#print(request.path.split('/')[2])

		class_id = request.path.split('/')[2]

		print(class_id)

		pdfs = PDF.objects.filter(class_id = class_id)

		context = { 'pdfs' : pdfs }

		"""
		classnode = ClassNode.objects.get(class_id = class_id)
		classnode.number_of_user = classnode.number_of_user + 1
		classnode.save()
		"""


		return render(request, './chat+viewer.html', context)

	if request.method == 'POST':
		class_id = request.POST.get('class_id_text', False)

		for pdf in request.FILES.getlist('upload[]'):
			#print(pdf)
			pdf_url = "../media/pdfs/" + "[" + class_id + "]" + pdf.name
			new_pdf = PDF(pdf_name = "[" + class_id + "]" + pdf.name,
				pdf_url = pdf_url, 
				class_id = class_id, 
				pdf = pdf)
			#print(new_pdf)
			new_pdf.save()
			#fs = FileSystemStorage()
			#filename = fs.save(pdf.name, pdf)
			#uploaded_file_url = fs.url(filename)
			#print(uploaded_file_url)

		#print(request.POST.get('class_id_text', False))

		pdfs = PDF.objects.filter(class_id = class_id)

		context = { 'pdfs' : pdfs }

		"""
		file_get = request.POST.get('upload', False)
		if(file_get == False) :
			img_src = request.FILES['upload']
			fs = FileSystemStorage()
			filename = fs.save(img_src.name, img_src)
		"""

		return render(request, './chat+viewer.html', context)




"""
def pdf_upload(request) :

	if request.method == 'POST':
		for f in request.FILES.getlist('upload[]'):
			print(f)

		#print(request.POST.get('class_id_text', False))

		class_id = request.POST.get('class_id_text', False)
		pdfs = PDF.objects.filter(class_id = class_id)

		context = { 'pdfs' : pdfs }

		return render(request, './chat+viewer.html', context)
		#return redirect(request, './chat+viewer.html', context)
"""


def check_class(request) :

	try :
		class_id = request.GET.get('class_id',None)

		classnode = ClassNode.objects.get(class_id = class_id)
		result = { "result" : "success"}

	except :

		result = { "result" : "failed"}


	return JsonResponse(result)







def inputClass(request) :

	return render(request, './input_class.html')



def create_class(request) :

	if request.method == 'GET' :

		class_name = request.GET.get('class_name',None)
		class_code = request.GET.get('class_code',None)
	
		result = { "result" : "success" }

		print(class_name, class_code)

		new_class = ClassNode(class_name = class_name, class_code = class_code)
		new_class.save()

		return JsonResponse(result)

def pdf(request) :

	return render(request, './viewer_test.html')


def updateChat(request) :

	if request.method == 'GET' :

		class_id = request.GET.get('class_id',None)

		json_serializer = serializers.get_serializer("json")()
		chats = json_serializer.serialize(ChatNode.objects.filter(class_id=class_id), ensure_ascii=False)
		#chats = json_serializer.serialize(Chat.objects.all(), ensure_ascii=False)
		#chats = Chat.objects.all()
	
		result = { "chats" : chats }

		#print(result)

		return JsonResponse(result)


def sendChat(request) :

	if request.method == 'GET' :
		now = datetime.now()
		#print(now)

		user_id = request.GET.get('user_id',None)
		user_name = request.GET.get('user_name',None)
		chat_content = request.GET.get('chat_content',None)
		class_id = request.GET.get('class_id',None)

		#print(chat_content)

		new_chat = ChatNode(user_id = user_id, user_name = user_name, content = chat_content, class_id = class_id)
		new_chat.save()
	
		result = { "result" : 'false' }

		return JsonResponse(result)


def ddabong(request) :

	if request.method == 'GET' :

		user_name = request.GET.get('user_name',None)
		content = request.GET.get('content',None)
		class_id = request.GET.get('class_id',None)
		date = request.GET.get('date',None)

		print(user_name, content, class_id, date)

		chat = ChatNode.objects.get(user_name = user_name, content = content, class_id=class_id, created_date = date)
		#print(chat.ddabong)
		chat.ddabong = chat.ddabong + 1
		chat.save()
	
		result = { "result" : 'false' }

		return JsonResponse(result)


def delete_msg(request) :

	if request.method == 'GET' :

		user_name = request.GET.get('user_name',None)
		content = request.GET.get('content',None)
		class_id = request.GET.get('class_id',None)
		date = request.GET.get('date',None)

		print(user_name, content, class_id, date)

		chat = ChatNode.objects.get(user_name = user_name, content = content, class_id=class_id, created_date = date)
		#print(chat.ddabong)
		#chat.ddabong = chat.ddabong + 1
		chat.delete()
	
		result = { "result" : 'false' }

		return JsonResponse(result)