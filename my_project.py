#!/usr/bin/python3
import jetson_inference
import jetson_utils
import argparse
#recogninzing and loading models+argparse parses the command line

#parses the image file and selects a network, parses=decipher
#defines expected command line arguement and parses them when script runs
parser=argparse.ArgumentParser()
#filename that is passed into command line
parser.add_argument("filename", type = str, help = "filename of the image to proceed")
#adds network going to be used
parser.add_argument("--network", type=str, default="googlenet", help = "model to use where googlenet is the default")
#takes in arguements from command line and convert them into object we named opt
opt = parser.parse_args()

#loads image from disk
img = jetson_utils.loadImage(opt.filename)

#load recognition network from command line
net = jetson_inference.imageNet(model="resnet18.onnx", labels="labels.txt", input_blob="input_0", output_blob="output_0")

#class_idx -> reresents the index of the predicted class
#confidence is how sure the model is that it is predicting correctly
class_idx, confidence=net.Classify(img)

class_desc=net.GetClassDesc(class_idx)

print("image is recognized as "+str(class_desc)+" (class# + "+str(class_idx)+") with "+str(confidence*100)+"%")