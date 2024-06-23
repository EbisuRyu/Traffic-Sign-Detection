import os
import cv2
import glob
import time
import numpy as np
import xml.etree.ElementTree as ET

def load_traffic_signboard_dataset():
    dataset_dir = './dataset/traffic_sign_board'
    image_dir = os.path.join(dataset_dir, 'images')
    annotation_dir = os.path.join(dataset_dir, 'annotations')
    # Read the dataset
    image_list = []
    label_list = []
    for annotation_file in os.listdir(annotation_dir):
        file_path = os.path.join(annotation_dir, annotation_file)
        tree = ET.parse(file_path)
        root = tree.getroot()
        
        image_file = root.find('filename').text
        image_path = os.path.join(image_dir, image_file)
        img = cv2.imread(image_path)
        
        for object in root.findall('object'):
            label = object.find('name').text
            if label == 'trafficlight':
                continue
            xmin = int(object.find('bndbox/xmin').text)
            ymin = int(object.find('bndbox/ymin').text)
            xmax = int(object.find('bndbox/xmax').text)
            ymax = int(object.find('bndbox/ymax').text)
            
            image_list.append(img[ymin:ymax, xmin:xmax])
            label_list.append(label)
    print('Number of objects: ', len(image_list))
    print('Classes: ', list(set(label_list)))
    return image_list, label_list


def load_traffic_signboard_dataset_test():
    dataset_dir = './dataset/traffic_sign_board'
    image_dir = os.path.join(dataset_dir, 'images')
    annotation_dir = os.path.join(dataset_dir, 'annotations')
    # Read the dataset
    image_list = []
    label_list = []
    bounding_boxes = []
    for annotation_file in os.listdir(annotation_dir):
        file_path = os.path.join(annotation_dir, annotation_file)
        tree = ET.parse(file_path)
        root = tree.getroot()
        
        image_file = root.find('filename').text
        image_path = os.path.join(image_dir, image_file)
        img = cv2.imread(image_path)
        image_label = []
        bounding_box = []
        for object in root.findall('object'):
            label = object.find('name').text
            if label == 'trafficlight':
                continue
            xmin = int(object.find('bndbox/xmin').text)
            ymin = int(object.find('bndbox/ymin').text)
            xmax = int(object.find('bndbox/xmax').text)
            ymax = int(object.find('bndbox/ymax').text)
            bounding_box.append([xmin, ymin, xmax, ymax])
            image_label.append(label)
        if label != 'trafficlight':
            image_list.append(img)
            label_list.append(image_label)
            bounding_boxes.append(bounding_box)
    return image_list, label_list, bounding_boxes


def crop_object(img, bbox):
    xmin, ymin, xmax, ymax = bbox
    object_img = img[xmin:xmax, ymin:ymax]
    return object_img