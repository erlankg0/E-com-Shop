# MEDIA
# media/brand_mango/some image.jpg
def brand_name_directory_path(instance, filename):
    return "brands/brand_{0}/{1}".format(instance.name.lower(), filename)
