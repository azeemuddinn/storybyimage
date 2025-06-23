from django.shortcuts import render

from .caption_generator import generate_caption
from .forms import ImageUploadForm
from .models import ImageUpload
from .story_generator import generate_story  

def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        mood = request.POST.get("mood", "")

        if form.is_valid():
            image_obj = form.save()
            image_path = image_obj.image.path

            # Generate description
            caption = generate_caption(image_path)
            image_obj.description = caption

            # Generate story
            story = generate_story(caption, mood)
            image_obj.save()

            return render(request, 'core/result.html', {
                'image': image_obj,
                'story': story,
                'mood': mood,
            })
    else:
        form = ImageUploadForm()
    return render(request, 'core/upload.html', {'form': form})
