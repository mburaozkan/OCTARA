import numpy as np
import matplotlib.pyplot as plt


def octara_ratio(image1, image2):
    numerator = np.minimum(image1, image2)
    denominator = np.maximum(image1, image2)
    return 1.0 - np.mean(numerator / denominator)

def compute_octa_image(images):
    num_combinations = len(images)
    octa_image = np.zeros_like(images[0], dtype=np.float32)

    for i in range(num_combinations - 1):
        for j in range(i + 1, num_combinations):
            octa_image += octara_ratio(images[i], images[j])

    octa_image /= (num_combinations * (num_combinations - 1) / 2)

    return octa_image

# every 4 slice b-scan = octa scan

def compute_octa(images):
    octa_images = []
    for location_images in images:
        print(location_images)
        octa_images.append(compute_octa_image(location_images))

    return octa_images

from oct_converter.readers import FDA

# Sample usage
if __name__ == "__main__":
    # Assuming you have a list of 2D numpy arrays for each location
    # Replace this with your actual OCT intensity images data
    
    filepath = "./192784.fda"
    fda = FDA(filepath)

    oct_volume = fda.read_oct_volume()

    oct_intensity_images = oct_volume.volume
    # [
    #     np.random.rand(512, 512),
    #     np.random.rand(512, 512),
    #     # Add more intensity images here for other scan locations
    # ]

    octa_images = compute_octa(oct_intensity_images)

    # Visualize one of the OCTA images (e.g., the first one)
    plt.imshow(octa_images, cmap='gray')
    plt.title('OCTA Image')
    plt.axis('off')
    plt.show()
