import boto3
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
from io import BytesIO

def detect_labels(photo, bucket):
    client = boto3.client('rekognition')

    response = client.detect_labels(
        Image={'S3Object': {'Bucket': bucket, 'Name': photo}},
        MaxLabels=10
    )

    print('Detected labels for ' + photo)
    print()

    # Print label information
    for label in response['Labels']:
        print("Label:", label['Name'])
        print("Confidence:", label['Confidence'])
        print()

    # Load the image from S3
    s3 = boto3.resource('s3')
    obj = s3.Object(bucket, photo)
    img_data = obj.get()['Body'].read()
    img = Image.open(BytesIO(img_data))

    # Display the image
    plt.imshow(img)
    ax = plt.gca()

    # Plot bounding boxes
    for label in response['Labels']:
        for instance in label.get('Instances', []):
            bbox = instance['BoundingBox']
            left = bbox['Left'] * img.width
            top = bbox['Top'] * img.height
            width = bbox['Width'] * img.width
            height = bbox['Height'] * img.height

            rect = patches.Rectangle(
                (left, top),
                width,
                height,
                linewidth=1,
                edgecolor='r',
                facecolor='none'
            )
            ax.add_patch(rect)

            label_text = f"{label['Name']} ({label['Confidence']:.2f}%)"
            text_y = max(top - 5, 0)

            plt.text(
                left,
                text_y,
                label_text,
                color='r',
                fontsize=8,
                bbox=dict(facecolor='white', alpha=0.7)
            )

    plt.axis('off')
    plt.show()

    return len(response['Labels'])

def main():
    photo = '20260129_135915.jpg'
    bucket = 'image-labeller-amazon'
    label_count = detect_labels(photo, bucket)
    print("Labels detected:", label_count)

if __name__ == "__main__":
    main()
