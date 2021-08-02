# Fake-News-Detection-System

![image](https://user-images.githubusercontent.com/66703039/127868827-4d4e34ef-b8b3-431d-9498-cb316ba8dfb9.png)
![image](https://user-images.githubusercontent.com/66703039/127868752-60e960eb-1690-4331-bc42-f3dc78906127.png)


The main goal of the project is to analyse news article and determine if it is reliable or not.

## Necessity

In these uncertain times, correct and timely information is very necessary for us to beat the pandemic. Fake news creates a panic amongst people and it is so dangerous that it has even caused riots in past. \
Thus, the effect of fake news has been growing, sometimes extending to the offline world and threatening public safety. \
Hence it is very important for us to build a system which can help people filter out the authentic news from the fake one.

## Approach

* Random Forest Classifier
    - Accuracy: 89.89%
    - F1 Score: 89.77%
* Support Vector Machine
    - Accuracy: 96.08%
    - F1 Score: 96.03%
* Passive Aggressive Classifier
    - Accuracy: 96.41%
    - F1 Score: 96.36%

After comparing different models, we concluded that Passive Aggressive Classifer works better than others.

## Deployment

Here is the [Live Deployment](https://share.streamlit.io/alooperalta/fake-news-detection-system/main/fakenews_detection.py)
