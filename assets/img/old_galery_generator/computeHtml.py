import os

subPath = "images/progressGallery/"

for file in os.listdir("."):
    if ".jpg" in file or ".JPG" in file:
        print("""
                    <div>
                    	<div class="image fit flush">
                    		<a href='"""+subPath+file+"""'><img src='"""+subPath+file+"""' alt="" /></a>
                    	</div>
                    </div>
        """);
