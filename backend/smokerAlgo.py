import time
import cv2
import mediapipe as mp
import numpy as np
from ultralytics import YOLO
import threading
import math
import os
from  text_analysis import text_analysis

import os

# Get the directory of the current Python script
script_dir = os.path.dirname(os.path.realpath(__file__))

# Construct the absolute path of the file

def normalize_distance(distance, face_size, image_width, image_height):
    # Normalize the distance with respect to the face size
    if(distance<=0):
        return 1
    else:
        distance_normalized_to_face = distance / face_size

        # Calculate the diagonal of the image
        image_diagonal = math.sqrt(image_width**2 + image_height**2)

        # Normalize the distance with respect to the image size
        distance_normalized_to_image = distance_normalized_to_face / image_diagonal
    return 1-distance_normalized_to_image

def calculate_distance(coord1, coord2):
    return math.sqrt((coord2[0] - coord1[0])**2 + (coord2[1] - coord1[1])**2)


def cigarette(picture):
    file_path = os.path.join(script_dir, 'models', 'best.pt')
    model = YOLO(file_path)
    results = model.predict(picture)
    result = results[0]
    answer=[]
    for box in result.boxes:
        class_id = result.names[box.cls[0].item()]
        cords = box.xyxy[0].tolist()
        cords = [round(x) for x in cords]
        conf = round(box.conf[0].item(), 2)
        conf = math.ceil(conf * 10) / 10  
        # If the detected object is a cigarette, draw a rectangle around it
        if class_id == 'cigarette':
            start_point = (cords[0], cords[1])
            end_point = (cords[2], cords[3])

            # Calculate the middle point of the rectangle
            middle_point = ((start_point[0] + end_point[0]) // 2, (start_point[1] + end_point[1]) // 2)
            
            # Calculate the radius of the circle
            radius = int(np.sqrt((end_point[0] - start_point[0])**2 + (end_point[1] - start_point[1])**2) / 2)
            temp=[middle_point, radius, conf]
            answer.append(temp)
    return answer


def hand(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(static_image_mode=True, max_num_hands=10)
    results = hands.process(image)
    result=[]
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            avg_x = np.mean([landmark.x for landmark in hand_landmarks.landmark])
            avg_y = np.mean([landmark.y for landmark in hand_landmarks.landmark])
            height, width, _ = image.shape
            avg_x_pixel = int(avg_x * width)
            avg_y_pixel = int(avg_y * height)
            # Calculate the maximum distance from the average point to all other points.
            max_distance = max(np.sqrt((landmark.x - avg_x)**2 + (landmark.y - avg_y)**2) for landmark in hand_landmarks.landmark)*0.8
            
            max_distance_pixel = int(max_distance * max(width, height))
            middle_point=(avg_x_pixel,avg_y_pixel)
            tempList=[middle_point, max_distance_pixel,1]
            result.append(tempList)
            # Draw a circle at the average coordinates with the calculated radius.
    return result


def face(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    mp_face_detection = mp.solutions.face_detection
    face_detection = mp_face_detection.FaceDetection(model_selection=0)
    results = face_detection.process(image)
    result=[]
    if results.detections:
        for detection in results.detections:
            #print("Confidence level: ", detection.score[0])
            bboxC = detection.location_data.relative_bounding_box
            ih, iw, _ = image.shape
            bbox = int(bboxC.xmin * iw), int(bboxC.ymin * ih), \
                int(bboxC.width * iw), int(bboxC.height * ih)
            # Draw a rectangle around the face
            start_point = (bbox[0], bbox[1])
            end_point = (bbox[0] + bbox[2], bbox[1] + bbox[3])
            middle_point = ((start_point[0] + end_point[0]) // 2, (start_point[1] + end_point[1]) // 2)
            #print(middle_point)
            radius = int((np.sqrt((end_point[0] - start_point[0])**2 + (end_point[1] - start_point[1])**2) / 2)*0.7)
            #print(radius)
            tempList=[middle_point, radius,detection.score[0]]
            result.append(tempList)
    return result

def extract_frames(i, video_path, output_folder):
    video_capture = cv2.VideoCapture(video_path)
    extracted_frames = []
    temp = []
    counterTemp = 0
    counterMaxTemp = 0

    index = 0
    while video_capture.isOpened():
        exists, extracted_frame = video_capture.read()
        if not exists:
            break

        if index % 12 == 0:
            frame_path = os.path.join(output_folder,"post{0}_frame{1}.jpg".format(i, index))
            cv2.imwrite(frame_path, extracted_frame)
            extracted_frames.append(frame_path)
            imageName = "./{0}/post{1}_frame{2}.jpg".format(output_folder,i,index)
            img = cv2.imread(imageName)
            temp, counterTemp, counterMaxTemp = analyseFunction(imageName, img, counterTemp, counterMaxTemp, temp)
        index += 1
    video_capture.release()
    
    temp = sorted(temp, key=lambda x: x[0], reverse=True)
    chosenFrame = temp[0][-1]
    return chosenFrame

def analyseFunction(imageName, img, counter, counterMax, finalResult):
    height, width, _ = img.shape
    faceRes=face(img)
    cigaretteRes=cigarette(imageName)
    handRes=hand(img)
    catalogue=[]

    if(len(cigaretteRes)==0):
        catalogue.append([0,0,imageName])
    else:
        wentIn=False
        for i in range(len(cigaretteRes)):
            cigConfidence=cigaretteRes[i][2]
            for j in range(len(faceRes)):
                distance=calculate_distance(cigaretteRes[i][0],faceRes[j][0])-cigaretteRes[i][1]-faceRes[j][1]
                normalization=normalize_distance(distance,cigaretteRes[i][2],height,width)
                if cigConfidence < 0.8:
                    cigConfidence+=0.2
                faceConfidence=faceRes[j][2]
                res=normalization*cigConfidence*faceConfidence
                res = math.ceil(res * 10) / 10
                temp=[res,cigaretteRes[i][0],cigaretteRes[i][1],faceRes[j][0],faceRes[j][1],1,imageName]
                catalogue.append(temp)
                wentIn=True
                
            for j in range(len(handRes)):
                distance=calculate_distance(cigaretteRes[i][0],handRes[j][0])-cigaretteRes[i][1]-handRes[j][1]
                normalization=normalize_distance(distance,cigaretteRes[i][2],height,width)
                if cigConfidence < 0.8:
                    cigConfidence+=0.2
                res=normalization*cigConfidence
                res = math.ceil(res * 10) / 10
                temp=[res,cigaretteRes[i][0],cigaretteRes[i][1],handRes[j][0],handRes[j][1],2,imageName]
                catalogue.append(temp)
                wentIn=True
            if(wentIn==False):
                temp=[1*cigaretteRes[i][2],cigaretteRes[i][0],cigaretteRes[i][1],3,imageName]
                catalogue.append(temp)
    catalogue = sorted(catalogue, key=lambda x: x[0], reverse=True)
    if(catalogue[0][len(catalogue[0])-2]==0):
        counter+=0
        counterMax+=1
    elif(catalogue[0][len(catalogue[0])-2]==1 or catalogue[0][len(catalogue[0])-2]==2):
        counter+=(10*catalogue[0][0])
        counterMax+=10
    else:
        counter+=(7*catalogue[0][0])
        counterMax+=7
 
    finalResult.append(catalogue[0])
    return finalResult, counter, counterMax


def smokerALgo(input):
    finalResult=[]
    #confidence, type0=face type=1
    counter=0
    counterMax=0    
    jpgCount = 0
    mp4Count = 0 
    
    for file_name in os.listdir(input):
       if file_name.lower().endswith(".jpg"):
           jpgCount += 1
       elif file_name.lower().endswith(".mp4"):
           mp4Count += 1
           
    anaylsisCount = jpgCount + mp4Count
      
    for i in range(0, anaylsisCount):
        file_path = "./{0}/post{1}.mp4".format(input,i)
        if os.path.exists(file_path):
            chosenFrame = extract_frames(i, file_path, input)
            img = cv2.imread(chosenFrame)
            finalResult, counter, counterMax = analyseFunction(chosenFrame, img, counter, counterMax, finalResult)
            continue

        imageName="./{0}/post{1}.jpg".format(input,i)
        try:
            img = cv2.imread(imageName)
            if img is None:
                raise FileNotFoundError(f"No such file or directory: '{imageName}'")
            finalResult, counter, counterMax = analyseFunction(imageName, img, counter, counterMax, finalResult)
        except FileNotFoundError as e:
            print(f"File not found: {e}")
            continue

    text_analysis_results = text_analysis(input)

    smoking_posts_sorted = text_analysis_results[2]

    avg_sent = text_analysis_results[1]
    ratio_of_smoking_posts = text_analysis_results[0]
    posts_score = avg_sent*ratio_of_smoking_posts

    finalResult = sorted(finalResult, key=lambda x: x[0], reverse=True)
    res=counter/counterMax
    smoking_score = (res+posts_score)/2
    #rounding
    smoking_score = math.ceil(smoking_score * 10) / 10
    return [finalResult,smoking_score,posts_score,smoking_posts_sorted]
if __name__ == "__main__":
    start_time = time.time()
    print(smokerALgo())
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"The script executed in {execution_time} seconds")
