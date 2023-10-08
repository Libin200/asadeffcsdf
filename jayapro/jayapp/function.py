def file_upload(h):
    with open('jayapp/static/upload/'+h.name,'wb+') as destination:
        for c in h.chunks():
            destination.write(c)