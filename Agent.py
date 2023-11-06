# Allowable libraries:
# - Python 3.10.12
# - Pillow 10.0.0
# - numpy 1.25.2
# - OpenCV 4.6.0 (with opencv-contrib-python-headless 4.6.0.66)

# To activate image processing, uncomment the following imports:
from PIL import Image
import numpy as np
import cv2
import pdb
import heapq
import random

class Agent:
    def __init__(self):
        """
        The default constructor for your Agent. Make sure to execute any processing necessary before your Agent starts
        solving problems here. Do not add any variables to this signature; they will not be used by main().
        """
        pass

    def Solve(self, problem):
        #Problem[dict, "name", "type"]
        #dict[key:value,"A":1.png]
        def twobytwo(problem):
            darkimages = {}
            threshold = 128
        
            for key, figure in problem.figures.items():
                image = Image.open(figure.visualFilename)
                dark_figure = image.convert('L')
                img_pixels = dark_figure.load()

                dark_pixel_count = 0
                total_pixels = 0
                for x in range(dark_figure.width):
                    for y in range(dark_figure.height):
                        total_pixels += 1
                        pixel_value = img_pixels[x, y]
                        if pixel_value < threshold:
                            dark_pixel_count += 1
                if dark_pixel_count == 0:
                    dark_pixel_count += 1

                dark_ratio = dark_pixel_count / total_pixels
                darkimages[key] = dark_ratio

            def Horizontal_Compare(darkimages):
                h_ratio = darkimages["A"] / darkimages["B"]
                #print(h_ratio, "h_ratio")
                h_rated_ans = {}
                for key in darkimages:
                    if key.isdigit():
                        #print(key)
                        ans_ratio = darkimages["A"] / darkimages[key]
                        #print(ans_ratio, "ans_ratio")
                        diff = abs(h_ratio - ans_ratio)
                        #print(diff, "diff")
                        h_rated_ans[key] = diff
                return h_rated_ans

            def Vertical_Compare(darkimages):
                v_ratio = darkimages["A"] / darkimages["C"]
                v_rated_ans = {}
                for key in darkimages:
                    if key.isdigit():
                        ans_ratio = darkimages["A"] / darkimages[key]
                        diff = abs(v_ratio - ans_ratio)
                        v_rated_ans[key] = diff
                return v_rated_ans
            
            def Select_Answer(h_rated_ans, v_rated_ans):
            #add horizontal and vertical scores
                final_scores = []
                for key in h_rated_ans:
                    final_score = h_rated_ans[key] + v_rated_ans[key]
                    heapq.heappush(final_scores, [final_score, key])
                return int(heapq.heappop(final_scores)[-1])

            horizontal_values = Horizontal_Compare(darkimages)
            vertical_values = Vertical_Compare(darkimages)

            return Select_Answer(horizontal_values, vertical_values)
                
        def threebythree(problem):
            darkimages = {}
            threshold = 128
        
            for key, figure in problem.figures.items():
                image = Image.open(figure.visualFilename)
                dark_figure = image.convert('L')
                img_pixels = dark_figure.load()

                dark_pixel_count = 0
                #total_pixels = 0
                for x in range(dark_figure.width):
                    for y in range(dark_figure.height):
                        #total_pixels += 1
                        pixel_value = img_pixels[x, y]
                        if pixel_value < threshold:
                            dark_pixel_count += 1
                if dark_pixel_count == 0:
                    dark_pixel_count += 1

                #dark_ratio = dark_pixel_count / total_pixels
                darkimages[key] = dark_pixel_count
            
            def A_C(darkimages):
                A_C_ratio = darkimages["A"] / darkimages["C"]
                return A_C_ratio

            def D_F(darkimages):
                D_F_ratio = darkimages["D"] / darkimages["F"]
                return D_F_ratio
            
            def Select_Answer(A_C, D_F, darkimages):
                ratio_addition = D_F - A_C
                goal_ratio = D_F + ratio_addition

                scores = {}

                for key in darkimages:
                    if key.isdigit():
                        G_Blank = darkimages["G"] / darkimages[key]
                        scores[key] = abs(goal_ratio - G_Blank)
                return scores

            A_C_ratio = A_C(darkimages)
            D_F_ratio = D_F(darkimages)
            scoring = Select_Answer(A_C_ratio, D_F_ratio, darkimages)
            return int(min(scoring, key=scoring.get))

        if problem.problemType == "2x2":
            return twobytwo(problem)
        else:
            return threebythree(problem)
        
        """
        Primary method for solving incoming Raven's Progressive Matrices.

        Args:
            problem: The problem instance.

        Returns:
            int: The answer (1 to 6). Return a negative number to skip a problem.
            Remember to return the answer [Key], not the name, as the ANSWERS ARE SHUFFLED.
            DO NOT use absolute file pathing to open files.
        """

        # Example: Preprocess the 'A' figure from the problem.
        # Actual solution logic needs to be implemented.
        # image_a = self.preprocess_image(problem.figures["A"].visualFilename)

        # Placeholder: Skip all problems for now.
        #return 1