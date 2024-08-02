# Dog Breeds
This project uses AI classification, to try to determine the dog breed of a dog in an image. It has the 11 most popular dog breeds. You use a picture of a dog, then the AI will tell you what breed it thinks it is, along with how sure it is. This can be useful to owners of strays, to figure out what breed their dog is. They can use this information to find out more about their dog's expected size, health risks, personality traits, and more.

<img width="509" alt="Screenshot 2024-08-02 at 12 49 06 PM" src="https://github.com/user-attachments/assets/23340ff7-867f-4743-a175-316abd8e9d20">
<img width="798" alt="Screenshot 2024-08-02 at 12 49 00 PM" src="https://github.com/user-attachments/assets/4999b9ce-5580-4415-97bd-e006c23da3fb">
The AI believes the dog is a beagle, and it is 25.5% sure, meaning it thinks theres a 1/4 chance it is right.

## The Algorithm

This project uses transfer learning. This basically uses an already trained model, and re-trains it for a specific dataset. How the training works is the model learns through errors in its predictions, and increases its accuracy as it learns. Through doing this, as it trains, it gets better at recognizing different dog breeds. To run it, it takes a sample image given, and determines what dog breed it thinks it is, along with how accurate it thinks it's prediction is. 

## Running this project

1. First download this file https://drive.google.com/file/d/1ftl7Drk55dsXf6aJ7OhHMiTpBShKcgr1/view?usp=drive_link
2. Go to your drive.google.com and upload the file downloaded (Images.zip)
3. Visit this: https://colab.research.google.com/drive/1_7BYxN2YPOPBSq5n6RcIchLFSPZFiy1E?usp=sharing
4. You can run cell blocks by clicking the underlined button <img width="719" alt="Screenshot 2024-08-01 at 3 26 20 PM" src="https://github.com/user-attachments/assets/194e0868-3628-4e68-9459-c178baf0b9e5">
5. Run the first 5 cells this way
6. It will ask you for permission, give it permission to your google drive
7. The next cell block will train the model.
5.<img width="719" alt="Screenshot 2024-08-01 at 3 26 20 PM" src="https://github.com/user-attachments/assets/8cf407f6-0f0f-4da2-add6-9e512830fd37">
8. The underlined number controls how long it runs. The larger the number, the longer it takes. A larger number will also increase the accuracy of the model. You may modify this as you prefer, but it is not reccomended to increase it too large, as the model won't gain much extra accuracy at very high numbers.
9. Once the training is done, run the next 3 blocks
10. On the left of your screen click on the folder icon
11. Click on the "pytoch classification folder", then under that the "models folder"
12. <img width="1470" alt="Screenshot 2024-08-02 at 12 19 18 PM" src="https://github.com/user-attachments/assets/9ed103b0-aff2-4681-83f1-3bafe6ceaddb">
13. Download the resnet18.onnx, by right clicking on it, then clicking download
14. Do the same thing on the labels.txt to download it
15. Open VS code, and make a folder
16. Label it "Dog Classification", or anything else you want
17. <img width="1470" alt="Screenshot 2024-08-02 at 12 19 18 PM" src="https://github.com/user-attachments/assets/ae47822e-e8ae-4a0b-8992-2e3b1c83716e">
18. Go to your finder, and find the resnet18 you downloaded, as well as the labels.txt
20. Drag and drop the two files into the folder you created 
21. Now create a new file inside that folder by right clicking on the folder name-new file. Label it something that makes sense. This is where the code to run it will go
22. Paste this code inside the new file created: https://docs.google.com/document/d/1TaTkfUd3BuNPbMordSEvcTEgpwrOogCkp6z1_k2JJao/edit?usp=sharing
23. Now go into your macbook terminal
24. Now cd into your folder-do so by typing in cd (your folder name)
25. If your folder is in another folder, you will need to cd into that first.
26. Now to select an image of a dog, drag and drop a dog picture into the folder (the same way you dragged and dropped the labels.txt and resnet18 into the folder)
27. Rename the image to something that makes sense (eg dog_picture.jpg)
28. Make sure your still the in the correct directory, and run the command python3 (the filename where you code is) (the filename of the dog picture) for example python3 my_code.py dog_picture.jpg
29. This will run the program, and the AI will tell you in the terminal what breed it thinks the dog is, along with how sure it is
30. https://drive.google.com/file/d/1ky4nMr2Cr9EF-QLFWNx_M90sjnaai7ea/view?usp=sharing)


