import cv2
import numpy as np

net = cv2.dnn.readNet('yolov3.weights', 'yolov3.cfg')

classes = []

with open('coco.names', 'r') as f:
    classes = f.read().splitlines()

# choice = str(input("Enter object you want to pick : "))
# print(choice)

cap = cv2.VideoCapture("test3.mp4")

while True:
    s, img = cap.read()
    height, width, _ = img.shape

    blob = cv2.dnn.blobFromImage(img, 1 / 255, (416, 416), (0, 0), swapRB=True, crop=False)
    net.setInput(blob)
    output_layer_names = net.getUnconnectedOutLayersNames()  # Get names of layers of network
    layer_outputs = net.forward(output_layer_names)  # To provide output at output layer

    boxes = []
    confidences = []  # how likely the box contains the  object
    class_ids = []
    obj_names=[]

    for output in layer_outputs:

        for detection in output:
            scores = detection[5:]
            # print(scores)
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5:
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)

                w = int(detection[2] * width)
                h = int(detection[3] * height)

                x = int(center_x - w / 2)
                y = int(center_y - h / 2)

                boxes.append([x, y, w, h])
                confidences.append(float(confidence) * 100)
                class_ids.append(class_id)
                # cv2.circle(img,(center_x,center_y),3,(120,120,255),5)


    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

    font = cv2.FONT_HERSHEY_PLAIN
    colors = np.random.uniform(0, 255, size=(len(boxes), 3))

    if (len(indexes)) > 0:
        for i in indexes.flatten():
            x, y, w, h = boxes[i]
            label = str(classes[class_ids[i]])
            confidence = str(round(confidences[i], 2))
            color = colors[i]
            obj_names.append(label)
            cv2.putText(img, label + " " + confidence + "%", (x, y + 20), font, 2, (255, 255, 255), 2)
            cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)


            # if label == choice:
            #     cv2.putText(img, label + " " + confidence + "%", (x, y + 20), font, 2, (255, 255, 255), 2)
            #     cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)

    cv2.imshow("image", img)

    key = cv2.waitKey(1)
    if key == 27:
        break
cap.release()
print(obj_names)
cv2.destroyAllWindows()
