# MAPLM: A Large-Scale Vision-Language Dataset for Map and Traffic Scene Understanding

### [中文简介](./README-zh.md)

#### - WACV 2024 Workshop on Large Language Vision Models for Autonomous Driving (LLVM-AD)

![Poster](./figures/poster.png)

## Workshop Introduction
The full name of WACV is the Winter Conference on Applications of Computer Vision. It is one of the renowned conferences in the domain of computer vision applications, held annually. The initiated “Workshop on Large Language and Vision Models for Autonomous Driving (LLVM-AD)” is co-hosted by Tencent Maps, PediaMed AI Lab, University of Illinois at Urbana-Champaign, Purdue University, and University of Virginia. The workshop will discuss various topics from computer vision, pattern recognition, autonomous driving, to high-definition maps. It will contain paper submissions, competitions, and award-sharing sessions during WACV 2024. The aim is to gather professionals from both academia and the industry to explore applications of large language and vision models in autonomous driving and high-definition mapping. As part of the workshop plan, we will release two open-source datasets to promote research on understanding real-world traffic language. While using the datasets is recommended, it is not mandatory for paper submission related to these two datasets.    

## MAPLM Dataset     
Tencent Maps HD Map T.Lab, in collaboration with the University of Illinois at Urbana-Champaign, Purdue University, and the University of Virginia, have launched the industry's first multimodal language+vision (point cloud BEV+panoramic images) traffic scenario understanding dataset: MAPLM. MAPLM provides abundant road scenario images complemented with multi-level scene description data, aiding models in navigating complex and varied traffic environments.     

### Scene of MAPLM：    
MAPLM offers a variety of traffic scenarios, including highways, expressways, city roads, and rural roads, along with detailed intersection scenes. Each frame of data includes two components:           
✧ Point Cloud BEV: A projection image of 3D point cloud viewed from the BEV perspective with clear visuals and high resolution.        
✧ Panoramic Images: High-resolution photographs captured from front, left-rear, and right-rear angles by a wide-angle camera.    

### Annotations：    
✧ Feature-level: Lane lines, ground signs, stop lines, intersection areas, etc.        
✧ Lane-level: Lane types, directions of traffic, turn categories, etc.       
✧ Road-level: Scene types, road data quality, intersection structures, etc.     

### Data Display：    
Point Cloud BEV image + 3 panoramic photos. Note: Panoramic images are 4096*3000 portrait shots. The image below is only a cropped sample.   

![Poster](./figures/example1.png)

### Label Display：    
The image below illustrates one frame's annotation information, encompassing three parts: road-level information (in red font), lane-level information (yellow geometric lines + orange font), and intersection data (blue polygons + blue font).         

![Poster](./figures/example2.png)

## Workshop Tasks and Benefits     

Leveraging the rich road traffic scene information from the above dataset, we have designed a natural language and image combined Q&A task based on ScienceQA.    

### Task Introduction:   
We offer the following data or prior inputs:       
✓ Point Cloud BEV Image: 3D point cloud projection in BEV perspective.    
✓ Panoramic Images: Wide-angle camera shots covering front, left-rear, and right-rear angles.    
✓ Projection Conversion Parameters: Perspective projection conversion parameters for each frame's photo and point cloud image.     
Questions will randomly target various tag dimensions, such as scene type, number and attributes of lanes, presence of intersections, etc. Sample questions are as follows:      

![Poster](./figures/qa1.png)    

![Poster](./figures/qa2.png)    

### How to Participate:    
✓ Vision, multimodal integration, autonomous driving, high-definition mapping, and other relevant domain researchers or practitioners are welcome to join the challenge.    
✓ Apart from the workshop competition content, we'll invite guests for topic-related presentations. Interested parties are urged to keep an eye out and join this workshop for paper submissions.    
✓ Outstanding students in the workshop paper submissions and competitions may receive priority for internship opportunities at Tencent Maps Perception Machine Learning Engineer / Research Scientist positions.    
✓ Competition details are still being prepared. Please keep checking our workshop homepage for updates.        


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
  year={2024},
  publisher={Wiley Online Library}
}
```






