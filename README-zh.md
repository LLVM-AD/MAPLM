# MAPLM数据集
#### - WACV 2024自动驾驶大语言视觉基础模型研讨会（LLVM-AD）

## 研讨会介绍
WACV全称：Winter Conference on Applications of Computer Vision，是领域内著名的计算机视觉应用会议之一，每年举办一次。本次发起的“自动驾驶大语言视觉模型研讨会”，全称：1st Workshop on Large Language and Vision Models for Autonomous Driving (LLVM-AD)，由腾讯地图联合PediaMed AI Lab, University of Illinois Urbana-Champaign、Purdue University以及University of Virginia共同举办，针对计算机视觉、模式识别、自动驾驶、高精度地图等一系列领域的议题，组织论文投稿，比赛及获奖分享，将在WACV 2024期间举行。本次研讨会旨在汇集学术界和工业界的专业人士，探索大型语言和视觉模型在自动驾驶以及高精地图中的应用。
作为研讨会计划的一部分，我们将发布两个开源数据集，用于实现对真实世界交通语言理解的研究。

## 特色数据集·MAPLM     
腾讯地图HD自动化团队、University of Illinois Urbana-Champaign、Purdue University以及University of Virginia联合推出了业界首个多模态语言 + 视觉（点云BEV+环视图像）交通场景理解数据集：MAPLM。MAPLM提供丰富的道路场景图像资料，并配套多个层级的场景描述信息，让模型学会处理更复杂多变的交通环境。
场景资料：MAPLM提供了包含高速、快速路、城市道路、乡村道路在内的各类交通场景图像资料，配合丰富的路口场景。每一帧数据资料包括两个部分：    
✧点云BEV：3D点云在BEV视角下的投影图，图像清晰，分辨率高    
✧环视图像：广角相机拍摄的前视、左后、右后三个方向的高分辨率照片    
描述标签：    
✧要素级：车道线、地面标志、停止线、路口区域等    
✧车道级：车道类型、通行方向、转向类别等    
✧道路级：场景类型、道路数据质量、路口结构等    
数据资料展示：    
点云bev图+3张环视影像，注环视影像为4096*3000的竖幅照片，下图仅为裁切后的示例      

