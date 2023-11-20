import base64
import json
from openai import OpenAI
import os

import time

client = OpenAI()

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

dataset_path = ""

with open('./maplm_test.json', 'r') as source_file:
    data = json.load(source_file)

system_prompt = "You are a helpful language and vision assistant for traffic, driving and map scene. " + "You are able to understand the visual content that the user provides, " + "and assist the user with a variety of tasks using natural language to interpret attributes in images or point clouds. " + "You only answer from the options for each question and do not generate any reasoning. If you don't know the answer, just radomly select one."
output = []

with open('maplm_gpt4_output.json', 'r') as source_file:
    output = json.load(source_file)

count = 0
while count < len(data):
    item = data[count]
    img = item["image"]
    if img == output[-1]["image"]:
        count+=1
        break
    else:
        count+=1

while count < len(data):
    item = data[count]
    img = item["image"]
    bev = item["pointcloud"]
    img_path = os.path.join(dataset_path, img)
    bev_path = os.path.join(dataset_path, bev)
    
    encoded_img = encode_image(img_path)
    encoded_bev = encode_image(bev_path)

    response = client.chat.completions.create(
        model="gpt-4-vision-preview",
        messages=[
            {
                "role": "system",
                "content": [
                    {"type": "text", "text": system_prompt},
                ],
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/jpeg;base64,{encoded_img}"},
                    }
                ],
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/jpeg;base64,{encoded_bev}"},
                    }
                ],
            },
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "1. What kind of road scene is it in the images? Your potential choice is: Normal city road. Construction road. Undeveloped road. Road mark repainting. Roundabout. None of the above; 2. What is the point cloud data quality in current road area of this image? Your potential choice is: Very clear. Not clear, road mark is worn. Not clear, road mark is occluded by some vehicle. Not clear, road mark is worn and occluded by vehicle; 3. How many lanes on the current road? Only answer the number; 4. Is there any road cross, intersection or lane change zone in the main road? Your potential choice is: No. Yes, there is one crossroad in the image. Yes, there is one T-junction in the image. Yes, there is a small road intersection in the image. Yes, there is one lane change zone in the image. Yes, there is one irregular intersection in the image."},
                ],
            },
        ],
        max_tokens=4096,
    )
    
    response_output = response.choices[0].message.content
    
    out_item = {
            "image": img,
            "pointcloud": bev,
            "conversations": response_output}
    
    output.append(out_item)
    
    print(response_output)
    
    with open('maplm_gpt4_output.json', 'w') as destination_file:
        json.dump(output, destination_file, indent=4)
    
    count+=1
    
    time.sleep(60)   

with open('maplm_gpt4_output.json', 'w') as destination_file:
    json.dump(output, destination_file, indent=4)
