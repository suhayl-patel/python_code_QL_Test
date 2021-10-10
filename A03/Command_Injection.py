@staticmethod
def save_data(file, backup=None):
    data_path = os.path.join(settings.MEDIA_ROOT, "data")
    full_file_name = os.path.join(data_path, file.name)
    # the uploaded file is read at once, as duplicated in railsgoat
    # use file.chunk() in a loop can prevent overwhelming system memory
    content = ContentFile(file.read())
    default_storage.save(full_file_name, content)
    if backup == "true":
        return Benefits.make_backup(file, data_path, full_file_name)

@staticmethod
@silence_streams
def make_backup(file, data_path, full_file_name):
    if os.path.isfile(full_file_name):
        epoch_time = int(time.time())
        bak_file_path = "%s/bak%d_%s" % (data_path, epoch_time, file.name)
        # intended vulnerability for command injection
        os.system("cp %s %s" % (full_file_name, bak_file_path))
        return bak_file_path
