import streamlit as st
import os
import torch
from torchvision.transforms import transforms
from PIL import Image
from pathlib import Path
import cv2


# this is for saving images and prediction
def save_image(uploaded_file):
    if uploaded_file is not None:
        save_dir = "images"
        os.makedirs(save_dir, exist_ok=True)  # Create directory if it doesn't exist
        save_path = os.path.join(save_dir, "input.jpeg")
        with open(save_path, "wb") as f:
            f.write(uploaded_file.read())
        st.success(f"Image saved to {save_path}")

        model = torch.load(Path('model/model.pt'))


        trans = transforms.Compose([
            transforms.RandomHorizontalFlip(),
            transforms.Resize(224),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            ])

        image = Image.open(Path('images/input.jpeg'))

        # image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


        input = trans(image)

        input = input.view(1, 3, 224, 224).repeat(1, 1, 1, 1)
        # print(input)

        output = model(input)

        prediction = int(torch.max(output.data, 1)[1].numpy())
        print(prediction)

        if (prediction == 0):
            print ('ringworm')
            st.text_area(label="Prediction:", value="ringworm", height=100)
        if (prediction == 1):
            print ('measles')
            st.text_area(label="Prediction:", value="measles", height=100)






if __name__ == "__main__":
    st.title("disease  classifier")
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])
    save_image(uploaded_file)
