import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from dotenv import load_dotenv

load_dotenv()

project_path = os.getenv('PROJECT_PATH')


class Result:
    def __init__(self, path: str):
        self.path = path
        # imread RGB
        self.image = cv2.cvtColor(cv2.imread(f'{project_path}{path}'), cv2.COLOR_BGR2RGB)
        self.temp_image = cv2.cvtColor(cv2.imread(f'{project_path}/media/files/template'
                                                  '.jpg'), cv2.COLOR_BGR2RGB)

    def kernel(self, size):
        return np.ones((size, size), np.uint8)

    def getThreshold(self, image):
        """
        Threshold the image.
        """
        # Adaptive thresholding
        mask = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 99, 7)
        return mask

    def alignImages(self):
        img1 = self.image
        img2 = self.temp_image

        # Initiate SIFT detector
        sift = cv2.SIFT_create()

        keypoints1, descriptors1 = sift.detectAndCompute(img1, None)
        keypoints2, descriptors2 = sift.detectAndCompute(img2, None)

        FLANN_INDEX_KDTREE = 1
        index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
        search_params = dict(checks=100)

        flann = cv2.FlannBasedMatcher(index_params, search_params)

        matches = flann.knnMatch(descriptors1, descriptors2, k=2)

        good = []
        for m, n in matches:
            if m.distance < 0.7 * n.distance:
                good.append(m)

        # Extract location of good matches
        points1 = np.zeros((len(good), 2), dtype=np.float32)
        points2 = np.zeros((len(good), 2), dtype=np.float32)

        for i, match in enumerate(good):
            points1[i, :] = keypoints1[match.queryIdx].pt
            points2[i, :] = keypoints2[match.trainIdx].pt

        # Find homography
        h, mask = cv2.findHomography(points1, points2, cv2.RANSAC)

        # Use homography
        height, width, channels = img2.shape
        im1Reg = cv2.warpPerspective(img1, h, (width, height))
        return im1Reg, h

    def cropImage(self, img):
        """
        Crop the image into 3 parts.
        """
        h = 762
        w = 102
        img1 = img[595:581 + h, 121:121 + w]
        img2 = img[595:581 + h, 350:350 + w]
        img3 = img[595:581 + h, 585:585 + w]

        img1 = cv2.cvtColor(img1, cv2.COLOR_RGB2GRAY)
        img2 = cv2.cvtColor(img2, cv2.COLOR_RGB2GRAY)
        img3 = cv2.cvtColor(img3, cv2.COLOR_RGB2GRAY)

        return img1, img2, img3

    def cropImage2(self, img):
        # id,767,561,154,250,img.jpg,1241,1754
        # id,995,563,179,256,img.jpg,1241,1754
        img1 = img[561:561 + 250, 767:767 + 154]
        img2 = img[563:563 + 256, 995:995 + 179]
        # rgb to gray
        img1 = cv2.cvtColor(img1, cv2.COLOR_RGB2GRAY)
        img2 = cv2.cvtColor(img2, cv2.COLOR_RGB2GRAY)
        return img1, img2

    def getPersonId(self, thresh_image, i):

        if i == 0:
            # Check langage point
            languages = []
            options = {0: "ingliz", 1: "nemis", 2: "fransuz"}
            x_point = [23, 74, 124]
            y_point = 18

            for lanId, x in enumerate(x_point):
                r = thresh_image[y_point - 5:y_point + 5, x - 5:x + 5]
                b = np.sum(r == 0)
                ans_dict = {
                    "option": options[lanId],
                    "score": int(b),
                }
                languages.append(ans_dict)

            languages = list(filter(lambda x: x['score'] >= 75, languages))

            if len(languages) == 1:
                language = {"language": languages[0]['option']}
            else:
                language = {"language": "error"}
            return language

        else:
            numbers = []
            x_point = [11, 40, 64, 88, 113, 138, 163]
            y_point = [15, 40, 66, 91, 117, 141, 167, 192, 217, 241]

            options = {0: "1", 1: "2", 2: "3", 3: "4", 4: "5", 5: "6", 6: "7", 7: "8", 8: "9", 9: "0"}
            img = cv2.cvtColor(thresh_image, cv2.COLOR_GRAY2RGB)

            for x in x_point:
                ans = []
                for numId, y in enumerate(y_point):
                    r = thresh_image[y - 5:y + 5, x - 5:x + 5]
                    b = np.sum(r == 0)

                    ans_dict = {
                        "option": options[numId],
                        "score": int(b),
                    }

                    ans.append(ans_dict)
                numbers.append(ans)

            option_numbers = {}
            number = []
            for option in numbers:
                op_filter = list(filter(lambda x: x['score'] >= 75, option))

                if len(op_filter) == 1:
                    number.append(op_filter[0]['option'])
                else:
                    number.append('error')
            return number

    def getIdentify(self):
        image, h = self.alignImages()
        imgs = self.cropImage2(image)
        thresh_iamges = [self.getThreshold(img) for img in imgs]

        language, numId = [self.getPersonId(img, i) for i, img in enumerate(thresh_iamges)]
        return language, numId

    def getAllResults(self, thresh_images, i):

        y_points = [15, 41, 65, 91, 116, 142, 167, 191, 217, 242, 263, 284, 308, 332, 357, 381, 407, 432, 457, 484, 509,
                    534, 560, 585, 610, 636, 660, 686, 711, 736]
        if i == 1:
            y_points = [14, 39, 64, 90, 115, 140, 165, 190, 216, 240, 262, 282, 306, 330, 355, 378, 404, 428, 453, 480,
                        505, 530, 556, 581, 607, 632, 658, 683, 709, 734]
        options = {1: "A", 2: "B", 3: "C", 4: "D"}

        x_points = [13, 38, 63, 89]  # x points +10 or -10

        result = []
        for idx, y in enumerate(y_points, 1):
            answer = []
            for i, x in enumerate(x_points, 1):
                r = thresh_images[y - 5:y + 5, x - 5:x + 5]
                b = np.sum(r == 0)
                # if b > 50:
                ans_dict = {
                    "option": options[i],
                    "score": int(b),
                }
                answer.append(ans_dict)
            result.append(answer)

        return result

    def get_option(self, data):
        results = {}

        for n, optons in data.items():
            # filter score > 60
            option = list(filter(lambda x: x['score'] >= 75, optons))

            if len(option) == 0:
                results[n] = "error"
            elif len(option) == 1 and option[0]['score'] < 90:
                results[n] = "error"
            elif len(option) == 1 and option[0]['score'] >= 90:
                results[n] = option[0]['option']
            elif len(option) > 1:
                results[n] = "error"
            else:
                results[n] = option[0]['option']

        formatted_results = [{str(k): v} for k, v in results.items()]
        return formatted_results

    def result(self):
        """
        Get the result of the image.
        """
        # align image
        image, h = self.alignImages()
        # Save the aligned image
        # aligned_image_filename = "aligned_image.jpg"  # Change the filename as needed
        # cv2.imwrite(aligned_image_filename, image)

        # crop image
        crop_images = self.cropImage(image)
        # threshold image
        thresh_images = [self.getThreshold(image) for image in crop_images]
        # get all results
        results = [self.getAllResults(thresh, i) for i, thresh in enumerate(thresh_images)]
        # add dictioanry
        all_results = []
        for result in results:
            all_results += result
        # add count number
        all_results = dict(zip(range(1, len(all_results) + 1), all_results))

        return self.get_option(all_results)
