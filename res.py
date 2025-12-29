import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from PIL import Image
import os

def compare_images(image_dir, image_number=170):
    """Loads and displays two images side-by-side for comparison."""
    hr_image_path = os.path.join(image_dir, f'hr_epoch_{image_number}.png')
    enhanced_image_path = os.path.join(image_dir, f'enhanced_epoch_{image_number}.png')
    if not (os.path.exists(hr_image_path) and os.path.exists(enhanced_image_path)):
        print(f"Could not find images for epoch: {image_number}")
        return
    try:
        hr_img = Image.open(hr_image_path)
        enhanced_img = Image.open(enhanced_image_path)

    except Exception as e:
        print(f"Error opening images: {e}")
        return

    fig = plt.figure(figsize=(10, 5)) # set figure size
    gs = gridspec.GridSpec(1, 2, width_ratios=[1, 1]) # create a grid for plots
    
    # set the first plot to be the original high resolution image
    ax1 = plt.subplot(gs[0])
    ax1.imshow(hr_img)
    ax1.set_title(f"Original HR Image")
    ax1.axis('off')

    # set the second plot to be the generated enhanced image
    ax2 = plt.subplot(gs[1])
    ax2.imshow(enhanced_img)
    ax2.set_title(f"Enhanced Image")
    ax2.axis('off')

    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    image_dir = 'result_images' # you might have to change this if you saved the images elsewhere
    compare_images(image_dir, image_number=170)