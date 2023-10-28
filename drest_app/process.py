def process_uploaded_file(file_instance):
    file_instance.processed = True
    file_instance.save()
