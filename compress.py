from PIL import Image
image=Image.open(BytesIO(image_response.content))
nx,ny=image.size
factor=float(ny/nx)
image.resize((1280,int(1280*factor)),Image.ANTIALIAS)
image.save(os.path.join(BASE_DIR,"static_res/"+servicegroup+"/"+service_slug+"/"+service_id+"/"+image_id),format="JPEG",quality=50)
