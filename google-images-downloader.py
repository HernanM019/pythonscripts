#Documentation:
#https://google-images-download.readthedocs.io/en/latest/index.html

#example

from google_images_download import google_images_download   #importing the library

response = google_images_download.googleimagesdownload()   #class instantiation

arguments = {"keywords":"Polar bears,baloons,Beaches","limit":100,"print_urls":True}   #creating list of arguments
#arguments = {"keywords":"Jennie blackpink, rose blackpink, blackpink","limit":5,"r:'labeled-for-reuse,""print_urls":True}   #creating list of arguments
paths = response.download(arguments)   #passing the arguments to the function
print(paths)   #printing absolute paths of the downloaded images
