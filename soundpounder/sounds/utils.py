# from django's docs


def handle_uploaded_file(f):
    ext = os.path.splitext(f.name)[1]
    destination = open('some/file/name%s'%(ext), 'wb+')
    for chunk in f.chunks():
        destination.write(chunk)
    destination.close()