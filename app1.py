import streamlit as st
import os
import torch
from torchvision.transforms import transforms
from PIL import Image
from pathlib import Path


# this is for saving images and prediction
def save_image(uploaded_file):
    if uploaded_file is not None:
        save_dir = "images"
        os.makedirs(save_dir, exist_ok=True)
        save_path = os.path.join(save_dir, "input.jpeg")
        with open(save_path, "wb") as f:
            f.write(uploaded_file.read())
        st.success(f"Image saved to {save_path}")

        model = torch.load(Path('model/model.pt'))

        trans = transforms.Compose([
            transforms.Resize((224, 224)),  # Resize the image to (224, 224)
            transforms.ToTensor(),
        ])

        image = Image.open(save_path)
        input = trans(image).unsqueeze(0)  # Add batch dimension

        output = model(input)

        prediction = int(torch.max(output.data, 1)[1].numpy())
        print(prediction)

        if prediction == 0:
            print('ringworm')
            st.text_area(label="Prediction:", value="ringworm", height=100)
        elif prediction == 1:
            print('measles')
            st.text_area(label="Prediction:", value="measles", height=100)







if __name__ == "__main__":
    st.title("Xray lung classifier")
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])
    save_image(uploaded_file)