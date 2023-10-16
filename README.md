# MAPLM: A Large-Scale Vision-Language Dataset for Map and Traffic Scene Understanding

Tencent, University of Illinois at Urbana-Champaign, Purdue University, University of Virginia    

### [Chinese Introduction](./README-zh.md)

### Open-source datasets of 1st Workshop on Large Language Vision Models for Autonomous Driving (LLVM-AD) in WACV 2024

## LLVM-AD Workshop Introduction

The Winter Conference on Applications of Computer Vision (WACV) is a renowned conference in the field of computer vision applications, held annually. This conference will co-host the "Workshop on Large Language and Vision Models for Autonomous Driving (LLVM-AD)" in collaboration with Tencent Maps, PediaMed AI Lab, University of Illinois at Urbana-Champaign, Purdue University, and University of Virginia. The workshop will cover various topics including computer vision, pattern recognition, autonomous driving, and high-definition maps. It will include paper submissions, competitions, and award-sharing sessions during WACV 2024. The goal is to bring together professionals from academia and industry to explore the applications of large language and vision models in autonomous driving and high-definition mapping.     

As part of the workshop, we are releasing two open-source datasets to encourage research on understanding real-world traffic language. While using these datasets is recommended, it is not mandatory for paper submissions related to these two datasets.     

## MAPLM Dataset

Tencent Maps HD Map T.Lab, in collaboration with the University of Illinois at Urbana-Champaign, Purdue University, and the University of Virginia, has launched MAPLM, the industry's first multimodal language+vision traffic scenario understanding dataset. MAPLM combines point cloud BEV (Bird's Eye View) and panoramic images to provide a rich collection of road scenario images. This dataset also includes multi-level scene description data, which helps models navigate through complex and diverse traffic environments.     

### Scene of MAPLM：

MAPLM offers a variety of traffic scenarios, including highways, expressways, city roads, and rural roads, along with detailed intersection scenes. Each frame of data includes two components:                   
✧ Point Cloud BEV: A projection image of 3D point cloud viewed from the BEV perspective with clear visuals and high resolution.     

✧ Panoramic Images: High-resolution photographs captured from front, left-rear, and right-rear angles by a wide-angle camera.      

### Annotations：

✧ Feature-level: Lane lines, ground signs, stop lines, intersection areas, etc.          
✧ Lane-level: Lane types, directions of traffic, turn categories, etc.        
✧ Road-level: Scene types, road data quality, intersection structures, etc.     

### Data Display：    

3D Point Cloud, Extracted Point Cloud BEV image + multiple panoramic photos + HD Map annotations. Note: Panoramic images are 4096*3000 portrait shots. The image below is only a cropped sample.           

![Poster](./figures/example1.png)

### Label Display：

The image below illustrates one frame's annotation information, encompassing three parts: road-level information (in red font), lane-level information (yellow geometric lines + orange font), and intersection data (blue polygons + blue font).     

<!-- ![Poster](./figures/example2.png) -->

## Workshop Challenge

Leveraging the rich road traffic scene information from the above dataset, we have designed a natural language and image combined Q&A task.     

### Data

We offer the following data:       
✓ Point Cloud BEV Image: 3D point cloud projection in BEV perspective.    
✓ Panoramic Images: Wide-angle camera shots covering front, left-rear, and right-rear angles.    
✓ Projection Conversion Parameters: Perspective projection conversion parameters for each frame's photo and 3D point cloud.      

Questions will target various tag dimensions, such as scene type, number and attributes of lanes, presence of intersections, etc. Sample questions are as follows:     

![Poster](./figures/qa1.png)

![Poster](./figures/qa2.png)

### Evaluation      

We will evaluate the performance of models on the test set using the following accuracy metrics:

- Frame-overall-accuracy `(FRM)`: A frame is considered correct if all closed-choice questions about it are answered
  correctly.
- Question-overall-accuracy `(QNS)`: A question is considered correct if its answer is correct.
- Individual-question-accuracy: The accuracy of each specific closed-choice question, including:
    - How many lanes in current road? `(LAN)`
    - Is there any road cross, intersection or lane change zone in the main road? `(INT)`
    - What is the point cloud data quality in current road area of this image? `(QLT)`
    - What kind of road scene is it in the images? `(SCN)`

We can get the accuracy metrics of each question and the overall accuracy with `random guessing` by running:

```bash
cd tools
python random_chance.py
```

Change the random guess to your algorithm's prediction to get the evaluation results of your algorithm.

**Please submit your results by filling out this [form](https://forms.office.com/r/mapGsGWQNf). This will allow us to
update your results on the leaderboard.**

### Leaderboard

|      Method       | FRM  |  QNS  |  LAN  |  INT  |  QLT  |  SCN  |
|:-----------------:|:----:|:-----:|:-----:|:-----:|:-----:|:-----:|
| **Random Chance** | 0.00 | 19.55 | 21.00 | 16.73 | 25.20 | 15.27 |


### Data Release Timeline     

`09/2023` First part of QA data, including extracted Point Cloud BEV image + 3 panoramic images: [Link](https://drive.google.com/drive/folders/1cqFjBH8MLeP6nKFM0l7oV-Srfke-Mx1R?usp=sharing)     

`01/2024` HD Map data and image caption, including 2M of 3D Point Cloud, Extracted Point Cloud BEV image + multiple panoramic images + HD Map annotations.      
  

## UCU Dataset

[See this page](https://github.com/LLVM-AD/ucu-dataset)

## Citation

If the code, datasets, and research behind this workshop inspire you, please cite our work:

```
@inproceedings{tang2023thma,
  title={THMA: tencent HD Map AI system for creating HD map annotations},
  author={Tang, Kun and Cao, Xu and Cao, Zhipeng and Zhou, Tong and Li, Erlong and Liu, Ao and Zou, Shengtao and Liu, Chang and Mei, Shuqi and Sizikova, Elena and Zheng, Chao},
  booktitle={Proceedings of the AAAI Conference on Artificial Intelligence},
  volume={37},
  number={13},
  pages={15585--15593},
  year={2023}
}
```

```
@article{zheng2023hdmap,
  title={High-Definition Map Automatic Annotation System Based on Active Learning},
  author={Zheng, Chao and Cao, Xu and Tang, Kun and Cao, Zhipeng and Sizikova, Elena and Zhou, Tong and Li, Erlong and Liu, Ao and Zou, Shengtao and Yan, Xinrui and Mei, Shuqi},
  journal={AI Magazine},
  year={2023},
  publisher={Wiley Online Library}
}
```






